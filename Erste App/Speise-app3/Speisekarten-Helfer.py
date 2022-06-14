from argparse import FileType
from curses import window
from os import close
from pydoc import safeimport
import tkinter as tk
from tkinter import Button, ttk
from tkinter import *
from tkinter import filedialog



def CSV_hello():
    print("Hallo, du hast CSV angeklickt :)")

def EXCEL_hello():
    print("Hallo, du hast EXCEL angeklickt :)")

def PDF_hello():
    print("Hallo, du hast PDF angeklickt :)")

root = tk.Tk()
root.title("Speisekarten Helper")
root.geometry("800x400")
root.minsize(width=300, height=300)
root.maxsize(width=1200, height=600)

#def openFile():
#    filepath = filedialog.askdirectory, initialdir="C\\Users\\amadeus\\Creative Cloud Files\\Intern Unterlagen\\Schulungsmaterial\\Erste App\\Speise-app3\\testdatei.txt"
 #   title="testdatei",
  #  filetypes= (("*txt"))
   # file = open(filepath,"r")
    #print(file.read())

   # file = close(filedialog.asksaveasfilename)
   # file.close=filedialog.SaveFileDialog("/Users/amadeus/Creative Cloud Files/Intern Unterlagen/Schulungsmaterial/#Erste App/Speise-app3/Testdatei.txt")
    

button3 =ttk.Button(root, text="TXT-Testdatei zum ausprobieren", width=30, padding=10)
button3.pack()

buttonup = ttk.Button(root, text="HIER Testdatei oder eigene Datei Hochladen", command=open)
buttonup.pack(filedialog="filedialog",FileType= "txt")



button1 = ttk.Button(root, text="CSV-Download", width=30, command=CSV_hello)
button1.pack(side="top")

button2 =ttk.Button(root, text="EXCEL-Download", width=30, command=EXCEL_hello)
button2.pack(side="top")



button4 =ttk.Button(root, text="Lade hier deine Datei hoch", width=30, padding=10, command=PDF_hello)
button4.pack(side="top")

quit_button=ttk.Button(root, text="Programm beenden", command=root.destroy)
quit_button.pack(side="bottom")



label1 = tk.Label(root, text="Hier deine Datei Hochladen", bg="#550000")
label1.pack(side="top", fill="both", expand="true")

label2 = tk.Label(root, text="Wir sorgen dafür dass du mehr Zeit zum Leben hast", bg="#005500")
label2.pack(side="top", fill="both", expand="true")
button2 =ttk.Button(root, text="Hier die Ausgezeichnete Date RUNTERLADEN", width=30, padding=30, command=EXCEL_hello)
button2.pack(side="top")
label3 = tk.Label(root, text="Ausgabe deiner Speisekarte String", bg="#000055")
label3.pack(side="top", fill="both", expand="true")


root.mainloop()


#Eingabe = input(str("hier die Speisekarte: "))
#Ausgabe = Eingabe.replace("Oliven", "Oliven 2, 3, 4, 2,")
#print(Ausgabe)