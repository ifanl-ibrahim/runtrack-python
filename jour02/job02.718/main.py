import classList as classes 
Personne = classes.Personne
Auteur = classes.Auteur

class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = {}


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}