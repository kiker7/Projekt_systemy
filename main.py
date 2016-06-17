import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
from time import gmtime, strftime
import os, smtplib

# Konfiguracja

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'baza_danych', 'baza.db')

DEBUG = True
SECRET_KEY = 'development key'
SERVER_MAIL = 'rraf@spoko.pl'
SERVER_PASS = 'Mahdi248'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schemat_bazy.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def send_mail(msg, email_to):
    email_from = app.config['SERVER_MAIL']
    email_pass = app.config['SERVER_PASS']
    server = smtplib.SMTP('smtp.poczta.onet.pl:587')
    server.starttls()
    server.login(email_from, email_pass)
    server.sendmail(email_from, email_to, msg)
    server.quit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    return render_template('login.html')


# strona z logowaniem studenta
@app.route('/signin_student', methods=['GET', 'POST'])
def signin_student():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cur = g.db.execute('SELECT email, haslo, id_studenta FROM student')
        dane = [dict(email=row[0], password=row[1], id=row[2]) for row in cur.fetchall()]
        for i in dane:
            if i.get('email') == email and i.get('password') == password:
                session['logged_in'] = True
                session['id'] = i.get('id')
                return redirect(url_for('profile_student'))
            else:
                error = 'Bledne dane logowania'
        return render_template('student_signin.html', error=error)
    return render_template('student_signin.html')


# strona z logowaniem wykladowcy
@app.route('/signin_lecturer', methods=['GET', 'POST'])
def signin_lecturer():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cur = g.db.execute('SELECT email, haslo, id_wykladowcy FROM wykladowca')
        dane = [dict(email=row[0], password=row[1], id=row[2]) for row in cur.fetchall()]
        for i in dane:
            if i.get('email') == email and i.get('password') == password:
                session['logged_in'] = True
                session['id'] = i.get('id')
                return redirect(url_for('profile_lecturer'))
            else:
                error = 'Bledne dane logowania'
        return render_template('lecturer_signin.html', error=error)
    return render_template('lecturer_signin.html')


# strona wyswietlajaca wszystkich studentow w panelu wykladowcy
@app.route('/database', methods=['GET'])
def database():
    cur = g.db.execute('SELECT student.id_studenta, student.imie, student.nazwisko, student.email, temat_pracy.temat'
                       ' FROM student INNER JOIN temat_pracy '
                       'ON student.id_studenta = temat_pracy.id_tematu;')
    users = [dict(id=row[0], name=row[1], surname=row[2], email=row[3], subject=row[4]) for row in cur.fetchall()]
    return render_template('lecturer_control.html', students=users)


# strona wyswietlajaca teamty prac dla wykladowcy
@app.route('/subjects', methods=['GET', 'POST'])
def subjects():
    id = session['id']
    cur = g.db.execute(
        'SELECT temat_pracy.id_tematu, temat_pracy.temat, temat_pracy.czy_zajety FROM temat_pracy WHERE id_wykladowca = ' + str(
            id) + ';')
    my_subjects = [dict(id=row[0], temat=row[1], czy_zajety=row[2]) for row in cur.fetchall()]
    cur = g.db.execute(
        'SELECT temat_pracy.id_tematu, temat_pracy.temat, temat_pracy.czy_zajety FROM temat_pracy WHERE id_wykladowca != ' + str(
            id) + ';')
    all_subjects = [dict(id=row[0], temat=row[1], czy_zajety=row[2]) for row in cur.fetchall()]
    return render_template('lecturer_subjects.html', my_subjects=my_subjects, all_subjects=all_subjects)


@app.route('/add_subject', methods=['POST'])
def add_subject():
    temat = request.form['temat']
    g.db.execute('INSERT INTO temat_pracy(id_wykladowca, temat, czy_zajety) VALUES (?, ?, ?)', [1, temat, 0])
    g.db.commit()
    return subjects()


# strona wyswietlajaca terminy
@app.route('/terms', methods=['GET'])
def terms():
    cur = g.db.execute('SELECT nazwa, data, id_terminu FROM termin')
    terms = [dict(nazwa=row[0], data=row[1], id=row[2]) for row in cur.fetchall()]
    return render_template('lecturer_terms.html', terms=terms)


# profil wykladowcy
@app.route('/profile_lecturer')
def profile_lecturer():
    id = session['id']
    cur = g.db.execute(
        'SELECT wykladowca.imie, wykladowca.nazwisko, wykladowca.email FROM wykladowca WHERE id_wykladowcy =' + str(
            id) + ';')
    dane = [dict(imie=row[0], nazwisko=row[1], email=row[2]) for row in cur.fetchall()]
    return render_template('lecturer_profile.html', dane=dane)


# profil studenta
@app.route('/profile_student')
def profile_student():
    id = session['id']
    cur = g.db.execute(
        'SELECT student.imie, student.nazwisko, student.email, temat_pracy.temat FROM student INNER JOIN temat_pracy ON student.id_temat = temat_pracy.id_tematu WHERE id_studenta = ' + str(
            id) + ';')
    dane = [dict(imie=row[0], nazwisko=row[1], email=row[2], temat=row[3]) for row in cur.fetchall()]
    return render_template('student_profile.html', dane=dane)


# wiadomosci wykladowcy
@app.route('/message_lecturer')
def message_lecturer():
    cur = g.db.execute(
        'SELECT wiadomosc.id_wiadomosci, wiadomosc.temat, student.email, wiadomosc.data, wiadomosc.tekst FROM wiadomosc INNER JOIN student ON wiadomosc.id_student = student.id_studenta ORDER BY id_wiadomosci DESC;')
    messages = [dict(id=row[0], temat=row[1], nadawca=row[2], data=row[3], tekst=row[4]) for row in cur.fetchall()]
    return render_template('lecturer_message.html', messages=messages)


@app.route('/show_message', methods=['POST'])
def show_message():
    id_tematu = request.form['id_wiadomosci']
    cur = g.db.execute(
        'SELECT wiadomosc.id_wiadomosci, wiadomosc.temat, wiadomosc.data, wiadomosc.tekst, student.email FROM wiadomosc INNER JOIN student WHERE wiadomosc.id_student = student.id_studenta AND wiadomosc.id_wiadomosci = ' + id_tematu + ' ;')
    message = [dict(id=row[0], temat=row[1], data=row[2], tekst=row[3], email=row[4]) for row in cur.fetchall()]
    return render_template('lecturer_show_message.html',
                           message=dict(temat=message[0].get('temat'), email=message[0].get('email'),
                                        data=message[0].get('data'), tekst=message[0].get('tekst')))


@app.route('/show_student_message', methods=['POST'])
def show_student_message():
    id_tematu = request.form['id_wiadomosci']
    cur = g.db.execute(
        'SELECT wiadomosc.id_wiadomosci, wiadomosc.temat, wiadomosc.data, wiadomosc.tekst, student.email FROM wiadomosc INNER JOIN student WHERE wiadomosc.id_student = student.id_studenta AND wiadomosc.id_wiadomosci = ' + id_tematu + ' ;')
    message = [dict(id=row[0], temat=row[1], data=row[2], tekst=row[3], email=row[4]) for row in cur.fetchall()]
    return render_template('student_show_message.html',
                           message=dict(temat=message[0].get('temat'), email=message[0].get('email'),
                                        data=message[0].get('data'), tekst=message[0].get('tekst')))


@app.route('/change_term', methods=['POST', "GET"])
def change_term():
    datetime = list(str(request.form['datetime']))
    if not datetime:
        return terms()
    datetime.append(':00')
    id_terminu = request.form['id']
    datetime[10] = ' '
    date = ''.join(datetime)
    g.db.execute('UPDATE termin SET data=?  WHERE id_terminu=?', [date, id_terminu])
    g.db.commit()
    return terms()


@app.route('/reply_lecturer', methods=['GET', 'POST'])
def reply_lecturer():
    nadawca = request.form['nadawca']
    return render_template('lecturer_reply.html', email=dict(email=nadawca))


@app.route('/reply_student', methods=['POST'])
def reply_student():
    nadawca = request.form['nadawca']
    return render_template('student_reply.html', email=dict(email=nadawca))


@app.route('/send_lecturer', methods=['POST', 'GET'])
def send_lecturer():
    temat = request.form['temat']
    tresc = request.form['tresc']
    email = request.form['email']
    cur = g.db.execute('SELECT id_studenta FROM student WHERE email LIKE ?', [email])
    result = [dict(id=row[0]) for row in cur.fetchall()]
    if not result:
        cur = g.db.execute('SELECT id_wykladowcy FROM wykladowca WHERE email LIKE ?', [email])
        result = [dict(id=row[0]) for row in cur.fetchall()]
    if not result:
        result = [dict(id=1)]
    g.db.execute(
        'INSERT INTO wiadomosc(id_wykladowca, id_student, tekst, data, temat, czy_przeczytane) VALUES (?, ?, ?, ?, ?, ?)',
        [session['id'], result[0].get('id'), tresc, strftime("%Y-%m-%d %H:%M:%S", gmtime()), temat, 0])
    g.db.commit()
    return message_lecturer()


@app.route('/send_student', methods=['POST'])
def send_student():
    temat = request.form['temat']
    tresc = request.form['tresc']
    email = request.form['email']
    id = session['id']
    cur = g.db.execute('SELECT id_wykladowcy FROM wykladowca WHERE email LIKE ?', [email])
    result = [dict(id=row[0]) for row in cur.fetchall()]
    if not result:
        cur = g.db.execute('SELECT id_studenta FROM student WHERE email LIKE ?', [email])
        result = [dict(id=row[0]) for row in cur.fetchall()]
    if not result:
        result = [dict(id=1)]
    g.db.execute(
        'INSERT INTO wiadomosc(id_wykladowca, id_student, tekst, data, temat, czy_przeczytane) VALUES (?, ?, ?, ?, ?, ?)',
        [str(id), result[0].get('id'), tresc, strftime("%Y-%m-%d %H:%M:%S", gmtime()), temat, 0])
    g.db.commit()
    return message_student()


@app.route('/new_message_lecturer')
def new_message_lecturer():
    return render_template('lecturer_new_message.html')


@app.route('/new_message_student')
def new_message_student():
    return render_template('student_new_message.html')


# wiadomosci studenta
@app.route('/message_student')
def message_student():
    cur = g.db.execute(
        'SELECT wiadomosc.id_wiadomosci, wiadomosc.temat, student.email, wiadomosc.data, wiadomosc.tekst FROM wiadomosc INNER JOIN student ON wiadomosc.id_student = student.id_studenta ORDER BY id_wiadomosci DESC ')
    messages = [dict(id=row[0], temat=row[1], nadawca=row[2], data=row[3], tekst=row[4]) for row in cur.fetchall()]
    return render_template('student_message.html', messages=messages)


# postep prac studenta
@app.route('/work_progress')
def work_progress():
    cur = g.db.execute('SELECT count(*) FROM student_etap WHERE id_student = 1 AND czy_zakonczony = 1;')
    closest_term = [dict(number=row[0] + 1) for row in cur.fetchall()]
    cur = g.db.execute(
        'SELECT termin.id_terminu, termin.nazwa, termin.data FROM termin INNER JOIN student_etap ON termin.id_terminu = student_etap.id_termin WHERE student_etap.czy_zakonczony = 0 AND termin.id_terminu = ' + str(
            closest_term[0].get('number')) + ' AND student_etap.id_student = 1  ;')
    closest_term_name = [dict(id=row[0], nazwa=row[1], data=row[2]) for row in cur.fetchall()]
    cur = g.db.execute(
        'SELECT termin.id_terminu, termin.nazwa, termin.data FROM termin INNER JOIN student_etap ON termin.id_terminu = student_etap.id_termin WHERE student_etap.czy_zakonczony = 0 AND student_etap.id_student = 1;')
    next_terms = [dict(id=row[0], nazwa=row[1], data=row[2]) for row in cur.fetchall()]
    cur = g.db.execute(
        'SELECT termin.id_terminu, termin.nazwa, termin.data FROM termin INNER JOIN student_etap ON termin.id_terminu = student_etap.id_termin WHERE student_etap.czy_zakonczony = 1 AND student_etap.id_student = 1;')
    done_terms = [dict(id=row[0], nazwa=row[1], data=row[2]) for row in cur.fetchall()]
    return render_template('student_control.html', closest_term_name=closest_term_name, next_terms=next_terms,
                           done_terms=done_terms)


# tematy prac dyplomowych
@app.route('/student_subjects')
def student_subjects():
    cur = g.db.execute(
        'SELECT temat_pracy.id_tematu, temat_pracy.temat, temat_pracy.czy_zajety, wykladowca.imie, wykladowca.nazwisko FROM temat_pracy INNER JOIN wykladowca ON temat_pracy.id_wykladowca=wykladowca.id_wykladowcy;')
    subjects = [dict(id=row[0], temat=row[1], czy_zajety=row[2], imie=row[3], nazwisko=row[4]) for row in
                cur.fetchall()]
    return render_template('student_subjects.html', subjects=subjects)


# wylogowanie
@app.route('/signout')
def signout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))


# porownywanie daty
def compare_date():
    pass


if __name__ == '__main__':
    app.run(debug=True)
