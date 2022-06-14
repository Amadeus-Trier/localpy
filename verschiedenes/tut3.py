
#print("anfang der programms")
#print("Wie heißt du?")
name = input("Bitte dein Name eingeben: ")
#print("Hallo " + name)
#print("Wie alt bist du " + name +"?")
age = int(input("Bitte trage dein Alter ein: "))
geburtsjahr = 2022 - age
print(geburtsjahr)
print("Du heißt also " + name + ", " + str(age) + "\n" + str(geburtsjahr) + " gebohren.")
#print("ende des programms")