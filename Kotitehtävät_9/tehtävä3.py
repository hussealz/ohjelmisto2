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
        print(f"Kuljettu matka: {self.kuljettu_matka} KM")

    def kiihdyta(self, muutos):
        uusi_nopeus = self.nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus
        print(f"Auton uusi nopeus on {self.nopeus} KM/H")

    def kulje(self, tunnit):
        edetty_matka = self.nopeus * tunnit
        self.kuljettu_matka += edetty_matka
        print(f"Auto kulki {edetty_matka} KM lisää, kuljettu matka on nyt {self.kuljettu_matka} KM")


# Pääohjelma
auto1 = Auto("ABC-123", 142)

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f"Auton nykyinen nopeus: {auto1.nopeus} KM/H")

auto1.kiihdyta(-200)
print(f"Auton uusi nopeus hätäjarrutuksen jälkeen: {auto1.nopeus} KM/H")

auto1.nopeus = 60
auto1.kuljettu_matka = 2000
auto1.kulje(1.5)
