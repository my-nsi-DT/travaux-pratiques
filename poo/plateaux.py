class Plateau:
    def __init__(self, taille, contenu):
        self.taille = taille
        self.contenu = contenu

    def afficher(self, items):
        print("_" * self.taille * 3)
        res = ""
        plateau = self.contenu.copy()
        for item in items:
            plateau[item.x] = item.symbole
        for i in range(self.taille):
            res += "|"
            res += plateau[i]
        print(res + "|")
        print("‾" * self.taille * 3)

class Plateau1(Plateau):
    def __init__(self):
        TAILLE = 9
        CONTENU = [str(i) for i in range(TAILLE)]
        CONTENU[4] = "🍎"
        Plateau.__init__(self, TAILLE, CONTENU)
