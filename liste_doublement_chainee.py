# coding=utf-8
# classe partielle (juste les opérations nécessaires pour résoudre le problème donné
class Liste_Doublement_Chainee:
    def __init__(self):
        self.premier = None
        self.dernier = None
        self.nb_noeuds = 0

    # ajoute un noeud à la fin de la chaine
    def add_noeud_fin(self, n):
        if self.nb_noeuds > 0:
            self.dernier.suivant = n
            n.precedent = self.dernier
            self.dernier = n
        else:
            self.premier = n
            self.dernier = n
        self.nb_noeuds = self.nb_noeuds + 1

    # chercher un noeud à l'aide de sa clé
    def get_noeud(self, cle):
        if self.nb_noeuds > 0:
            courant = self.premier
            if courant.cle == cle:
                return courant
            for i in range(1, self.nb_noeuds):
                courant = courant.suivant
                if courant is None:
                    return None
                if courant.cle == cle:
                    return courant
        return None
