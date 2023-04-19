
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




from tkinter import Tk, Label, Button
from random import randint

kartai = 0

def move_button(event):
global kartai
kartai += 1
x = randint(0, langas.winfo_width() - mygtukas2.winfo_width())
y = randint(0, langas.winfo_height() - mygtukas2.winfo_height())
mygtukas2.place(x=x, y=y)
if kartai == 10:
langas.geometry("500x400")
if kartai == 15:
langas.geometry("1000x500")

langas = Tk()
langas.geometry("250x200")

# for x in range(16):
# for y in range(16):
# langelis = Label(langas)
# langelis["text"] = "X"
# langelis.grid(row=y, column=x)


uzrasas = Label(langas, text="Ar tu mane myli?")
uzrasas.grid(row=0, column=6, columnspan=4)

mygtukas1 = Button(langas, text="Taip")
mygtukas1.grid(row=2, column=6)

mygtukas2 = Button(text="Ne")
mygtukas2.bind("<Enter>", move_button)
mygtukas2.grid(row=2, column=8)


langas.mainloop()