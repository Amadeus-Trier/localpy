from cgitb import text
from curses import wrapper
from readline import insert_text
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from distutils.fancy_getopt import wrap_text
import textwrap
from asyncore import read
from tokenize import PseudoExtras
from turtle import textinput

from setuptools import Command


root = Tk()
root.geometry("500x500")

def open_txt():
    text_file = filedialog.askopenfilename(initialdir="/Users/program/textedit/text.txt", title="Open Text File")
    text_file = open(text_file, 'r+')
    stuff = text_file.read()

    my_text.insert(END, stuff)
    text_file.close()

def save_txt():
    text_file = filedialog.askopenfilename(initialdir="C:/Users/program/ausgabes.txt", title="Speichern Text File")
    text_file.write(my_text.get(1.0, END))


def verwandeln():
    my_text_out = text
    my_text.insert(0, text)
    

my_text = Text(root, width=40, height=10)
my_text.pack(pady=20)

konvert_button = Button(root, text="konvertieren", command=verwandeln)
konvert_button.pack(pady=29)
    

my_text_out = Text(root,  width=60, height=5)
my_text_out.pack(pady=10)

Button1 = Button(root, text="Öffne deine Datei", command=open_txt)
Button1.pack(pady=20)

save_button = Button(root, text="Download", command=save_txt)
save_button.pack(pady=20)




#Ergänzung = textwrap.fill("Käse"),("1,3,5")


root.mainloop()