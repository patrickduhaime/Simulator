from noeud import Noeud
from liste_doublement_chainee import Liste_Doublement_Chainee
import random


def main():
    liste = Liste_Doublement_Chainee()
    for i in range(5):
        n = Noeud()
        n.cle = i
        liste.add_noeud(n)

    moyenne = 0.0
    fini_en_moins_de_trois = 0.0
    # resultats = []
    nb_iterations = 100000

    for i in range(nb_iterations):
        neoud_markov = liste.get_noeud(random.randint(1, 3))
        compteur = 0
        while True:
            neoud_markov = deplacement_aleatoire(neoud_markov)
            compteur = compteur + 1
            if neoud_markov.suivant is None or neoud_markov.precedent is None:
                break
        if compteur == 1 or compteur == 2:
            fini_en_moins_de_trois = fini_en_moins_de_trois + 1
        moyenne = moyenne + compteur
        # resultats.append(compteur)

    moyenne = moyenne / nb_iterations
    print "moyenne:", moyenne
    print "pourcentage qui ont finis apres trois pas ou plus:", (1 - (fini_en_moins_de_trois / nb_iterations)) * 100, "%"
    # print "resultats:", resultats


def deplacement_aleatoire(noeud):
    if random.randint(0, 1) == 0:
        noeud = noeud.precedent
    else:
        noeud = noeud.suivant
    return noeud


if __name__ == '__main__':
    main()
