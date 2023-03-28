import personne as personne
Personne = personne.Personne

class Auteur(Personne):
    def __init__(self, nom,prenom, oeuvre):
        super().__init__(nom,prenom,)
        self.oeuvre = oeuvre
        
    def listerOeuvre(self):
        print(f"{self.prenom} {self.nom} est l'auteur de:")
        for i in range(len(self.oeuvre)):
            print(self.oeuvre[i])

    def ecrireUnLivre(self, titre):
        self.oeuvre.append(titre)
        print("L'auteur a sortie un nouvel ouvrage  : {} ".format(titre))

    
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = Auteur(auteur.nom, auteur.prenom, auteur.oeuvre)
    
    def print(self):
        print("Le titre du livre est : ", self.titre)


livre = Livre("Dragon Ball", Auteur("Snow", "John", ["Dragon ball", "Dragon ball Z"]))
livre.print()
livre.auteur.listerOeuvre()
print("New books !!!")
livre.auteur.ecrireUnLivre("Dragon ball GT")
livre.auteur.listerOeuvre()