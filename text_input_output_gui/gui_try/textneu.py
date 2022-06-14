from itertools import tee
from tkinter import *
root=Tk()
root.geometry("400x200")


def knopffunktion():
    text="das ist ein text"
    eingabe1.insert(0, text)
    return None

eingabe1 = Entry(root,width=20)
eingabe1.pack()


Button(root, text="knopf", command=knopffunktion).pack()







root.mainloop()