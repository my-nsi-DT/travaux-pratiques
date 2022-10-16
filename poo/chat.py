class Chat:
    def __init__(self, x, y = 0):
        self.symbole = "🐈"
        self.x = x
        self.y = y
    def avancer(self, nombreCases):
        self.x += nombreCases
    def reculer(self, nombreCases):
        self.x -= nombreCases
    def monter(self, nombreCases):
        self.y -= nombreCases
    def descendre(self, nombreCases):
        self.y += nombreCases
    def manger(self, plateau):
        plateau.contenu[self.y][self.x] = str(self.x)
