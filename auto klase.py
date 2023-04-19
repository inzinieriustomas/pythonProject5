



class Automobilis:

    def __init__(self, metai, modelis, degalai):
        self.metai = metai
        self.modelis = modelis
        self.degalai = degalai
        print("sukurtas automobilis: {self.metai} {self.modelis} {self.kuro_tipas")

    def vaziuoti(self):
        print("Vaziuoju")

    def stoveti(self):
        print("Stoviu")

    def pildyti_degalus(self):
        print("ipilti degalai: { self.kuro_tipas}" )

class Elektromobilis (Automobilis):
    def __init__(self, metai, modelis):
        super().__init__(metai, modelis, "Elektra")

    def pildyti_degalus ( self):
        print( "Baterija ikrauta")

    def vaziuoti_autonomiskai(self):
        print("vaziuoju pats")



mano_masina = Automobilis (2009, "Volvo", "Dujos")
mano_masina.vaziuoti()
mano_masina.stoveti()
mano_masina.pildyti_degalus()
print( mano_masina.modelis )

elektro_masina = Elektromobilis(2018, "tesla")
elektro_masina.vaziuoti()
elektro_masina.stoveti()
elektro_masina.pildyti_degalus()





# class Automobilis:
# def __init__(self, metai, modelis, kuro_tipas):
# print(f"\nSukuriame automobili pagal \n Metus: {metai} \n Modeli: {modelis} \n Kuro tipa: {kuro_tipas}")
# self.metai = metai
# self.modelis = modelis
# self.kuro_tipas = kuro_tipas
#
# def vaziuoti(self):
# print(f"Vaziuoja {self.modelis}")
#
# def stoveti(self):
# print(f"Priparkuota: {self.modelis}")
#
# def pildyti_degalu(self):
# print(f"Degalai įpilti: {self.kuro_tipas}")
#
# class Elektromobilis(Automobilis):
# def pildyti_degalu(self):
# print("Baterija ikrauta") #taip parasius galima pakoreguoti isaukus sia klasse ir ji pakeis klases automobilis
# # funkcija pildyti degalus i Baterija pakrauta, tiesiog koregacija funkcijos
# def vaziuoti_automatiskai(self):
# print("Vaziuoja autonomiskai")


# Opelis = Automobilis(2005, "Opelis", "Dyzelis")
# Opelis.vaziuoti()
# Opelis.stoveti()
# Opelis.pildyti_degalu()


class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        print(f'Automobilio metai: {metai}, modelis: {modelis}, kuro tipas: {kuro_tipas}')
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
    def vaziuoti(self):
        print('Vaziuoja')
    def stoveti(self):
        print('Priparkuota')
    def pildyti_degalu(self):
        print('Degalai ipilti')
class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print('Baterija ikrauta')
    def vaziuoti_autonomiskai(self):
        print('Vaziuoja autonomiskai')

auto1 = Automobilis(2002, 'BMW', 'benzinas')
auto2 = Elektromobilis(2022, 'Jaguar', 'elektra')

auto1.vaziuoti()
auto1.stoveti()
auto1.pildyti_degalu()
auto2.vaziuoti()
auto2.stoveti()
auto2.pildyti_degalu()
auto2.vaziuoti_autonomiskai()











"""
Turėtų klasę Automobilis
        Automobilis
        turėtų
        savybes: metai, modelis, kuro_tipas

        Automobilis
        turėtų
        metodus: vaziuoti, stoveti, pildyti_degalu, kurie
        atitinkamai
        atspausdintų „Važiuoja“, „Priparkuota“, „Degalai
        įpilti“

        Sukūrus
        objektą, automatiškai
        atspausdintų
        automobilio
        metus, modelį
        ir
        kuro
        tipą

        Turėtų
        klasę
        Elektromobilis(jo
        tėvinis
        objektas – Automobilis)

        Elektromobilis
        pakeistų
        Automobilio
        metodą
        pildyti_degalu
        taip, kad
        jis
        atspausdintų „Baterija
        įkrauta“

        Elektromobilis
        turėtų
        metodą
        vaziuoti_autonomiskai, kuris
        spausdintų „Važiuoja
        autonomiškai“

        Sukurti
        norimą
        Automobilio
        objektą

        Sukurti
        norimą
        Elektromobilio
        objektą

        Su
        sukurtu
        Automobilio
        objektu
        paleisti
        funkcijas
        vaziuoti, stoveti, pildyti_degalu

        Su
        sukurtu
        Elektromobilio
        objektu
        paleisti
        funkcijas
        vaziuoti, stoveti, pildyti_degalu, vaziuoti_autonomiskai
"""