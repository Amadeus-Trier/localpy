from argparse import FileType
from curses import window
from os import close
from pydoc import safeimport
import tkinter as tk
from tkinter import Button, ttk
from tkinter import *
from tkinter import filedialog

root = tk.Tk()
root.title("Speisekarten Helper")
root.geometry("800x400")
root.minsize(width=200, height=200)
root.maxsize(width=00, height=600)


button1 =ttk.Button(root, text="CSV-Download")
button1.pack(side="left")

button2 =ttk.Button(root, text="EXCEL-Download")
button2.pack()

button3 =ttk.Button(root, text="PDF-Download")
button3.pack()


label1 = tk.Label(root, text="Eingabe deiner Speisekarte String", bg="#550000")
label1.pack(side="top", fill="both", expand="true")

label2 = tk.Label(root, text="Ausgabe deiner Speisekarte String", bg="#005500")
label2.pack(side="top", fill="both", expand="true")

label3 = tk.Label(root, text="Ausgabe deiner Speisekarte String", bg="#000055")
label3.pack(side="top", fill="both", expand="true")


root.mainloop()


#Eingabe = input(str("hier die Speisekarte: "))
#Ausgabe = Eingabe.replace("Oliven", "Oliven 2, 3, 4, 2,")
#print(Ausgabe)