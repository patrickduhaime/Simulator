from noeud import noeud


class liste:
    def __init__(self):
        self.premier = None
        self.dernier = None
        self.nbNoeud = 0


    def addNoeudDebut(self, n):
        if self.nbNoeud > 0:
           temp = self.premier
           self.premier=n
           self.premier.suivant = temp