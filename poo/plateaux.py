class Plateau:
    TAILLE = 2
    CONTENU = [str(i) for i in range(TAILLE)]

    def afficher(items):
        print("_" * Plateau.TAILLE * 3)
        res = ""
        for item in items:
            Plateau.CONTENU[item.x] = item.symbole
        for i in range(Plateau.TAILLE):
            res += "|"
            res += Plateau.CONTENU[i]
        print(res + "|")
        print("‾" * Plateau.TAILLE * 3)

class Plateau1(Plateau):
    Plateau.TAILLE = 6
    Plateau.CONTENU = [str(i) for i in range(Plateau.TAILLE)]
