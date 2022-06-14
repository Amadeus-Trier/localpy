#Speisekartenhelper
#created 06.13.2022
wörter=[]
ergänzung=[]



import csv
with open("/Users/amadeus/Creative Cloud Files/Intern Unterlagen/Schulungsmaterial/Python/Speisekartenhelper/allergene.csv") as csvdatei:
    abgleich = csv.reader(csvdatei, delimiter=';')
    for row in abgleich:
        ergänzung.append([row[1]])
        wörter.append([row[0]])
        #print(row)

print(wörter)
print(ergänzung)


