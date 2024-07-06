def statlist(mon_liste) :
    dictionaire = {}
    min_ = min(mon_liste)
    max_ = max(mon_liste)
    somme = sum(mon_liste)
    compteur = len(mon_liste)
    moyenne = sum(mon_liste)/ len(mon_liste)
    dictionaire["minimum"] = min_
    dictionaire["maximum"] = max_
    dictionaire["somme"] = somme
    dictionaire["nembre d'elements"] = compteur
    dictionaire["moyenne"] = moyenne
    #print(dictionaire)
    #resultat = "Minimum ", min_, "Maximum ", max_, "Somme ", somme, "Compteur ", compteur, "Moyenne ", moyenne
    #for i, j in dictionaire.items() :
       # print(f"{i} {j}")
    return dictionaire