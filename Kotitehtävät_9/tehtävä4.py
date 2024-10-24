import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def info(self):
        return f"{self.rekisteritunnus} | Huippunopeus: {self.huippunopeus} KM/H | Nopeus: {self.nopeus} KM/H | Kuljettu matka: {self.kuljettu_matka} KM"

    def kiihdyta(self, muutos):
        uusi_nopeus = self.nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tunnit):
        edetty_matka = self.nopeus * tunnit
        self.kuljettu_matka += edetty_matka

autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu_kaynnissa = True

while kilpailu_kaynnissa:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False
            break

print(f"{'Rekisteritunnus':<12} | {'Huippunopeus':<14} | {'Nopeus':<8} | {'Kuljettu matka'}")
print("-" * 50)
for auto in autot:
    print(f"{auto.rekisteritunnus:<12} | {auto.huippunopeus:<14} KM/H | {auto.nopeus:<8} KM/H | {auto.kuljettu_matka:.2f} KM")
