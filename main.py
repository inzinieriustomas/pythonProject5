

#
#
# with open(" failas.png", "wb") as failas:
#     failas.write()


# import os

# zmogaus_ivestis =(input("iveskite programos pavadinima "))
#
# a = 9
# b = 0
# print (a/b)

# try:
#
#     with open (zmogaus_ivestis, "r") as failas:
#          print( failas.read())
#
# except ZeroDivisionError:
#     print("bandema dalinti is nulio")
# except:
#     print("Tokio failo nera")
# finally:
#     print("po failo atidarymo")
# print ("progrma dirba toliau")

# def gauk_vartotojo_skaiciu():
#     while True:
#      try:
#          skaicius = int(input( "iveskite skaiciu: "))
#          return skaicius
#      except ValueError:
#          print( "iveskite skaiciu")


#
# import pickle
#
#
#
# zaidejo_taskai = 97
# with open ( "failas.txt", "w") as failas:
#     failas.write(str(24))
#
# with open("failas.txt", "r") as failas:
#     duom = int(failas.read())

# Parašyti
# programą, kuri
# iš failo ištrauktų skaičių sąrašą (supickle),
#
# vartotojo paprašytų skaičiaus ir jį įterptų į sąrašą
# atspausdintų sąrašo skaičių sumą sąrašą įrašytų
# atgal į failą(su pickle)

# skaiciukai = []
# try:
#     with open("duom.txt", "r") as duom_failas:
#         duomenys = pickle.load(duom_failas)
# except FileNotFoundError:
#     print( "failas dar nesukurtas :(")
#
# duomenys.append
#
# #nuskaitymas
#
# with open("duom.txt", "wb") as duom_failas:
#     pickle.dump(duomenys,)

# Skaitymo algoritmas:
# Sukuriamas tuščias skaičių sąrašas numbers
# Pereinam per kiekvieną failo eilutę, ją pasiverčiame į int, ir pridedame į mūsų sąrašą
# Žmogus įveda skaičių, skaičius pridedamas prie skaičių listo
# Rašymo algoritmas:
# Pereinam per mūsų listą (sąrašą)
# su file.write() įrašome mūsų skaičių į failą
# Nepamirškite, kad norint kad skaičius būtų parašytas iš naujos eilutės faile, reikia pridėti "\n" (naujos eilutės simbolį)
#
# Nuskaityti kiekvieną failo eilutę:
# for eilutė in file:
# # kodas
#
# kur file - mūsų failas, atidarytas su open() funkcija
# pridėti skaičių prie sąrašo (list)
# numbers = []
# numbers.append( skaicius )


# import os
#
# skaiciukai = []
#
# with open("skaiciukai.txt", "r+") as failas:
#     for eilute in failas:
#         skaicius = int(eilute)




# with open ("duom.txt", "r") as failas:
#     for eilute in failas:
#         print(failas)
#         skaiciukai=[]
#         while True:
#             minibiudzetas=int(input("Iveskite pajamas arba išlaidas (su '-' ženklu):"))
#             if not minibiudzetas:
#                 break    skaiciukai.append(minibiudzetas)
#                 print(skaiciukai)
#                 balansas=sum(skaiciukai)
#                 print(balansas)



#
# numbers = []
# with open( "failas.txt", "r") as duomenu_failas:
#     for eilute in duomenu_failas:
#         skaicius = int( eilute)
#         numbers.append(skaicius)
# print(numbers)
#
#
# zmogaus_skaicius = int(input( "iveskite skaiciu: "))
# numbers.append(zmogaus_skaicius)
#
# print(numbers)
# with open("failas.txt", "w") as duomenu_failas:
#     for sk in numbers:
#         duomenu_failas.write(str(sk))
#         duomenu_failas.write("\n")



#
# from tkinter import Tk, Label, Frame, Button,BOTTOM, LEFT, Y, RIGHT
#
# langas = Tk()
#
# def spausdinti():
#     uzrasas["text"] = "aha"
#
# langas.geometry("800x800")
# langas.grid()
# uzrasas = Label(langas, text = "labas vakaras")
# uzrasas.pack()
# virsutinis = Frame(langas)
# apatinis = Frame(langas)
#
# mygtukas1 = Button(virsutinis, text = "spausdinti", height = 5,width=8, command=spausdinti )
# mygtukas2 = Button(virsutinis, text = "2 mygtukas", bg='yellow', fg="black")
# mygtukas3 = Button(apatinis, text = "3 mygtukas", bg = 'red', fg="black")
# mygtukas4 = Button(apatinis, text = "4 mygtukas",bg = 'red', activebackground="green")
# virsutinis.pack()
#
# apatinis.pack(side=BOTTOM)
# mygtukas1.pack(side=LEFT)
# mygtukas2.pack(side=LEFT)
# mygtukas3.pack(side=RIGHT)
# mygtukas4.pack(side=BOTTOM, fill=Y)
#
# rezultato_langelis = Label(langas, text = "")
#
# langas.mainloop()
#


# a = ( 1,2,3, "labas")
#
# ilgis = len(a)
#
# print(ilgis)
#
# aibe = {5,8,7,9,}
#
# aibe.add(10)
#
# aibe.add(9)
#
# print(aibe)

# if 3 in aibe:
#     print("yra")
#
# sarasas = {1,2,1,2,1,3,4,4,4,}
#
# aibe2 = set(sarasas)
#
# print(aibe2)
# if 1 in sarasas:
#     print("yra")
# if 1 in aibe2:
#     print("yra")
#
# print(aibe | aibe2)
#
# print(aibe.union(aibe2))
# print(aibe & aibe2)
#
# print(aibe - aibe2)





#
# from PIL import Image
#
# im = Image.open("DSC01127.jpg")
# im.show()
#
# im2 = Image.open("DSC01141.jpg")
# im2.show()
#
# atvirute = im
# atvirute.save("DSC01127.jpg")
#
# print(im.format, im.size, im.mode)
# print(im2.format, im2.size, im2.mode)
# size = 3547, 2988
#
# im.thumbnail(size)
# # im.show()
#
# box = (300,300,600,600)
# dalis = im.crop(box)
# # dalis.show()
#
# apversta = im2.transpose(Image.FLIP_TOP_BOTTOM)
# # apversta.show()
#
#
# istempta = im2.resize((300,100))
# # istempta.show()
#
# im2.thumbnail((1500,1500))
#
# im2_location = ( 0,100, im.size[0], im.size[1]+100)
#
# im2.paste(im,im2_location)
#
# im2.show()
#

#
#
# import datetime
# import calendar
#
#
# class Sukaktis:
#     def __init__(self, metai = 1984, menuo = 07, diena = 06, valandos = 10, minutes = 10):
#         self.metai = metai
#         self.menuo = menuo
#         self.diena = diena
#         self.valandos = valandos
#         self.minutes = minutes
#         self.data = datetime.datetime(metai, menuo, diena, valandos, minutes)
#
#     def smulkiai(self):
#         now = datetime.datetime.now()
#         skirtumas = now - self.data
#         print(f"Praėjo metų: ", skirtumas.days // 365)
#         print("Praėjo mėnesių: ", skirtumas.days / 365 * 12)
#         print("Praėjo savaičių: ", skirtumas.days / 7)
#         print("Praėjo dienų: ", skirtumas.days)
#         print("Praėjo valandų: ", skirtumas.total_seconds() / 3600)
#         print("Praėjo minučių: ", skirtumas.total_seconds() / 60)
#         print("Praėjo sekundžių: ", skirtumas.total_seconds())
#
#     def keliamieji(self):
#         if calendar.isleap(self.metai):
#             print("keliamieji metai")
#
#     def atimti_dienas(self, dienos):
#         return self.data - datetime.timedelta(days = dienos)
#
#     def prideti_dienas(self, dienos):
#         return self.data + datetime.timedelta(days = dienos)
#
#     def __str__(self):
#         return (
#             f"Data: {self.metai}-{self.menuo}-{self.diena} {self.valandos}:{self.minutes}")
#
#
# data1 = Sukaktis(2023, 01, 01, 13, 13)
# data1.keliamieji()
# data1.smulkiai()
# print(data1.atimti_dienas(10))
# print(data1.prideti_dienas(31))
# print(data1)
#
#



zalgiris = 'zalgiris'
euroleague = ['zalgiris']
while zalgiris in euroleague:
    print("Play")
