# import sys
# from accountant import dotychczasowa_historia_operacji
# from accountant import historia_operacji
# from accountant import historia_na_dzialania
# from accountant import zapis_do_pliku


class Manager:
    def __init__(self, file_path):
        self.saldo = 0
        self.magazyn = {}
        self.historia_operacji = []
        self.file_path = file_path
        self.dotychczasowa_historia_operacji()
        self.historia_na_dzialania()


    # wczytywanie danych z zewnętrznego pliku z historią operacji i zapisanie ich do historii operacji wewnątrz programu
    def dotychczasowa_historia_operacji(self):
        with open(self.file_path, 'r') as f:
            while True:
                dana_z_wejscia = f.readline().strip()
                if dana_z_wejscia == "saldo":
                    zmiana_na_koncie = f.readline().strip()
                    nazwa_operacji = f.readline().strip()
                    obecna_lista = (dana_z_wejscia, zmiana_na_koncie, nazwa_operacji)
                elif dana_z_wejscia == "zakup":
                    nazwa_zakup = f.readline().strip()
                    cena_szt_zakup = f.readline().strip()
                    ilosc_zakup = f.readline().strip()
                    obecna_lista = (dana_z_wejscia, nazwa_zakup, cena_szt_zakup, ilosc_zakup)
                elif dana_z_wejscia == "sprzedaz":
                    nazwa_sprzedaz = f.readline().strip()
                    cena_szt_sprzedaz = f.readline().strip()
                    ilosc_sprzedaz = f.readline().strip()
                    obecna_lista = (dana_z_wejscia, nazwa_sprzedaz, cena_szt_sprzedaz, ilosc_sprzedaz)
                elif dana_z_wejscia == "stop":
                    break
                else:
                    print("Błąd")
                    break
                self.historia_operacji.append(obecna_lista)

    def saldo_func(self, polecenie):
        kwota = polecenie[1]
        self.saldo += int(kwota)
        if self.saldo < 0:
            print("Brak wystarczających środków na koncie do przeprowadzenia operacji")

    def zakup_func(self, polecenie):
        kwota = int(polecenie[2]) * int(polecenie[3])
        self.saldo -= kwota
        if self.saldo < 0 or int(polecenie[2]) < 0 or int(polecenie[3]) < 0:
            print("Błąd")
        przedmiot = polecenie[1]
        if not self.magazyn.get(przedmiot):
            self.magazyn[przedmiot] = 0
        self.magazyn[przedmiot] += int(polecenie[3])

    def sprzedaz_func(self, polecenie):
        kwota = int(polecenie[2]) * int(polecenie[3])
        self.saldo += kwota
        liczba_sztuk_w_magazynie = int(self.magazyn[polecenie[1]])
        if liczba_sztuk_w_magazynie < int(polecenie[3]) or int(polecenie[2]) < 0 or int(polecenie[3]) < 0:
            print("Błąd")
        self.magazyn[polecenie[1]] -= int(polecenie[3])

    # przerobienie historii operacji na działania
    def historia_na_dzialania(self):
        for polecenie in self.historia_operacji:
            if polecenie[0] == "saldo":
                self.saldo_func(polecenie)
            elif polecenie[0] == "zakup":
                self.zakup_func(polecenie)
            elif polecenie[0] == "sprzedaz":
                self.sprzedaz_func(polecenie)
            else:
                break

    # zapisanie danych historii operacji do pliku
    def zapis_do_pliku(self):
        with open(self.file_path, 'w') as f:
            f.write("")
        with open(self.file_path, 'a') as f:
            for element in self.historia_operacji:
                for element2 in element:
                    f.write(element2 + "\n")
            f.write("stop" + "\n")



# def sprzedaz_func(abc):
#     dotychczasowa_historia_operacji()
#     # wczytanie danych wejsciowych uruchamiających program i zapisanie ich w historii operacji
#     nazwa_zakup = sys.argv[2]
#     cena_jednostkowa = sys.argv[3]
#     liczba_sztuk = sys.argv[4]
#     obecna_lista = (sys.argv[0][0:len(sys.argv[0])-3], nazwa_zakup, cena_jednostkowa, liczba_sztuk)
#     historia_operacji.append(obecna_lista)
#     historia_operacji.append(("stop",))
#
#     if historia_na_dzialania() == "Błąd":
#         print("Błąd")
#     else:
#         zapis_do_pliku()






