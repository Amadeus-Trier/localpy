from distutils import text_file
from fileinput import close
from imp import new_module
from msilib import Directory
from telnetlib import TTYPE
from tkinter import filedialog
with open("W:/Creative Cloud Files/Intern Unterlagen/Schulungsmaterial/Python/Pgrogramierübungen/app/tutorial/exportversuche/text.txt", encoding="utf-8") as csvfile:
    text=input
    for row in csvfile:
        print(row)
filedialog.asksaveasfile(initialfile=(True), title="neue-datei")