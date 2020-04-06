class Pracownik:
    def __init__(self):
        self.__imie = "Jan"
        self.__nazwisko = "Kowalski"
        self.__zarobki = "3400"
    def dane(self,plec,stanowisko):
        self.__plec = plec
        self.__stanowisko = stanowisko
    def wypisz(self):
        print('Imie ', self.__imie)
        print('Nazwisko ', self.__nazwisko)
        print('Zarobki ', self.__zarobki)
        print('Płec ', self.__plec)
        print('Stanowisko ', self.__stanowisko)
    def setcostam(self,imie,nazwisko,zarobki): # jak ktoś by chciał zmienić wartosc
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__zarobki = zarobki

pracownik_01 = Pracownik()
pracownik_01.dane("Helikopter","Tester")
pracownik_01.wypisz()
