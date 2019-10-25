from noeud import Noeud
from liste import Liste
import random


def main():
    liste = Liste()
    for i in range(5):
        n = Noeud()
        n.id = i
        liste.add_noeud(n)

    debut_markov = liste.get_noeud(random.randint(1, 3))
    test = ""


if __name__ == '__main__':
    main()
