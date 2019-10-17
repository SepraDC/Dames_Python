class Pion():

    DISTANCE_MAX = 2

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
        if abs(deplacementXY[0]) > Pion.DISTANCE_MAX or abs(deplacementXY[1]) > Pion.DISTANCE_MAX : return False

        # On vérifie si le joueur peux aller dans ce sens
        if self.joueur.id == 1 and deplacementXY[1] < 0 : return False
        elif self.joueur.id == 2 and deplacementXY[1] > 0 : return False

        # On vérifie si aucun pion ne bloque la route
        if abs(deplacementXY[1]) == 1 and damier[self.x + deplacementXY[0], self.y + deplacementXY[1]] == "" :
            self.x += deplacementXY[0]
            self.y += deplacementXY[1]
            return True
        # On vérifie si on passe par dessus un pion, si oui on le mange
        elif abs(deplacementXY[1]) == Pion.DISTANCE_MAX and damier[self.x + deplacementXY[0] - 1, self.y + deplacementXY[1] - 1]  != "" :
            self.manger(damier[self.x + deplacementXY[0] - 1, self.y + deplacementXY[1] - 1])
            self.x += deplacementXY[0]
            self.y += deplacementXY[1]
            return True
        else : return False

    def manger(self, pion) :
        self.joueur.ajouterAuCimetiere(pion)
        pion.joueur.perdrePion(pion)

    def __eq__(self, other) :
        if self.x == other.x and self.y == other.y and self.couleur == other.couleur and self.joueur == other.joueur :
            return True


class Dame(Pion) :

    def __init__(self, x, y, joueur) :
        Pion.__init__(self, x, y, joueur)

    def deplacer(self, event, damier) :
        return "PUUUUTE"

        

    
