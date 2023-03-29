import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import string

lettres = {charactere: 0 for charactere in string.ascii_lowercase}
with open("data.txt", "r") as fichier:
    for ligne in fichier:
        for charactere in ligne.lower():
            if charactere in lettres:
                lettres[charactere] += 1

total = sum(lettres.values())
pourcentages = {charactere: count/total*100 for charactere, count in lettres.items()}

plt.bar(pourcentages.keys(), pourcentages.values())
plt.title("Pourcentage d'apparition de chaque lettre")
plt.xlabel("Lettres")
plt.ylabel("Pourcentage")
plt.show()