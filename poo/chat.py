class Chat:
    def __init__(self, x):
        self.symbole = "🐈"
        self.x = x
    def avancer(self, nombreCases):
        self.x += nombreCases
    def reculer(self, nombreCases):
        self.x -= nombreCases
