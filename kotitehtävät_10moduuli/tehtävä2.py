class Hissi:
    def __init__(self, eka, vika, tamahetkinen):
        self.eka = eka
        self.vika = vika
        self.tamahetkinen = tamahetkinen
    def mene_ylos(self):
        self.tamahetkinen += 1
    def mene_alas(self):
        self.tamahetkinen -= 1
    def mene(self, kerros):
        if kerros > self.vika or kerros < self.eka:
            print(f"ei ole kerrosta {kerros}")
            return True
        else:
            while self.tamahetkinen != kerros:
                if self.tamahetkinen < kerros:
                    Hissi.mene_ylos(self)
                elif self.tamahetkinen:
                    Hissi.mene_alas(self)
            print(f"Hissi on siirtynyt kerrokseen: {self.tamahetkinen}")

class Talo:
    def __init__(self, ekakerros, vikakerros, hissit):
        self.ekakerros = ekakerros
        self.vikakerros = vikakerros
        self.hissit = hissit
        self.hissilista = []

        for i in range(1, hissit + 1):
            self.hissilista.append(Hissi(ekakerros, vikakerros, i))

    def Hissi_ajo(self, numeron, kerros):
        hissi = self.hissilista[numeron - 1]
        print(f"Hissi: {numeron} on nyt kerroksessa: {hissi.tamahetkinen}")
        kayta = hissi.mene(kerros)
        return kayta

Talo = Talo(0, 10, 3)
Talo.Hissi_ajo(1, 2)
Talo.Hissi_ajo(2, 5)
Talo.Hissi_ajo(3, 6)
Talo.Hissi_ajo(1, 10)