import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mots = {i: 0 for i in range(1, 20)}
with open("data.txt", "r") as fichier:
    for ligne in fichier:
        for mot in ligne.split():
            taille = len(mot)
            if taille in mots:
                mots[taille] += 1

total = sum(mots.values())
pourcentages = {taille: count/total*100 for taille, count in mots.items()}

plt.bar(pourcentages.keys(), pourcentages.values())
plt.title("Pourcentage d'apparition de chaque taille de mot")
plt.xlabel("Taille de mot")
plt.ylabel("Pourcentage")
plt.show()