#age = int(input("wie alt bist du?"))
#höhe = int(input("wie groß bist du?"))
#if (age > 8) and (höhe > 50):
#    print("willkommen an board")
#else:
#    print("leider nein")



#dunkel = input("ist es draußen dukel? ja/nein: ")
#if dunkel == "ja":
#    print("geh schlafen")
#else:
#    print("lerne weiter")

#wetter = input("welches Wetter haben wir? Sonne, Regen, Sturm oder Schnee?: ")
#if wetter == "Sonne":
#    print("Sonnenbrille nicht vergessen")
#elif wetter =="Regen":
#    print("Regenschirm nicht vergessen")
#elif wetter =="Sturm":
#    print("bleibe lieber zuause")
#else:
#    print("bereite dich vor")

#for counter in range(1,11):
#    print("mein Zimmer")

#hippos = 0
#antwort = "ja"
#while antwort == "ja":
#    hippos = hippos + 1
#    print(str(hippos) + "balancing hippos")
#    antwort = input("hippo hinzufügen? ja/nein: ")

#zahl = int(input("zahl eingeben:"))
#while zahl < 10:
#    print(str(zahl) + " ist unter 10")
#    print(str(zahl) + "+1")
#    zahl = zahl + 1
#if zahl >= 10:
#    print (str(zahl) + " ist über 10")

#zahl = int(input("zahl eingeben: "))
#if zahl <= 10:
#    print("die zahl ist unter 10")
#else:
#    print("zahl ist über 10")
#hinzufügen = input("mit 1 addieren? ja/nein?: ")
#print(zahl)
#while hinzufügen =="ja":
#    zahl = zahl + 1
#    print(zahl)
#    if zahl < 10:
#        print("die zahl ist unter 10")
#    else:
#        print("zahl ist über 10")
#    hinzufügen = input("weiter addieren?: ja/nein ")

##################
 #   if zahl >= 10:
 #       break
##################
###########

##################
#zahl = int(input("zahl eingeben"))
#if zahl < 10:
#    print("die Zahl " + str(zahl) + " ist kleiner als 10")
#plus = zahl + 1
#hinzufügen=input("noch eins hinzuüggen: ja oder nein?:")
#while hinzufügen =="ja":
#    print("\n")
#    zahl = zahl + 1
#    if zahl < 10:
#        print("die Zahl " + str(zahl) + " ist kleier als 10")
#    elif zahl == 10:
#        print("die Zahl " + str(zahl) + " ist gleich groß wie 10")
#    else:
#        print("die Zahl " + str(zahl) + " ist größer als 10")
#    print(zahl)
#    hinzufügen=input("noch eins hinzuüggen: ja oder nein?:")
##################
#################
#for hurra in range(1,2):
#    for hip in range(1,3):
#        print("HIP")
#    print("HURRA!")
##################
##################
#for sing in range(1,3):
#    for hoch in range(1,3):
#        print("hoch soll er leben")
#    print("dreiii mal hoch!")
##################


#Funktion um die antwort zu prüfen 
def prüf_antwort (frage, lösung):
    global punktstand
    versuchsreihe = True
    versuche = 0
    while versuchsreihe and versuche < 3:
        if frage.lower() == lösung.lower():
            print("YEAH - richtige Antwort! ")
            punktstand = punktstand + 1
            versuchsreihe = False
        else:
            if versuche < 2:
                frage = input("OOHHH NEIN. Versuchen es noch einmal. ")
            versuche = versuche + 1
    if versuche ==3:
        print("die richtige Antwort ist " + lösung)
 #   else:
 #       print("falsche Antwort")

#Punktestand wird auf null gesetzt       
punktstand = 0
#Willkommensnachricht beim starten des Spiels
print("Erraten Sie das Tier!")
#fragen und funktion prüfzeile der eingabe
frage1 = input("Welcher Bär lebt am Nordpol? ")
prüf_antwort(frage1, "polarbär")
frage2 = input("Welches Tier ist der König des Jungels? ")
prüf_antwort(frage2, "löwe")
frage3 = input("Welches Tier ist das größte Tier? ")
prüf_antwort(frage3, "blauwaal")

print("dein Punktestand ist " + str(punktstand))