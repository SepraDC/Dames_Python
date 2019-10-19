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
        print("Position XY actuelle :", self.x, self.y)
        print("Position sélectionnée :", self.x + dpl_x, self.y + dpl_y)

        # On vérifie si la case sélectionnée est vide - ok
        if isinstance(damier[self.x + dpl_x][self.y + dpl_y], Pion) or isinstance(damier[self.x + dpl_x][self.y + dpl_y], Dame) :
            print(damier[self.x + dpl_x][self.y + dpl_y], Pion)
            return False


        # On vérifie si le pion sort du plateau - nok
        if (self.x + dpl_x or self.y + dpl_y) > len(damier[0]) - 1 : return False

        # On vérifie si le déplacement est diagonale - ok
        if abs(dpl_x) != abs(dpl_y) : return False 

        # On vérifie si le pion est sur la même case - ok
        if x == self.x : return False

        # On vérifie si le déplacement est trop grand - ok
        if abs(dpl_x) > self.DIST_MAX : return False

        coef_x = -1 if dpl_x >= Pion.DIST_MAX else 1
        coef_y = -1 if dpl_y >= Pion.DIST_MAX else 1

        # On vérifie si le joueur peux aller à l'envers - ok
        if not self.deplacement_arriere(dpl_x, dpl_y, coef_x, coef_y, damier) : return False
        print("hello")
        # On bouge le pion - ok
        if abs(dpl_y) == 1 :
            self.x += dpl_x
            self.y += dpl_y
            return True
        else :
            return self.terminer_deplacement(dpl_x, dpl_y, coef_x, coef_y, damier)


    def deplacement_arriere(self, dpl_x, dpl_y, coef_x, coef_y, damier) :

        pion = isinstance(damier[self.x + dpl_x + coef_x][self.y + dpl_y + coef_y], Pion)

        if dpl_y == self.DIST_MAX and self.joueur == 1 and not pion :
            return False
        elif dpl_y == -self.DIST_MAX and self.joueur == 2 and not pion :
            return False
        elif (dpl_y == 1 and self.joueur.id == 1) or (dpl_y == -1 and self.joueur.id == 2) :
            return False

        return True


    def terminer_deplacement(self, dpl_x, dpl_y, coef_x, coef_y, damier) :
        # On vérifie si on passe par dessus un pion, si oui on le mange - ok
        if isinstance(damier[self.x + dpl_x + coef_x][self.y + dpl_y + coef_y], Pion) :
            print("Position du pion mangé :", self.x + dpl_x + coef_x, self.y + dpl_y + coef_y)
            pion_adverse = damier[self.x + dpl_x + coef_x][self.y + dpl_y + coef_y]
            self.x += dpl_x
            self.y += dpl_y
            return self.manger(pion_adverse)
        else : return False


    def manger(self, pion) :
        print(self, pion)
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
        self.img = "./assets/crown.png"

    def deplacement_arriere(self, dpl_x, dpl_y, coef_x, coef_y, damier) :
        return True

    def terminer_deplacement(self, dpl_x, dpl_y, coef_x, coef_y, damier) :
        # On vérifie si on passe par dessus un pion, si oui on le mange - ok
        nbre_pions = 0
        for i in range(1, abs(dpl_y)) :
            print(nbre_pions)
            if isinstance(damier[self.x + dpl_x + (coef_x * i)][self.y + dpl_y + (coef_y * i)], Pion) and nbre_pions < 2:
                nbre_pions += 1
        if nbre_pions == 1 : 
            print("Position du pion mangé :", self.x + dpl_x + coef_x, self.y + dpl_y + coef_y)
            pion_adverse = damier[self.x + dpl_x + coef_x][self.y + dpl_y + coef_y]
            self.x += dpl_x
            self.y += dpl_y
            return self.manger(pion_adverse)
        elif nbre_pions == 0 : 
            self.x += dpl_x
            self.y += dpl_y
            return True
        else : return False


                

        
