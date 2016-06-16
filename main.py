import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
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
        pass
    return render_template('student_signin.html', error=error)


# strona z logowaniem wykladowcy
@app.route('/signin_lecturer', methods=['GET', 'POST'])
def signin_lecturer():
    error = None
    if request.method == 'POST':
        pass
    return render_template('lecturer_signin.html', error=error)


# strona wyswietlajaca wszystkich studentow w panelu wykladowcy
@app.route('/database', methods=['GET'])
def database():
    cur = g.db.execute('SELECT student.id_studenta, student.imie, student.nazwisko, student.email, temat_pracy.temat'
                       ' FROM student INNER JOIN temat_pracy '
                       'ON student.id_studenta = temat_pracy.id_tematu;')
    users = [dict(id=row[0], name=row[1], surname=row[2], email=row[3], subject=row[4]) for row in cur.fetchall()]
    return render_template('lecturer_control.html', students=users)


# strona wyswietlajaca teamty prac dla wykladowcy
@app.route('/subjects', methods=['GET'])
def subjects():
    id = "1"
    cur = g.db.execute(
        'SELECT temat_pracy.id_tematu, temat_pracy.temat, temat_pracy.czy_zajety FROM temat_pracy WHERE id_wykladowca = ' + id + ';')
    my_subjects = [dict(id=row[0], temat=row[1], czy_zajety=row[2]) for row in cur.fetchall()]
    cur = g.db.execute(
        'SELECT temat_pracy.id_tematu, temat_pracy.temat, temat_pracy.czy_zajety FROM temat_pracy WHERE id_wykladowca != ' + id + ';')
    all_subjects = [dict(id=row[0], temat=row[1], czy_zajety=row[2]) for row in cur.fetchall()]
    return render_template('lecturer_subjects.html', my_subjects=my_subjects, all_subjects=all_subjects)


# strona wyswietlajaca terminy
@app.route('/terms', methods=['GET'])
def terms():
    cur = g.db.execute('SELECT nazwa, data FROM termin')
    terms = [dict(nazwa=row[0], data=row[1]) for row in cur.fetchall()]
    return render_template('lecturer_terms.html', terms=terms)


# funkcja dodajaca termin do bazy
@app.route('/add_term', methods=['POST'])
def add_term():
    return redirect(url_for('terms'))


# profil wykladowcy
@app.route('/profile_lecturer')
def profile_lecturer():
    return render_template('lecturer_profile.html')


# profil studenta
@app.route('/profile_student')
def profile_student():
    return render_template('student_profile.html')


# wiadomosci wykladowcy
@app.route('/message_lecturer')
def message_lecturer():
    cur = g.db.execute('SELECT id_wiadomosci, temat, id_student, data'
                       ' FROM wiadomosc')

    messages = [dict(id=row[0], temat=row[1], nadawca=row[2], data=row[3]) for row in cur.fetchall()]
    return render_template('lecturer_message.html', messages=messages)


@app.route('/show_message', methods=['POST'])
def show_message():
    return render_template('lecturer_show_message.html',
                           message=dict(temat="Dupa", nadawca="CHuj", data="Wczoraj", tresc="Bylem tam"))


@app.route('/reply')
def reply():
    return render_template('lecturer_new_message.html')


@app.route('/send')
def send():
    return render_template('lecturer_message.html')


@app.route('/new_message')
def new_message():
    return render_template('lecturer_new_message.html')


# wiadomosci studenta
@app.route('/message_student')
def message_student():
    return render_template('student_message.html')


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
    return redirect(url_for('index'))


# porownywanie daty
def compare_date():
    pass


if __name__ == '__main__':
    app.run(debug=True)
