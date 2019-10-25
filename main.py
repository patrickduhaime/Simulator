from noeud import Noeud
from liste import Liste
import random


def main():
    liste = Liste()
    for i in range(5):
        n = Noeud()
        n.id = i
        liste.add_noeud(n)

    moyenne = 0.0
    fini_en_trois = 0.0
    resultats = []

    for i in range(10):
        neoud_markov = liste.get_noeud(random.randint(1, 3))
        compteur = 0
        while True:
            neoud_markov = deplacement(neoud_markov)
            compteur = compteur + 1
            if neoud_markov.suivant is None or neoud_markov.precedent is None:
                break
        if compteur == 3:
            fini_en_trois = fini_en_trois + 1
        resultats.append(compteur)

    for i in resultats:
        moyenne = moyenne + i
    moyenne = moyenne / len(resultats)
    print "moyenne:", moyenne
    print "pourcentage qui ont finis en trois:", fini_en_trois / len(resultats)
    print "resultats:", resultats


def deplacement(noeud):
    if random.randint(0, 1) == 0:
        noeud = noeud.precedent
    else:
        noeud = noeud.suivant
    return noeud


if __name__ == '__main__':
    main()
