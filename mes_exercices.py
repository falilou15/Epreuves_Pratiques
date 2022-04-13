Exercice 08.1 :

def recherche(elt : int,tab : list) -> int:
    for i in range(len(tab)):
        if tab[i] == elt :
                return i
    return -1
