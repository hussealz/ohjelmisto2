class Hissi:
    def __init__(self, nimi, ylin, alin, tila = 1):
        self.nimi = nimi
        self.ylin = ylin
        self.alin = alin
        self.tila  = tila

    def kerros_ylos(self):
        self.tila  = self.tila  + 1

    def kerros_alas(self):
        self.tila  = self.tila  - 1

    def siirry_kerrokseen(self, kerros):
        if kerros > self.ylin:
            print(f"{kerros} ei ole olemassa")
            exit()
        if kerros < self.alin:
            print(f"{kerros} ei ole olemassa")
            exit()
        while hissi1.tila  < kerros:
            hissi1.kerros_ylos()
            print(f"{hissi1.nimi} \nSijainti: {hissi1.tila }-kerros")
        while hissi1.tila > kerros:
            hissi1.kerros_alas()
            print(f"{hissi1.nimi} \nSijainti: {hissi1.tila }-kerros")



hissi1 = Hissi("Hissi1", 5, 1)
print(f"{hissi1.nimi} \nSijainti: {hissi1.tila }-kerros")
hissi1.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(-1)

hissi1.siirry_kerrokseen(hissi1.alin)