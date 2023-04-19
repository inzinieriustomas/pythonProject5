

#
# class Automobilis:
#
#     def __init__(self, maks_greitis=200):
#         self.greitis=0
#         self.maksimalus_greitis = maks_greitis
#     def greiteti(self):
#         self.greitis = self.greitis + 1
#
#     def vaziuoti(self):
#         self.greitis = 20
#
#     def ilgai_pypseti(self):
#         for i in range(5):
#             self.pypseti()
#
#
#     def pypseti():
#         print("pyyyp")
#
#
# mano_auto = Automobilis()
#
# mano_auto.pypseti()
# mano_auto.pypseti()
#
# auto = Automobilis()
#
# auto1 = Automobilis()
# auto1.ilgai_pypseti()
#
# auto1.greiteti()
#
# for i in range(30):
#     mano_masina.greiteti()
# print(mano_masina.greitis)
#



# class Sandelis:
#
#     def __init__(self):
#         self.daiktai = []
#         self.adresas = ""
#         self.duru_aukstis = 0
#         self.atidarytas = False
#
#     def atidaryti(self):
#         self.atidarytas = True
#
#     def uzdaryti(self):
#         self.atidaytas = False





from PIL import Image


class Automobilis:

    def __init__(self):
        self.zemelapis = Image.open("map.jpg")
        self.auto = Image.open("car.jpg")
        self.auto.thumbnail((20,20))
        self.auto.transpose(Image.ROTATE_90)
        self.auto_location = (0,0,self.auto.size[0],self.auto.size[1])
        self.auto.paste(self.auto, self.auto_location)
        self.kryptis = 0

            if self.kryptis == 90
                self.auto = self.auto.transpose(Image.ROTATE_90)
            if self.kryptis == 90
                self.auto = self.auto.transpose(Image.ROTATE_180)
            if self.kryptis == 270
                self.auto = self.auto.transpose(Image.ROTATE_270)
            self.auto_location = (0,0, self.auto.size[0], self.auto.size[1])
    def pavaziuoti (self, km):
        if self.kryptis == 0
            self.y = self.y - km
        elif self.kryptis == 90
            self.x = self.x - km
        elif self.kryptis == 270
            self.x = self.x + km
        elif self.kryptis == 180
            self.y = self.y + km


    def pasisukti(self, laipsniai):

        # :param laipsniai: gali buti 90, 180 arba 270 laipsniu
        self.kryptis = (self.kryptis + laipsniai) % 360



    def parodyti(self):
        print(self.auto_location)
        self.zemelapis.paste(self.auto, self.auto_location)
        self.zemelapis.show()

masina = Automobilis()
masina.pasisukti(270)
masina.pavaziuoti(200)
masina.pasisukti(270)
masina.pavaziuoti(60)
masina.parodyti()













