import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

# Konfiguracja

DATABASE = 'baza_danych/baza.db'
DEBUG=True
SECRET_KEY = 'development key'


app = Flask(__name__)
app.config.from_object(__name__)

def polacz_z_baza():
    return sqlite3.connect(app.config['DATABASE'])

def inicjuj_baze():
    with closing(polacz_z_baza()) as db:
        with app.open_resource('schemat_bazy.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def index():
    return 'Hello World!'


@app.route('/student/')
def student():
    return 'student main site !'

if __name__ == '__main__':
    app.run(debug=True)

