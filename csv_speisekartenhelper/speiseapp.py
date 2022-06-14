#Speisekartenhelper
#created 06.13.2022
import tkinter for tk
import csv
with open("/Users/amadeus/Creative Cloud Files/Intern Unterlagen/Schulungsmaterial/Python/Speisekartenhelper/abgleich.csv") as csvdatei:
    abgleich = csv.reader(csvdatei, delimiter=';')
    for row in abgleich:
        print(row)




