import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import string

lettres = {char: 0 for char in string.ascii_lowercase}
with open("data.txt", "r") as fichier:
    for ligne in fichier:
        mots = ligne.split()
        for mot in mots:
            charactere = mot[0].lower()
            if charactere in lettres:
                lettres[charactere] += 1

total = sum(lettres.values())
pourcentages = {charactere: count/total*100 for charactere, count in lettres.items()}

plt.bar(pourcentages.keys(), pourcentages.values())
plt.title("Pourcentage d'apparition de chaque lettre en début de mot")
plt.xlabel("Lettres")
plt.ylabel("Pourcentage")
plt.show()