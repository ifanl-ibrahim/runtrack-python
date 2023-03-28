class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def get_nom(self):
        return self.nom
    def set_nom(self, nom):
        self.nom = nom
    def get_prenom(self):
        return self.prenom
    def set_prenom(self, prenom):
        self.prenom = prenom
    
    def SePresenter(self):
        print("Je m'appelle " + self.prenom + " " + self.nom)

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