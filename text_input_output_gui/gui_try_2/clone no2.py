import tkinter as tk
from importlib.resources import open_text
from tkinter import *
from tkinter import filedialog

from pkg_resources import safe_name

root = Tk()
root.geometry("500x500")

def open_txt():
    text_file1 = filedialog.askopenfilename(initialdir="C:/Users/program/eingabe.txt", title="Open Text File")
    text_file1 = open(text_file1, 'r+')
    stuff = text_file1.read()
    
    my_text1.insert(END, stuff)
    print(text_file1)
    #text_file1()
    #print(Text)

my_text1 = Text(root, width=50, height=10)
my_text1.pack(pady=20)
    

def save_txt():
    text_file2 =  open('ausgabe.txt', 'w+')
    text_file2.write(my_text2.get(1.0, END))


open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=20)

    
save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=20)


my_text2 = Text(root, width=50, height=10)
my_text2.pack(pady=10)




root.mainloop()
