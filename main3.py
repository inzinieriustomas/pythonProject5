
import datetime


class Sukaktis:

    def __init__(self,data):
        self.data = datetime.datetime.strptime(data, "%Y-%m-%d")
        print(self.data)
    def ar_keliamieji(self):
        if self.data.year % 4==0:
          return True
        return False


    def atimti_dienas(self, dienos):

        nauja_data = "kazkas"

        return nauja_data
    def kiek_praejo(self, laiko_vienetai):

        return

gimtadienis = Sukaktis("1980-12-15")

vestuves = Sukaktis('2000-01-20')
if gimtadienis.ar_keliamieji():
    print("gimtadienis buvo keliamaisiais metais")
else:
    print("gimtadienis buvo ne keliamaisiais metais")

gimtadienis.ar_keliamieji()

vestuves.ar_keliamieji()