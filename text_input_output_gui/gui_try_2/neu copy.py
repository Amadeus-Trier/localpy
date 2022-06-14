import tkinter as tk
from importlib.resources import open_text
from tkinter import *
from tkinter import filedialog

from pkg_resources import safe_name





    
   # my_text.insert(END, stuff)
    #text1_file.close()
    

#def save_txt():
 #   fin =  open('sample2.txt', 'w+')
  #  fin.write(my_text.get(1.0, END))
    

#fin = Text(root, width=40, height=10)
#fin.pack(pady=20)

#fin = Button(root, text="Öffne deine Datei", command=open_txt)
#fin.pack(pady=20)

#save_button = Button(root, text="Lade deine Neue Datei runter")
#save_button.pack(pady=20)
#root = Tk()
#fin = open("/Users/program/eingabe.txt", "rt")
#fin = Button(root, text="Öffne deine Datei")
#fin.pack(pady=20)






#for line in fin:#


fin = open("C:/Users/program/eingabe.txt", "rt")
for line in fin:
    fout.write(line.replace("Oliven", ",Oliven 2, 3, 4, 2, 3wefwefwefwefwe")
    .replace("Soße", "Soße 6, 7, 4")
    .replace("Käse", "Käsese 7, 9, dsfsdfdsfdsfd3, b")
    .replace("Sahnesauce", "Sahnesauce a, b, c, d")
    .replace("Pide", "Pide a, 4, 5, 6")
    .replace("Mozzarella", "Mozzarella 7, 5, h, j")
    .replace("Weichkäse", "Weichkäse s, d, f, k, l")
    .replace("Schinken", "Schinken b, n, m, k, 9, 7")
    .replace("Ei", "Ei 7, 8, 2")
    .replace("Krabben", "Krabben 3, 7, 8, 2")
    .replace("Thunfisch", "Thunfisch ü, ä, l"))
    fin.close()
    fout = open("/Users/program/ausgabe.txt", "wt",)
    fout.close()

