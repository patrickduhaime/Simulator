# coding=utf-8
from noeud import Noeud
from liste_doublement_chainee import Liste_Doublement_Chainee
import random


def main():
    # création de la chaine
    liste = Liste_Doublement_Chainee()
    for i in range(5):
        n = Noeud()
        n.cle = i
        liste.add_noeud_fin(n)

    # déclaration et affectation des variables
    moyenne = 0.0
    fini_en_moins_de_trois = 0.0
    nb_iterations = 100000

    # boucle qui permet de répéter les test pendant "nb_iterations"
    for i in range(nb_iterations):

        # Sélection aléatoire du noeud de départ
        noeud_markov = liste.get_noeud(random.randint(1, 3))
        compteur = 0

        # boucle qui effectue le test de deplacement aléatoire jusqu'a se retrouver dans un état absorbant
        while True:
            noeud_markov = deplacement_aleatoire(noeud_markov)
            compteur = compteur + 1
            # état absorbant
            if noeud_markov.suivant is None or noeud_markov.precedent is None:
                break

        # évaluation du moment ou le test prends fin
        if compteur == 1 or compteur == 2:
            fini_en_moins_de_trois = fini_en_moins_de_trois + 1
        moyenne = moyenne + compteur

    # affichage des statistiques des tests effectués
    moyenne = moyenne / nb_iterations
    print "moyenne:", moyenne
    print "pourcentage qui ont finis apres trois pas ou plus:", (1 - (
                fini_en_moins_de_trois / nb_iterations)) * 100, "%"


def deplacement_aleatoire(noeud):
    # si le nombre aléatoire entre 0 et 1 est 0 on se deplace vers le noeud précédent sinon vers le noeud suivant
    if random.randint(0, 1) == 0:
        noeud = noeud.precedent
    else:
        noeud = noeud.suivant
    return noeud


if __name__ == '__main__':
    main()