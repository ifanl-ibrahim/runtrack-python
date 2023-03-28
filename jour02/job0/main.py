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

a = Personne("Doe", "John")
a.SePresenter()
print(a.get_nom())
print(a.get_prenom())
a.set_nom("Doe2")
a.set_prenom("John2")
a.SePresenter()