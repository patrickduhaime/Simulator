from noeud import noeud


class liste:
    def __init__(self):
        self.premier = None
        self.dernier = None
        self.nbNoeud = 0

    def add_noeud_debut(self, n):
        if self.nbNoeud > 0:
            temp = self.premier
            self.premier = n
            self.premier.suivant = temp
        else:
            self.premier = n
        self.nbNoeud = self.nbNoeud + 1

    def add_noeud_fin(self, n):
        if self.nbNoeud > 0:
            self.dernier.suivant = n
            self.dernier = n
        else:
            self.premier = n
        self.nbNoeud = self.nbNoeud + 1
