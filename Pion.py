class Pion:

    DIST_MAX = 2

    def __init__(self, id, x, y, joueur) :
        self.id = id
        self.x = x
        self.y = y
        self.joueur = joueur 
        self.couleur = joueur.couleur

    def deplacer(self, x, y, damier) :
        dpl_x = x - self.x
        dpl_y = y - self.y
        print("Deplacement XY :", dpl_x, dpl_y)
        print("Position XY actuelle :", self.x, self.y)
        print("Position sélectionnée :", self.x + dpl_x, self.y + dpl_y)

        # On vérifie si la case sélectionnée est vide
        if isinstance(damier[self.x + dpl_x][self.y + dpl_y], Pion) : return False
        print("#1")
        # On vérifie si le pion sort du plateau - ok
        if (self.x + dpl_x or self.y + dpl_y) > len(damier[0]) - 1 : return False
        print("#2")
        # On vérifie si le déplacement est diagonale - ok
        if abs(dpl_x) != abs(dpl_y) : return False 
        print("#3")
        # On vérifie si le pion est sur la même case
        if x == self.x : return False
        print("#4")
        # On vérifie si le déplacement est trop grand - ok
        if not isinstance(self, Dame) and abs(dpl_x) > self.DIST_MAX or abs(dpl_y) > self.DIST_MAX : return False

        print("#5")
        coef_x = -1 if dpl_x == Pion.DIST_MAX else 1
        coef_y = -1 if dpl_y == Pion.DIST_MAX else 1
        # On vérifie si le joueur peux aller à l'envers
        if dpl_y == self.DIST_MAX and self.joueur == 1 :
            if not isinstance(damier[self.x + dpl_x + coef_x][self.y + dpl_y + coef_y], Pion) :
                return False
        if dpl_y == -self.DIST_MAX and self.joueur == 2 :
            if not isinstance(damier[self.x + dpl_x + coef_x][self.y + dpl_y + coef_y], Pion) :
                return False

        if (dpl_y == 1 and self.joueur.id == 1) or (dpl_y == -1 and self.joueur.id == 2) :
            return False

        print("#6")
        # On bouge le pion
        if abs(dpl_y) == 1 :
            self.x += dpl_x
            self.y += dpl_y
            return True
        # On vérifie si on passe par dessus un pion, si oui on le mange
        # Remplacer les valeurs cases par les bonnes 
        elif abs(dpl_y) == self.DIST_MAX and isinstance(damier[self.x + dpl_x + coef_x][self.y + dpl_y + coef_y], Pion) :
            print("Position du pion mangé :", self.x + dpl_x + coef_x, self.y + dpl_y + coef_y)
            pion_adverse = damier[self.x + dpl_x + coef_x][self.y + dpl_y + coef_y]
            self.x += dpl_x
            self.y += dpl_y
            return self.manger(pion_adverse)
        else : return False

    def manger(self, pion) :
        if self.joueur != pion.joueur :
            self.joueur.ajouterAuCimetiere(pion)
            pion.joueur.perdrePion(pion)
            return True
        return False

    def __eq__(self, other) :
        if self.x == other.x and self.y == other.y and self.couleur == other.couleur and self.joueur == other.joueur :
            return True


class Dame(Pion) :

    DIST_MAX = 9

    def __init__(self, id, x, y, joueur) :
        Pion.__init__(self, id, x, y, joueur)

        
