import tkinter as tk
from importlib.resources import open_text
from tkinter import *
from tkinter import filedialog

from pkg_resources import safe_name

root = Tk()
root.geometry("500x500")

def open_txt():
    text1_file = filedialog.askopenfilename(initialdir="C:/Users/program/sample1.txt", title="Open Text File")
    text1_file = open(text1_file, 'r+')
    stuff = text1_file.read()
    
    my_text.insert(END, stuff)
    text1_file.close()
    

def save_txt():
    text_file2 =  open('sample2.txt', 'w+')
    text_file2.write(my_text.get(1.0, END))
    

my_text = Text(root, width=40, height=10)
my_text.pack(pady=20)

open_button = Button(root, text="Öffne deine Datei", command=open_txt)
open_button.pack(pady=20)

save_button = Button(root, text="Lade deine Neue Datei runter", command=save_txt)
save_button.pack(pady=20)


root.mainloop()
