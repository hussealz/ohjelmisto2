class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka
        print("Uusi auto luotu")

    def info(self):
        print(f"Rekisterinumero: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} KM/H")
        print(f"Hetkellinen nopeus: {self.nopeus} KM/H")
        print(f"Kuljettu matka: {self.kuljettu_matka} M")

# Pääohjelma
auto1 = Auto("ABC-123", 142)
auto1.info()
