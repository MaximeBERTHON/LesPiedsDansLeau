#
#       PremierPasDansLEau
#
#   Enzo Guyot & Maxime Berthon
#
#


tableauJDLS = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]
tableauMois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre",
               "novembre", "decembre"]
incrementMois = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
incrementSiecle = [6, 4, 2, 0, 6, 4]
joursParMois = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# renvoie la date saisie au clavier, avec un controle de validite de la date
def saisirDate():
    while True:

        print("Saisissez la date au format jj/mm/aaaa\n")
        jour = int(input("Saisissez un jour: "))
        mois = int(input("Saisissez un mois(format MM): "))
        annee = int(input("Saisissez une année: "))

        d = {"j": jour, "m": mois, "a": annee}
        if not dateValide(d):
            print("erreur de saisie, date invalide")
        else:
            break

    return d


# renvoie vrai ou faux selon si l'année est bissextile ou non.
def estBissextile(a):
    return (a % 400 == 0) or (a % 4 == 0 and not a % 100 == 0)


# renvoie vrai ou faux selon si la date est valide.

def dateValide(d):
    if estBissextile(d["a"]):
        joursParMois[1] = 29
    else:
        joursParMois[1] = 28
    return d["m"] >= 1 and d["m"] <= 12 and d["j"] >= 1 and d["j"] <= joursParMois[d["m"] - 1] and d["a"] >= 1600 and d[
        "a"] <= 2199


# calcule le jour de la semaine
def calculerJDLS(d):
    # 1. On garde les deux derniers chiffres de l'année en question.
    j = d["a"] % 100

    # 2. On ajoute 1/4 de ce chiffre en ignorant les restes.
    j = j + j // 4

    # 3. On ajoute la journee du mois.
    j = j + d["j"]

    # 4. Selon le mois on ajoute 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5
    j = j + incrementMois[d["m"] - 1]

    # 5. Si l'année est bissextile et le mois est janvier ou fevrier, on ote 1.
    if estBissextile(d["a"]) and (d["m"] == 1 or d["m"] == 2):
        j = j - 1

    # 6. Selon le siecle, on ajoute :
    j = j + incrementSiecle[d["a"] // 100 - 16]

    # 7. On divise la somme par 7 et on garde le reste;
    j = j % 7

    return j


# afficher le resultat
def afficher(d, jdls):
    print("Le jour de la semaine du", d["j"], tableauMois[d["m"] - 1], d["a"], "est un", tableauJDLS[jdls], " :)")


# programme principal
print("Premiers pas dans l'eau, Calendrier Grégorien\n")
date = saisirDate()
jdls = calculerJDLS(date)
afficher(date, jdls)
