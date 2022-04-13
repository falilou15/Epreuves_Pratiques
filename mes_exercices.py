#Exercice 08.1 :

def recherche(elt : int,tab : list) -> int:
    for i in range(len(tab)):
        if tab[i] == elt :
                return i
    return -1

#Nombre puis Double :

def nombres_puis_double(valeurs: list) -> list :
    lst = []
    for i in range(len(valeurs)-1):
        if valeurs[i+1] == valeurs[i] * 2:
            lst.append((valeurs[i] , valeurs[i+1]))
    return lst
