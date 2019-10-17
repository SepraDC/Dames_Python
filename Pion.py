class Pion():

    def __init__(self, x, y, joueur) :
        self.x = x
        self.y = y
        self.joueur = joueur
        self.couleur = joueur.couleur

    def deplacer(self, event, damier) :
        deplacementXY = [event.x - self.x, event.y - self.y]

        # On vérifie si le déplacement est diagonale
        if abs(deplacementXY[0]) != abs(deplacementXY[1]) : return False 

        # On vérifie si le déplacement est trop grand 
        for deplacement in range(deplacementXY) :
            if deplacementXY[deplacement] > 3 and deplacementXY[deplacement] < -3 : return False

        # On vérifie si le joueur peux aller dans ce sens
        if self.joueur.id == 1 : 
            if deplacementXY[1] < 0 : return False
        elif self.joueur.id == 2 :
            if deplacementXY[1] > 0 : return False

        # On vérifie si aucun pion ne bloque la route
        if abs(deplacementXY[1]) == 2 :
            if damier[self.x + deplacementXY[0], self.y + deplacementXY[1]] == "" :
                self.x += deplacementXY[0]
                self.y += deplacementXY[1]
                return True
            else : return False
        if abs(deplacementXY[1]) == 3 :
            if damier[self.x + deplacementXY[0] - 1, self.y + deplacementXY[1] - 1]  != "" :
                self.manger(damier[self.x + deplacementXY[0] - 1, self.y + deplacementXY[1] - 1])
                self.x += deplacementXY[0]
                self.y += deplacementXY[1]
                return True
            else : return False

    def manger(self, pion) :
        self.joueur.ajouterAuCimetiere(pion)
        pion.joueur.perdreJoueur(pion)

    def __eq__(self, other) :
        if self.x == other.x and self.y == other.y and self.couleur == other.couleur and self.joueur == other.joueur :
            return True
