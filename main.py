from noeud import noeud


def main():
    n1 = noeud()
    n2 = noeud()
    n3 = noeud()

    n1.suivant = n2
    n2.precedent = n1
    n2.suivant = n3
    n3.precedent = n2


if __name__ == '__main__':
    main()
