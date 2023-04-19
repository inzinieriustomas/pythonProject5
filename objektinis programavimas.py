





#
# import datetime
#
# class User():
#     def __init__(self, email, name, password):
#         self.email = "email"
#         self.password = ""
#         self.name = ""
#         self.birth_date = datetime.datetime.now()
#
#     def check_password(self, slaptazodis):
#         if slaptazodis == self.password:
#             print("teisingas slaptazodis")
#         else:
#             print("neteisingas slaptazodis:(")
#
#     def __str__(self):
#         return f"User: {self.name}, {self.email}"
# vart1 = User("test@test.com", "Jonas", "slaptazodis")
# vart2 = User("test2@test2.com", "T", "testslaptazodis")
#
# vart1.check_password("slaptazodis")
# vart2.check_password("slaptazodis")
#

# class Student():
#     def __init__(self):
#         self.vardas = "vardas"
#         self.pavarde = "pavarde"
#
#     def sakyk_labas (self):
#         print(f"labas, as esu {self.vardas} {self.pavarde}")
#
#
# studentas = Student()
#
# stud2 = Student()
# stud2.vardas = "Petras"
#
# studentas.sakyk_labas()
# stud2.sakyk_labas()
# print(studentas.vardas)
# print(stud2.vardas)
#




class Sakinys():
    def __init__(self, mano_tekstas):
        self.tekstas = mano_tekstas


    def atbulai(self):
        return self.tekstas[::-1]
    def didziosiomis(self):
        return self.tekstas.upper()

    def mazosiomis(self):
        return self.tekstas.lower()

    def grazinti(self, zodzio_numeris):
        isdalintas = self.tekstas.split()
        return isdalintas [zodzio_numeris]

    def ieskok_simboliu(self, simboliai):
        return self.tekstas.count(simboliai)

    def sukeisti(self, simboliai,a):
        return self.tekstas.replace(simboliai,a)
    def statistika(self):
        raides = 0
        skaiciu = 0
        mazosios = 0
        didiziosios = 0
        for simbolis in self.tekstas:
            if simbolis.isalpha():
                raides +=1
            elif simbolis.isnumeric():
                skaiciu += 1
            if simbolis.islower():
                mazosios +=1
            elif simbolis.isupper():
                didiziosios += 1
        print(f"raidziu: {raides}, skaiciai: {skaiciu}, mazosios:{mazosios}, didziosios: {didiziosios}")

mano_sakinys = Sakinys("dar kitoks sakinys")
antras = Sakinys ( "kitas tekstas")

print(mano_sakinys.atbulai())
print(antras.atbulai())
print(antras.didziosiomis())
print(antras.mazosiomis())
print(antras.grazinti(1))
print(antras.ieskok_simboliu("a"))
print(antras.sukeisti("a", "c"))

class Sakinys():
    def __init__(self)
    def atspausdina(self):
        return self.tekstas[::-1]



