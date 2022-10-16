import copy
class Plateau:
    def __init__(self, contenu):
        self.contenu = contenu

    def afficher(self, items):
        LARGEUR = len(self.contenu[0])
        HAUTEUR = len(self.contenu)

        plateau = copy.deepcopy(self.contenu)
        for item in items:
            plateau[item.y][item.x] = item.symbole
        for j in range(HAUTEUR):
            print("_" * LARGEUR * 7)
            res = ""
            for i in range(LARGEUR):
                res += "  |  "
                res += plateau[j][i]
            print(res + "  |")
class Plateau1(Plateau):
    def __init__(self):
        TAILLE = 9
        CONTENU = [[str(i) for i in range(TAILLE)]]
        CONTENU[0][4] = "🍎"
        Plateau.__init__(self, CONTENU)

class Plateau2(Plateau):
    def __init__(self):
        TAILLE = 5
        CONTENU = [[str(i+(j*10)) for i in range(TAILLE)] for j in range(TAILLE)]
        CONTENU[0][4] = "🍎"
        Plateau.__init__(self, CONTENU)
