class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def aseta_nopeus(self, nopeus):
        if nopeus <= self.huippunopeus:
            self.nopeus = nopeus
        else:
            self.nopeus = self.huippunopeus  #

    def aja(self, tunnit):
        self.matkamittari += self.nopeus * tunnit

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

if __name__ == "__main__":
    sahkoauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sahkoauto.aseta_nopeus(167)
    polttomoottoriauto.aseta_nopeus(145)

    sahkoauto.aja(3)
    polttomoottoriauto.aja(3)

    print(f"Sähköauton matkamittarilukema: {sahkoauto.matkamittari} km")
    print(f"Polttomoottoriauton matkamittarilukema: {polttomoottoriauto.matkamittari} km")
