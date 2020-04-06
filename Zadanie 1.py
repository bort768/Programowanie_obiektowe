class Pilkarz:
    def Strzelgola(self):
        print('Zostala strzelona bramka')

class PilakrzReczny(Pilkarz):
    def strelic(Pikarz):
        def gol():
            print("Reczny strzelil!!")
        return gol()

class PilakrzNozny(Pilkarz):
    def strelic(self):
        def gol():
            print("Nozny strzelil!!")
        return gol()

def wypisz(to):
    to.Strzelgola()
    to.strelic()

xdd = PilakrzNozny()
xd = PilakrzReczny()

wypisz(xdd)
wypisz(xd)