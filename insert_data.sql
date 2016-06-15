/* uzupelnienie terminow */
insert into termin (nazwa, data) values ('Wydanie tematu pracy','2016-06-25 12:00:00');
insert into termin (nazwa, data) values ('Wniesienie opłaty za dyplom','2016-10-15 12:00:00');
insert into termin (nazwa, data) values ('Pierwsze spotkanie z promotorem (oddanie wstępu oraz planu pracy)','2016-10-30 12:00:00');
insert into termin (nazwa, data) values ('Oddanie pierwszego rozdziału pracy dyplomowej','2016-11-15 12:00:00');
insert into termin (nazwa, data) values ('Oddanie drugiego rozdziału pracy dyplomowej','2016-12-01 12:00:00');
insert into termin (nazwa, data) values ('Oddanie trzeciego rozdziału pracy dyplomowej','2016-12-15 12:00:00');
insert into termin (nazwa, data) values ('Oddanie czwartego rozdziału pracy dyplomowej','2017-01-03 12:00:00');
insert into termin (nazwa, data) values ('Oddanie piątego rozdziału pracy dyplomowej','2017-01-15 12:00:00');
insert into termin (nazwa, data) values ('Oddanie streczenia pracy w dwóch wersjach językowych','2017-01-20 12:00:00');
insert into termin (nazwa, data) values ('Złożenie podania o dopuszczenie do obrony','2017-02-01 12:00:00');
insert into termin (nazwa, data) values ('Złożenie pracy dyplomowej','2017-02-10 12:00:00');
insert into termin (nazwa, data) values ('Otrzymanie recenzji pracy dyplomowej','2017-02-17 12:00:00');
insert into termin (nazwa, data) values ('Obrona pracy dyplomowej','2017-02-20 12:00:00');
insert into termin (nazwa, data) values ('Odbiór dyplomu','2017-03-20 12:00:00');

/* wykladowcy */
insert into wykladowca (imie, nazwisko, email, haslo) values ('Piotr', 'Pleban', 'plebanp@op.pl', '1234');
insert into wykladowca (imie, nazwisko, email, haslo) values ('Mateusz', 'Nowak', 'plebanp@op.pl', '1234');
insert into wykladowca (imie, nazwisko, email, haslo) values ('Michał', 'Kowalski', 'plebanp@op.pl', '1234');
insert into wykladowca (imie, nazwisko, email, haslo) values ('Jacek', 'Lewandowski', 'plebanp@op.pl', '1234');
insert into wykladowca (imie, nazwisko, email, haslo) values ('Kamil', 'Kapustka', 'plebanp@op.pl', '1234');
insert into wykladowca (imie, nazwisko, email, haslo) values ('Tomasz', 'Grosicki', 'plebanp@op.pl', '1234');
insert into wykladowca (imie, nazwisko, email, haslo) values ('Konrad', 'Szczęsny', 'plebanp@op.pl', '1234');

/* tematy prac */
insert into temat_pracy (id_wykladowca, temat, czy_zajety) values (1, 'System obsługi redakcji studenckiego czasopisma internetowego', 0);
insert into temat_pracy (id_wykladowca, temat, czy_zajety) values (2, 'Projekt i implementacja modułu statystyk w systemie eProto', 0);
insert into temat_pracy (id_wykladowca, temat, czy_zajety) values (3, 'Repozytorium dokumentów dla redakcji czasopisma naukowego', 0);
insert into temat_pracy (id_wykladowca, temat, czy_zajety) values (4, 'System wizualizacji i analizy reguł decyzyjnych do zastosowań medycznych', 0);
insert into temat_pracy (id_wykladowca, temat, czy_zajety) values (5, 'Symulacja i wizualizacja ekosystemu', 0);
insert into temat_pracy (id_wykladowca, temat, czy_zajety) values (6, 'Uczenie maszynowe z milionami klas (Jak poprawnie wybrać kilka z miliona?)', 0);
insert into temat_pracy (id_wykladowca, temat, czy_zajety) values (7, 'Wykorzystanie środowiska webowego do rozproszonych obliczeń wielkiej skali', 0);

/* studenci */
insert into student (id_temat, email, nazwisko, imie, haslo) values (1, 'rafalrutyna00@gmail.com', 'Rutyna', 'Rafał', '1234');
insert into student (id_temat, email, nazwisko, imie, haslo) values (2, 'rafalrutyna00@gmail.com', 'Pyśk', 'Piotr', '1234');
insert into student (id_temat, email, nazwisko, imie, haslo) values (3, 'rafalrutyna00@gmail.com', 'Nowak', 'Janusz', '1234');
insert into student (id_temat, email, nazwisko, imie, haslo) values (4, 'rafalrutyna00@gmail.com', 'Milik', 'Arkadiusz', '1234');
insert into student (id_temat, email, nazwisko, imie, haslo) values (5, 'rafalrutyna00@gmail.com', 'Boruc', 'Artur', '1234');
insert into student (id_temat, email, nazwisko, imie, haslo) values (6, 'rafalrutyna00@gmail.com', 'Fabiański', 'Łukasz', '1234');
insert into student (id_temat, email, nazwisko, imie, haslo) values (7, 'rafalrutyna00@gmail.com', 'Krychowiak', 'Grzegorz', '1234');

/* etap pracy dla każdego studenta */
insert into student_etap (id_student, id_termin, czy_zakonczony) values (1,1,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (1,2,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (1,3,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (1,4,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (1,5,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (1,6,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (1,7,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (1,8,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (1,9,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (1,10,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (1,11,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (1,12,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (1,13,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (1,14,0);

insert into student_etap (id_student, id_termin, czy_zakonczony) values (2,1,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (2,2,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (2,3,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (2,4,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (2,5,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (2,6,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (2,7,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (2,8,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (2,9,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (2,10,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (2,11,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (2,12,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (2,13,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (2,14,0);

insert into student_etap (id_student, id_termin, czy_zakonczony) values (3,1,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (3,2,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (3,3,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (3,4,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (3,5,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (3,6,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (3,7,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (3,8,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (3,9,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (3,10,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (3,11,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (3,12,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (3,13,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (3,14,0);

insert into student_etap (id_student, id_termin, czy_zakonczony) values (4,1,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (4,2,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (4,3,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (4,4,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (4,5,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (4,6,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (4,7,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (4,8,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (4,9,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (4,10,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (4,11,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (4,12,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (4,13,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (4,14,0);

insert into student_etap (id_student, id_termin, czy_zakonczony) values (5,1,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (5,2,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (5,3,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (5,4,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (5,5,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (5,6,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (5,7,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (5,8,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (5,9,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (5,10,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (5,11,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (5,12,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (5,13,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (5,14,0);

insert into student_etap (id_student, id_termin, czy_zakonczony) values (6,1,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (6,2,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (6,3,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (6,4,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (6,5,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (6,6,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (6,7,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (6,8,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (6,9,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (6,10,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (6,11,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (6,12,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (6,13,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (6,14,0);

insert into student_etap (id_student, id_termin, czy_zakonczony) values (7,1,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (7,2,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (7,3,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (7,4,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (7,5,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (7,6,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (7,7,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (7,8,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (7,9,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (7,10,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (7,11,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (7,12,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (7,13,0);
insert into student_etap (id_student, id_termin, czy_zakonczony) values (7,14,0);