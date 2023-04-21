
















class Tank:
    def __init__(self, tinklas):
        self.tinklas = tinklas
        self.x = 0
        self.y = 0

    def pirmyn(self, x,y):
        self.pirmyn(x,y)

    def atgal(self):
        self.atgal(x,y)
        self.tankas_location = self.tank_location
    def kairen(self):
        self.kairen(x,y)

    def desinen(self):
        self.desinen(x,y)
    def shoot(self):
        self.shoot(x,y)

        def pasisukti(self, laipsniai):
            """
            :param laipsniai: gali būti 90, 180 arba 270 laipsnių
            """
            self.kryptis = (self.kryptis + laipsniai) % 360

            if laipsniai == 90:
                self.auto = self.auto.transpose
            if laipsniai == 180:
                self.auto = self.auto.transpose
            if laipsniai == 270:
                self.auto = self.auto.transpose
            self.auto_location = self.auto_location = (
            self.x, self.y, self.x + self.auto.size[0], self.y + self.auto.size[1])


tank = tankas