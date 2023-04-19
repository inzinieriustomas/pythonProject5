

class Payment:

    def __init__(self, p1, p2):
        print(f"sukuriame {p1} {p2}")
        self.moketojo_vardas = p1
        self.suma = p2

    def atlik_mokejima (self):
        print(f"Vartotojas {self.moketojo_vardas} atliko {self.suma} euru mokejima")


class CardPayment ( Payment ):
    def __init__(self, p1, p2, p3):
        print("Kuriame korteles mokejima")
        super().__init__( p1,p2 )
        self.korteles_numeris = p3


    def atlik_mokejima(self):
        print( f"Vartotojas {self.moketojo_vardas} atliko {self.suma} mokejima kortele nr {self.korteles_numeris}")


    def tikrink_kortele(self):
        return len(self.korteles_numeris) == 16





class CreditCardPayment (CardPayment):
    def __init (self, p1,p2,p3):
        super().__init__(p1,p2,p3)

mokejimai = [
    Payment ( "Petriukas", 980),
    CardPayment ("Juozukas", 1000, "574237357357375"),
    Payment ( "Onute", 88888),
    Payment ( "TTTTT", 5555 ),
    CreditCardPayment ( "T", 740, "1951951591951951")

]

for mok in mokejimai:
    mok.atlik_mokejima()





kortele = CardPayment ( "Petriukas", 800, "4565465465757456454" )
kreditine = CreditCardPayment ("styvas", 988, "89789798789798789789")
kreditine.tikrink_vartotojo_varda

kortele.atlik_mokejima()
ar_kortele_teisinga = kortele.tikrink_kortele()

if kortele.tikrink_kortele() == True:
    print( "kortele teisinga")
else:
    print ("ivestas blogas korteles numeris")


mokejimas = Payment ("Jonukas", 900)
mokejimas2 = Payment ("Tomukas", 550)

kortele.tikrink_vartotojo_varda()


















