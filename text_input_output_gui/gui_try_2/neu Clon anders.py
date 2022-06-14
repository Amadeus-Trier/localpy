import tkinter as tk
from importlib.resources import open_text
from tkinter import *
from tkinter import filedialog

from pkg_resources import safe_name

root = Tk()
root.geometry("500x500")

def open_txt():
    text_file = filedialog.askopenfilename(initialdir="C:/Users/program/eingabe.txt", title="Open Text File")
    text_file = open(text_file, 'r+')
    stuff = text_file.read()
    
    my_text.insert(stuff, 'w+')
    transform="text_file"
    print="trans"
    



def save_txt():
    text_file = filedialog.askopenfilename(initialdir="C:/Users/program/ausgabes.txt", title="Open Text File")
    text_file.write(my_text.get(1.0, END))
    

my_text = Text(root, width=40, height=10)
my_text.pack(pady=20)

open_button = Button(root, text="Öffne deine Datei", command=open_txt)
open_button.pack(pady=20)

save_button = Button(root, text="Lade deine Neue Datei runter", command=save_txt)
save_button.pack(pady=20)

root.mainloop()
