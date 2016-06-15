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