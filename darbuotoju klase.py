
"""
import datetime

class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
    self.vardas = vardas
    self.valandos_ikainis = valandos_ikainis
    self.dirba_nuo = dirba_nuo

    def _nudirbo_dienas(self):
    dabar = datetime.date.today()
    pradzia = datetime.datetime.strptime(self.dirba_nuo, '%Y-%m-%d').date()
    dienu_sk = (dabar - pradzia).days
    return dienu_sk

    def paskaiciuoti_atlyginima(self):
    dienu_sk = self._nudirbo_dienas()
    atlyginimas = dienu_sk * 8 * self.valandos_ikainis
    return atlyginimas


class NormalusDarbuotojas(Darbuotojas):
    def _nudirbo_dienas(self):
    dabar = datetime.date.today()
    pradzia = datetime.datetime.strptime(self.dirba_nuo, '%Y-%m-%d').date()
    sav_dienos_sk = 5
    dienu_sk = ((dabar - pradzia).days // 7) * sav_dienos_sk
    dienu_sk += min((dabar - pradzia).days % 7, sav_dienos_sk)
    return dienu_sk


darbuotojas = Darbuotojas("Jonas", 10, "2023-01-01")
ndarbuotojas = NormalusDarbuotojas("Petras", 10, "2023-01-01")

atlyginimas1 = darbuotojas.paskaiciuoti_atlyginima()
atlyginimas2 = ndarbuotojas.paskaiciuoti_atlyginima()

print(f"{darbuotojas.vardas} atlyginimas: {atlyginimas1} euru")
print(f"{ndarbuotojas.vardas} atlyginimas: {atlyginimas2} euru")
"""
import datetime


class Darbuotojas:
    def __init__(self, vardas, ikainis, darbo_pradzia ):
        self.vardas = vardas
        self.valandinis_ikainis = ikainis
        self.dirba_nuo = darbo_pradzia


    def _darbo_dienu_skaicius(self):
        skirtumas = datetime.date.today() - self.dirba_nuo
        return skirtumas.days

    def paskaiciuoti_atlyginima(self):
        atlyginimas = self._darbo_dienu_skaicius() * self.valandinis_ikainis
        return atlyginimas

darbuotojas = Darbuotojas( "juozukas", 12 , datetime.date(2023, 4, 1))
darbuotojas1 = Darbuotojas( "juozukas", 12 , datetime.date(2023, 4, 1))
print( darbuotojas._darbo_dienu_skaicius())
print( darbuotojas1.paskaiciuoti_atlyginima())

