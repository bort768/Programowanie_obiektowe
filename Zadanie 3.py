class Alko:
    def __init__(self, nazwa,proc,cena,ilosc):
        self.nazwa = nazwa
        self.proc = proc
        self.cena = cena
        self.ilosc = ilosc



def main():

    # classy

    wodka = Alko("wódka", 40, 8, 50)
    rum = Alko("rum", 60, 9, 50)
    cola = Alko("cola", 0, 2, 100) # Dobre alko XD
    lod = Alko("lód", 0, 0, 30) # XD

    # zmienne

    vat = 0.23
    tablica = [[wodka.nazwa, wodka.proc,  wodka.cena,  wodka.ilosc],[rum.nazwa, rum.proc,  rum.cena, rum.ilosc],
               [cola.nazwa, cola.proc,  cola.cena, cola.ilosc],[lod.nazwa, lod.proc,  lod.cena,  lod.ilosc]]

    while True:         # main menu

        print('           Cennik              ')
        for i in range(4):
            print(i+1, tablica[i][0], tablica[i][1], '%',tablica[i][2],'zł', tablica[i][3],'ml')

        print('5.EXIT')
        x = int(input('---->: '))
        uwu = []
        # if'y do menu
        if  1 <= x <= 4:
            while True:
                try:
                    print('Czy chcesz połaczyć', nazwa_drinka, 'z:')
                except:
                    print('Czy chcesz połaczyć', tablica[x-1][0], 'z:')
                heh = 1
                for i in range(4):
                    try:
                        if submenu == i:
                            continue
                    except:
                        pass
                    if i == x-1: continue
                    else:
                        print(heh, tablica[i][0], tablica[i][1], '%', tablica[i][2], 'zł', tablica[i][3], 'ml')
                        heh = heh + 1
                        uwu.append(i)

                print('4.Cofnij')
                print('5.Zapłac')
                #print(uwu)   debug


                submenu = int(input('---->: '))
                if 1 <= submenu <= 3:
                    try:
                        nazwa_drinka = nazwa_drinka + ' i ' + tablica[uwu[submenu-1]][0]
                        naz_dri = 1
                    except:
                        naz_dri = 0
                        pass
                    if naz_dri == 0:
                        nazwa_drinka = tablica[x-1][0]+' z '+tablica[uwu[submenu-1]][0]

                    try:
                        cena_drinka = cena_drinka + tablica[uwu[submenu-1]][2]
                        cen_dri = 1
                    except:
                        cen_dri = 0
                        pass
                    if cen_dri == 0:
                        cena_drinka = (tablica[x - 1][2] + tablica[uwu[submenu - 1]][2])

                    try:
                        if tablica[uwu[submenu-1]][1] == 0:
                            procent_drinka = (procent_drinka * ilosc_drinka) / (ilosc_drinka + tablica[uwu[submenu-1]][3])
                        else:
                            procent_drinka = procent_drinka + ((tablica[uwu[submenu-1]][1]/100)*tablica[uwu[submenu-1]][3]) / (ilosc_drinka + tablica[uwu[submenu-1]][3])
                        pro_dri = 1
                    except:
                        pro_dri = 0
                        pass
                    if pro_dri == 0:
                        if tablica[uwu[submenu-1]][1] == 0:
                            procent_drinka = ((tablica[x - 1][1] / 100) * tablica[x - 1][3]) / (tablica[x - 1][3] + tablica[uwu[submenu - 1]][3]    )
                        else:
                            procent_drinka = ((tablica[x - 1][1] / 100) * tablica[x - 1][3]) + (
                                    (tablica[uwu[submenu - 1]][1] / 100) * tablica[uwu[submenu - 1]][3]) / (tablica[x - 1][3] + tablica[uwu[submenu - 1]][3]    )

                    try:
                        ilosc_drinka = ilosc_drinka + tablica[uwu[submenu-1]][3]
                        ilo_dri = 1
                    except:
                        ilo_dri = 0
                        pass
                    if ilo_dri == 0:
                        ilosc_drinka = tablica[x-1][3]+tablica[uwu[submenu-1]][3]
                    uwu.clear()
                    print(nazwa_drinka)
                    print('Cena:', cena_drinka * (1 + vat))
                    print('Procent', round(procent_drinka, 2),'%')
                    print('Ilość:',  ilosc_drinka, 'ml')
                    czekaj = input()
                    czekaj = 1

                if submenu == 4: break

                if submenu == 5:
                    try:
                        if czekaj == 1:
                            print(nazwa_drinka)
                            print('Cena:', cena_drinka * (1 + vat))
                            print('Procent', round(procent_drinka, 2),'%')
                            print('Ilość:',  ilosc_drinka, 'ml')
                    except:
                        print(tablica[i][0], tablica[i][1], '%',tablica[i][3], 'ml')
                        print('Do zapłaty', tablica[x-1][2]*(1+vat),'zł')

                    exit()
                continue
        if x == 5:

            exit()
        exit()

main()
