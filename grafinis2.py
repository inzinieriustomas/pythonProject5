

#
# from tkinter import Tk, Label, Frame, Button,BOTTOM, LEFT, Y, RIGHT,Entry
#
# langas = Tk()
#
# def spausdinti():
#     ivestas_tekstas = laukelis1.get()
#     uzrasas["text"] = ivestas_tekstas
#
# langas.geometry("800x800")
# uzrasas = Label(langas, text = "labas vakaras")
# uzrasas.pack()
# mygtukas1 = Button(langas, text = "spausdinti", height = 5,width=8, command=spausdinti )
# laukelis1 = Entry(langas)
#
# laukelis1.pack()
# mygtukas1.pack(side=LEFT)
#
#
#
#
#
#
# langas.mainloop()





# from tkinter import Tk, Label, Frame, Button,BOTTOM, LEFT, Y, RIGHT,Entry,Listbox,END
#
# langas = Tk()
# langas.title( "puslapis nerastas 404")
# def spausdinti():
#     ivestas_tekstas = laukelis1.get()
#     uzrasas["text"] = ivestas_tekstas
#
# langas.geometry("800x800")
# uzrasas = Label(langas, text = "labas vakaras")
#
# boksas = Listbox(langas)
# sarasas = range(1, 200)
# boksas.insert(END,*sarasas)
# boksas.pack(side=LEFT)
#
#
# mygtukas1 = Button(langas, text = "spausdinti", height = 5,width=8, command=spausdinti )
# laukelis1 = Entry(langas)
#
# uzrasas.grid(row=0, columnspan=2)
# laukelis1.grid(row=1, column=1)
# mygtukas1.grid(row=2, column=1)

#
#
#
#
#
# langas.mainloop()

#                             #meniu
# from tkinter import *
# langas = Tk()
#
# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)
#
# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
# submeniu.add_command(label="Antras")
# langas.mainloop()
#



# #su slankiojancia juosta
# from tkinter import *
#
# langas = Tk()
# sarasas = range(1, 200)
# Scrolas = Scrollbar(langas)
#
# boksas = Listbox(langas)
# Scrolas.config(command=boksas.yview)
# boksas.insert(END,*sarasas)
# Scrolas.pack(side=RIGHT, fill=Y)
# boksas.pack(side=LEFT)
# langas.mainloop()


#
# from tkinter import *
# langas = Tk()
# langas.geometry("800x800")
# langas.title( "RESTORANAS")
# langas.title( "puslapis nerastas 404")
# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 10)
#
# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
# submeniu.add_command(label="Antras")
# langas.mainloop()

# #meniu su submeniu ir submeniu
# from tkinter import *
# langas = Tk()
# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)
# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
# submeniu.add_command(label="Antras")
# submeniu_pirmo = Menu(submeniu, tearoff = 0)
# submeniu.add_cascade(label="Trecias", menu=submeniu_pirmo)
# submeniu_pirmo.add_command(label="Ketvirtas")
# langas.mainloop()


# from tkinter import *
# from PIL import ImageTk, Image
#
# root = Tk()
# img = ImageTk.PhotoImage(Image.open("paveiksliukas.JPG"))
# panel = Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")
# root.mainloop()


# from tkinter import *
# import webbrowser
#
# def callback(url):
#     webbrowser.open_new(url)
#
# langas = Tk()
# langas.geometry("800x800")
# langas.title("puslapis nerastas 404")
# langas.title()
#
# teksto_dydis = Label(langas, text="Puslapiai", font=("Helvetica", 56))
# teksto_dydis.pack()
#
# nuoroda = Label(langas, text="Google", fg="red", cursor="hand1")
# nuoroda.pack()
# nuoroda.bind("<Button-1>", lambda e: callback("http://www.google.com"))
#
# nuoroda2 = Label(langas, text="delfi", fg="blue", cursor="hand1")
# nuoroda2.pack()
# nuoroda2.bind("<Button-1>", lambda e: callback("http://www.delfi.lt"))
#
# nuoroda3 = Label(langas, text="technologijos", fg="green", cursor="hand2")
# nuoroda3.pack()
# nuoroda3.bind("<Button-1>", lambda e: callback("http://www.technologijos.lt"))
#
# langas.mainloop()

#
# from tkinter import *
# from PIL import ImageTk, Image
#
# langas = Tk()
# langas.geometry("800x800")
# langas.title("puslapis nerastas")
# def rodomas_pav():
#     foto1 = ImageTk.PhotoImage(Image.open("foto1.JPG"))
#     remas["image"] = foto1
#
# panel = Label(langas, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")
# langas.mainloop()


# from tkinter import *
#
# langas = Tk()
# langas.geometry ("800x800")
# uzrasas1 = Label(langas, text="Vardas")
# laukas1 = Entry(langas)
# uzrasas2 = Label(langas, text="Pavardė")
# laukas2 = Entry(langas)
# varnele = Checkbutton(langas, text="Pažymėk varnelę")
#
# uzrasas1.grid(row=1, column=0, sticky=E)
# laukas1.grid(row=2, column=1)
# uzrasas2.grid(row=3, column=0, sticky=E)
# laukas2.grid(row=4, column=1)
# varnele.grid(row=5, columnspan=2)
#
# langas.mainloop()
#

