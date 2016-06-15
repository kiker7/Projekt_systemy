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
    return render_template('signin_student.html', error=error)


# strona z logowaniem wykladowcy
@app.route('/signin_lecturer', methods=['GET', 'POST'])
def signin_lecturer():
    error = None
    if request.method == 'POST':
        pass
    return render_template('signin_lecturer.html', error=error)


# strona wyswietlajaca wszystkich studentow w panelu wykladowcy
@app.route('/database', methods=['GET'])
def database():
    cur = g.db.execute('select student.id_studenta, student.imie, student.nazwisko, student.email, temat_pracy.temat'
                       ' from student inner join temat_pracy '
                       'on student.id_studenta = temat_pracy.id_tematu;')
    users = [dict(id=row[0], name=row[1], surname=row[2], email=row[3], subject=row[4]) for row in cur.fetchall()]
    return render_template('control_panel.html', students=users)


# strona wyswietlajaca teamty prac dla wykladowcy
@app.route('/subjects', methods=['GET'])
def subjects(id):
    cur = g.db.execute('select temat_pracy.temat from temat_pracy where id_wykladowca = ' + id + ';')
    my_subjects = [dict(temat=row[0]) for row in cur.fetchall()]
    cur = g.db.execute('select * from temat_pracy.temat where id_wykladowca != ' + id + ';')
    all_subjects = [dict(temat=row[0]) for row in cur.fetchall()]
    return render_template('lecturer_subjects.html', my_subjects=my_subjects, all_subjects=all_subjects)


# strona wyswietlajaca terminy
def terms():
    cur = g.db.execute('select temat, data, tekst from wiadomosc')
    terms = [dict(temat=row[0], data=row[2], tekst=row[3]) for row in cur.fetchall()]
    return render_template('terms.html', terms=terms)

# funkcja dodajaca termin do bazy
def add_term():
    render_template('terms.html')

# profil wykladowcy
@app.route('/profile_lecturer')
def profile_lecturer():
    return render_template('profil_lecturer.html')


# profil studenta
@app.route('/profile_student')
def profile_student():
    return render_template('profil_student.html')


# wiadomosci wykladowcy
@app.route('/message_lecturer')
def message_lecturer():
    return render_template('message_lecturer.html')


# wiadomosci studenta
@app.route('/message_student')
def message_student():
    return render_template('message_student.html')


# postep prac studenta
@app.route('/work_progress')
def work_progress():
    return render_template('work_progress.html')


# wylogowanie
@app.route('/signout')
def signout():
    return redirect(url_for('login.html'))


# porownywanie daty
def compare_date():
    pass

if __name__ == '__main__':
    app.run(debug=True)
