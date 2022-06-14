import numpy as np

liste = {
    "beine": [4, 5, 4, 4, 4],
    "groesse": [34.4, 66.4, 22.4, 44.3, 34.3],
    "breite": [33.3, 22.4, 88.3, 44.3, 33.4],
    "label": [1, 0, 1, 1, 1] #[Hund=1], [nicht Hund=0]
}

beine = np.array(liste["beine"])
groesse = np.array(liste["groesse"])
breite = np.array(liste["breite"])
label = np.array(liste["label"])

 
merkmale = np.array([liste["beine"], liste["breite"], liste["groesse"], liste["label"]])
print(merkmale[:2:1])


