



from time import sleep

from PIL import Image



class Automobilis:

    def __init__(self):
        self.zemelapis = Image.open("map1.jpg")
        self.auto = Image.open("car1.jpg")
        self.paveiksliukas = copy(self.zemelapio_failas)
        self
        self.auto.thumbnail((40, 40))
        self.auto = self.auto.transpose(Image.ROTATE_270)
        self.auto_location = (0, 0, self.auto.size[0], self.auto.size[1])
        self.kryptis = 0
        self.x = 0
        self.y = 0

    def pasisukti(self, laipsniai):
        """
        :param laipsniai: gali būti 90, 180 arba 270 laipsnių
        """
        self.kryptis = (self.kryptis + laipsniai) % 360

        if laipsniai == 90:
            self.auto = self.auto.transpose(Image.ROTATE_90)
        if laipsniai == 180:
            self.auto = self.auto.transpose(Image.ROTATE_180)
        if laipsniai == 270:
            self.auto = self.auto.transpose(Image.ROTATE_270)
        self.auto_location = self.auto_location = (self.x, self.y, self.x + self.auto.size[0], self.y + self.auto.size[1])

    def kaire(self):
        self.pasisukti(90)

    def desine(self):
        self.pasisukti(270)

    def pavaziuoti(self, km):
        if self.kryptis == 0:
            self.y = self.y - km
        elif self.kryptis == 90:
            self.x = self.x - km
        elif self.kryptis == 270:
            self.x = self.x + km
        elif self.kryptis == 180:
            self.y = self.y + km

        self.auto_location = (self.x, self.y, self.x + self.auto.size[0], self.y + self.auto.size[1])

    def parodyti(self):
        print(self.auto_location)
        self.zemelapis.paste(self.auto, self.auto_location)
        self.zemelapis.show()

masina = Automobilis()

masina.desine()
print(masina.kryptis)
print(masina.auto_location)

masina.parodyti()

sleep(1)

masina.pavaziuoti(200)
print(masina.kryptis)
print(masina.auto_location)

masina.parodyti()

sleep(1)

masina.desine()

print(masina.kryptis)
print(masina.auto_location)

masina.parodyti()

sleep(1)

masina.pavaziuoti(60)


masina.parodyti()

sleep(1)
print(masina.kryptis)
print(masina.auto_location)

masina.kaire()

masina.parodyti()

sleep(1)

masina.pavaziuoti(200)

masina.parodyti()

sleep(1)

masina.parodyti()

