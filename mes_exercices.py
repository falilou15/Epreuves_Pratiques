#sujets : https://pixees.fr/informatiquelycee/term/suj_bac/index.html

# Exercice 08.1 :

def recherche(elt : int,tab : list) -> int:
    for i in range(len(tab)):
        if tab[i] == elt :
                return i
    return -1

# Nombre puis Double :

def nombres_puis_double(valeurs: list) -> list :
    lst = []
    for i in range(len(valeurs)-1):
        if valeurs[i+1] == valeurs[i] * 2:
            lst.append((valeurs[i] , valeurs[i+1]))
    return lst


# occurrences mini

def occurrences_mini(donnees : list) -> tuple:
    m = []
    for i in range(len(donnees)) :
        if donnees[i] <= donnees[i+1] :
            
        return 

print(occurrences_mini([+13, +49, +13, +5]))

# Maximum

def maximum(nombres):
    n = nombres[0]
    for i in nombres :
        if n < i :
            n = i
    return n

# Indice de la première occurrence

def indice(element, tableau):
    n = None
    for i in tableau :
        if element == i :
            n = tableau.index(i)
    return n

# valeur et indice du max

def valeur_et_indice_du_max(valeurs):
    if valeurs == []:
        return(None,None)
    ind = 0
    nb = 0
    for i in range(len(valeurs)) :
        if nb < valeurs[i] :
            nb = valeurs[i]
            ind = i
    return (nb,ind)
