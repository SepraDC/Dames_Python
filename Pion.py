class Pion():

    DISTANCE_MAX = 2

    def __init__(self, id, x, y, joueur) :
        self.id = id
        self.x = x
        self.y = y
        self.joueur = joueur
        self.couleur = joueur.couleur

    def deplacer(self, x, y, damier) :
        deplacement_x = x - self.x
        deplacement_y = y - self.y

        # Il faut vérifier sur quel diagonale regardez pour le pion a manger

        # On vérifie si le pion sort du plateau
        if (self.x + deplacement_x or self.y + deplacement_y) > len(damier[0]) : return False

        # On vérifie si le déplacement est diagonale
        if abs(deplacement_x) != abs(deplacement_y) : return False 

        # On vérifie si le déplacement est trop grand
        if not isinstance(self, Dame) and abs(deplacement_x) > self.DISTANCE_MAX or abs(deplacement_y) > self.DISTANCE_MAX : return False

        # On vérifie si le joueur peux aller dans ce sens
        if self.joueur.id == 1 and deplacement_y < 0 : return False
        elif self.joueur.id == 2 and deplacement_y > 0 : return False

        # On vérifie si la case sélectionnée est vide
        if damier[self.x + deplacement_x, self.y + deplacement_y] != "" : return False

        # On bouge le pion
        if abs(deplacement_y) == 1 :
            self.x += deplacement_x
            self.y += deplacement_y
            return True
        # On vérifie si on passe par dessus un pion, si oui on le mange
        elif abs(deplacement_y) == self.DISTANCE_MAX and damier[self.x + deplacement_x - 1, self.y + deplacement_y - 1]  != "" :
            self.manger(damier[self.x + deplacement_x - 1, self.y + deplacement_y - 1])
            self.x += deplacement_x
            self.y += deplacement_y
            return True
        else : return False

    def manger(self, pion) :
        self.joueur.ajouterAuCimetiere(pion)
        pion.joueur.perdrePion(pion)

    def __eq__(self, other) :
        if self.x == other.x and self.y == other.y and self.couleur == other.couleur and self.joueur == other.joueur :
            return True


class Dame(Pion) :

    DISTANCE_MAX = 9

    def __init__(self, id, x, y, joueur) :
        Pion.__init__(self, id, x, y, joueur)

        
