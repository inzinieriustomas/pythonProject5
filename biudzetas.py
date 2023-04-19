# class Irasas:
#     def __init__(self, tipas, suma):
#         self.tipas = tipas
#         self.suma = suma
#
#     def __str__(self):
#         return f"{self.tipas}: {self.suma}"
#
#
# class Biudzetas:
#     def __init__(self):
#         self.zurnalas = []
#
#     def prideti_pajamu_irasa(self, suma):
#         pajamos = Irasas("Pajamos", suma)
#         self.zurnalas.append(pajamos)
#
#     def prideti_islaidu_irasa(self, suma):
#         islaidos = Irasas("Išlaidos", suma)
#         self.zurnalas.append(islaidos)
#
#     def gauti_balansą(self):
#         suma = 0
#         for irasas in self.zurnalas:
#             if irasas.tipas == "Pajamos":
#                 suma += irasas.suma
#             if irasas.tipas == "Išlaidos":
#                 suma -= irasas.suma
#         print(suma)
#
#     def parodyti_ataskaita(self):
#         for irasas in self.zurnalas:
#             print(f"{irasas.tipas}: {irasas.suma}")
#
#
# biudzetas = Biudzetas()
#
# while True:
#     pasirinkimas = int(input("1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - gauti balansą, \n4 - parodyti ataskaitą, \n9 - išeiti iš programos"))
#     if pasirinkimas == 1:
#         suma = float(input("Įveskite pajamų sumą: "))
#         biudzetas.prideti_pajamu_irasa(suma)
#     if pasirinkimas == 2:
#         suma = float(input("Įveskite išlaidų sumą: "))
#         biudzetas.prideti_islaidu_irasa(suma)
#     if pasirinkimas == 3:
#         biudzetas.gauti_balansą()
#     if pasirinkimas == 4:
#         biudzetas.parodyti_ataskaita()
#     if pasirinkimas == 9:
#         print("Viso gero")
#         break
#
#
















"""
import datetime
import calendar


class Sukaktis:
    def __init__(self, metai=1984, menuo=07, diena=06, valandos=10, minutes=10):
        self.metai = metai
        self.menuo = menuo
        self.diena = diena
        self.valandos = valandos
        self.minutes = minutes
        self.data = datetime.datetime(metai, menuo, diena, valandos, minutes)

    def smulkiai(self):
        now = datetime.datetime.now()
        skirtumas = now - self.data
        print(f"Praėjo metų: ", skirtumas.days // 365)
        print("Praėjo mėnesių: ", skirtumas.days / 365 * 12)
        print("Praėjo savaičių: ", skirtumas.days / 7)
        print("Praėjo dienų: ", skirtumas.days)
        print("Praėjo valandų: ", skirtumas.total_seconds() / 3600)
        print("Praėjo minučių: ", skirtumas.total_seconds() / 60)
        print("Praėjo sekundžių: ", skirtumas.total_seconds())

    def Keliamieji(self):
        if calendar.isleap(self.metai):
            print("Keliamieji metai")

    def atimtiDienas(self, dienos):
        return self.data - datetime.timedelta(days=dienos)

    def pridetiDienas(self, dienos):
        return self.data + datetime.timedelta(days=dienos)

    def __str__(self):
        return (
            f"Data: {self.metai}-{self.menuo}-{self.diena} {self.valandos}:{self.minutes}")


data1 = Sukaktis(2023, 1, 1, 12, 12)
data1.Keliamieji()
data1.smulkiai()
print(data1.atimtiDienas(10))
print(data1.pridetiDienas(31))
print(data1)


"""

"""1 užduotis: sukurti klasę Irasas, kuri turėtų savybę suma"""


class Irasas:
    def __init__(self, s):
        self.suma = s

    def parodyti_informacija(self):
        print(f"Irasas: {self.suma}")


"""2 užduotis: sukurti klasę PajamuIrasas, kuri turėtų savybes: siuntejas, papildoma_informacija"""


class PajamuIrasas(Irasas):
    def __init__(self, s, siuntejas, pap_informacija):
        super().__init__(s)
        self.siuntejas = siuntejas
        self.papildoma_informacija = pap_informacija

    def parodyti_informacija(self):
        print(f"Pajamos: +{self.suma}. ({self.siuntejas}; {self.papildoma_informacija})")


"""3 užduotis: sukurti klasę IslaiduIrasas, kuri turėtų savybes: atsiskaitymo_budas, isigyta_preke_paslauga"""


class IslaiduIrasas(Irasas):
    def __init__(self, s, atsiskaitymas, isigyta_preke):
        super().__init__(s)
        self.atsiskaitymo_budas = atsiskaitymas
        self.isigyta_preke_ar_paslauga = isigyta_preke

    def parodyti_informacija(self):
        print(f"Islaidos: -{self.suma}. ({self.atsiskaitymo_budas}; Isigyta {self.isigyta_preke_ar_paslauga})")


"""4 užduotis: sukurti klasę Biudzetas, kuri turėtų savybę: irasai"""


class Biudzetas:
    def __init__(self):
        self.irasai = []

    """
    5 užduotis: 
    prie klasės Biudzetas pridėti funkcija prideti_irasa(), kurio argumentas būtų Irasas
    metodas prie Biudzeto klasės savybės 'irasai' turi pridėti pateiktą įrašą
    """

    def prideti_irasa(self, irasas):
        self.irasai.append(irasas)

    """
    6 užduotis:
    Biudzetas klasei sukurti metodą gauti_balansa, kuris:
    pereitų per visus įrašus ir suskaičiuotų galutinį balansą.
    Su isinstance funkcija galime patikrinti, ar įrašas yra IslaiduIrasas, ar PajamuIrasas, 
    ir atitinkamai pridėti arba atimti iraso sumą
    """

    def gauti_balansa(self):
        galutine_suma = 0
        for irasas in self.irasai:
            if isinstance(irasas, PajamuIrasas) == True:
                galutine_suma += irasas.suma
            elif isinstance(irasas, IslaiduIrasas) == True:
                galutine_suma -= irasas.suma
        return galutine_suma

    """
    7 užduotis:
    Biudzetui sukurti funkciją, parodyti_ataskaita
    Funkcija pereina per kiekvieną įrašą ir iškviečia to įrašo funkciją gauti_informacija
    Tam reikės prie kiekvieno įrašo klasės pridėti funkciją gauti_informaciją, kuri
    su print išves to įrašo informaciją
    Pvz klasėje PajamuIrasas funkcija gauti_informacija išves suma, siunteja ir papildoma_informacija
    """

    def parodyti_ataskaita(self):
        for irasas in self.irasai:
            irasas.parodyti_informacija()


"""
8 užduotis:
    Sukurti vartotojo sąsają, kuri leistų dirbti su mūsų sukurtom klasėm

    Vartotojui pateikiami pasirinkimai:
    1. Pridėti pajamas
    2. Pridėti išlaidas
    3. Skaičiuoti balansą
    4. Parodyti ataskaitą
    0. Išeiti
"""
biudzetas = Biudzetas()
while True:
    print("1: Pridėti pajamas")
    print("2: Pridėti išlaidas")
    print("3: Skaičiuoti balansą")
    print("4: Parodyti ataskaitą")
    print("0: Išeiti")
    user_input = input("Jusu pasirinkimas: ")
    if user_input == "1":
        suma = float(input("Įveskite sumą: "))
        siuntejas = input("Įveskite siuntėją: ")
        pap_duom = input("Įveskite papildomus duomenis: ")
        irasas = PajamuIrasas(suma, siuntejas, pap_duom)
        biudzetas.prideti_irasa(irasas)
    elif user_input == "2":
        suma = float(input("Įveskite sumą: "))
        siuntejas = input("Įveskite atsiskaitymo būdą: ")
        pap_duom = input("Įveskite įsigytą prekę/paslaugą: ")
        irasas = IslaiduIrasas(suma, siuntejas, pap_duom)
        biudzetas.prideti_irasa(irasas)
    elif user_input == "3":
        print(biudzetas.gauti_balansa())
    elif user_input == "4":
        biudzetas.parodyti_ataskaita()
    else:
        break



bmghjgjgjg






















