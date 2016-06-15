DROP TABLE IF EXISTS student;
CREATE TABLE student(
  id_studenta INTEGER PRIMARY KEY AUTOINCREMENT,
  id_temat INTEGER,
  email TEXT NOT NULL,
  nazwisko TEXT NOT NULL,
  imie TEXT NOT NULL,
  haslo TEXT NOT NULL,
  FOREIGN KEY (id_temat) REFERENCES temat_pracy(id_tematu)
);

DROP TABLE IF EXISTS wykladowca;
CREATE TABLE wykladowca(
  id_wykladowcy INTEGER PRIMARY KEY AUTOINCREMENT,
  imie TEXT NOT NULL,
  nazwisko TEXT NOT NULL,
  email TEXT NOT NULL,
  haslo TEXT NOT NULL
);

DROP TABLE IF EXISTS temat_pracy;
CREATE TABLE temat_pracy(
  id_tematu INTEGER PRIMARY KEY AUTOINCREMENT,
  id_wykladowca INTEGER,
  temat TEXT NOT NULL,
  czy_zajety INTEGER,
  FOREIGN KEY (id_wykladowca) REFERENCES wykladowca(id_wykladowcy)
);

DROP TABLE IF EXISTS wiadomosc;
CREATE TABLE wiadomosc(
  id_wiadomosci INTEGER PRIMARY KEY AUTOINCREMENT,
  id_wykladowca INTEGER,
  id_student INTEGER,
  tekst TEXT NOT NULL,
  data TEXT NOT NULL,
  temat TEXT NOT NULL,
  czy_przeczytane INTEGER,
  FOREIGN KEY (id_wykladowca) REFERENCES wykladowca(id_wykladowcy),
  FOREIGN KEY (id_student) REFERENCES student(id_studenta)
);

DROP TABLE IF EXISTS termin;
CREATE TABLE termin(
  id_terminu INTEGER PRIMARY KEY AUTOINCREMENT ,
  nazwa TEXT NOT NULL,
  data TEXT NOT NULL
);

DROP TABLE IF EXISTS student_etap;
CREATE TABLE student_etap(
  id_etapu INTEGER PRIMARY KEY AUTOINCREMENT,
  id_student INTEGER,
  id_termin INTEGER,
  czy_zakonczony INTEGER,
  FOREIGN KEY (id_student) REFERENCES student(id_studenta),
  FOREIGN KEY (id_termin) REFERENCES termin(id_terminu)
);