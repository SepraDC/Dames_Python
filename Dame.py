from tkinter import *
import Pion


class Jeu:
    def __init__(self, canevas, joueur1, joueur2):
        self.can = canevas
        self.caseSide = 60
        self.jeu = []
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.tour = 1
        self.can.bind("<Button-1>", self.catch_object)
        self.can.bind("<Button1-Motion>", self.move_object)
        self.can.bind("<Button1-ButtonRelease>", self.leave)

        for i in range(10):
            self.jeu.append([''] * 10)

    def PlateauDeJeu(self):
        caseX = 10
        caseY = 10
        self.can.create_rectangle(caseX, caseY, caseX+10* self.caseSide, caseY + self.caseSide, fill="#f4e7d3")
        caseY = 10 + 11* self.caseSide
        self.can.create_rectangle(caseX, caseY, caseX + 10 * self.caseSide, caseY + self.caseSide, fill="#f4e7d3")
        caseY = 10+self.caseSide
        for i in range(10):
            decalage_couleur = 0 if i % 2 == 0 else 1
            for l in range(10):
                couleur = "white" if l % 2 == decalage_couleur else "black"
                self.can.create_rectangle(caseX, caseY, caseX + self.caseSide, caseY + self.caseSide, fill=couleur)
                caseX += self.caseSide
            caseY += self.caseSide
            caseX = 10

        self._initialisationPion()
        self.dessinerPions(self.joueur2)
        self.dessinerPions(self.joueur1)

    def _initialisationPion(self):
        idPions = 103
        for i in range(10):
            for l in range(10):
                joueur = self.joueur1
                if(i <= 4):
                    joueur = self.joueur2
                elif(i>=6):
                    joueur = self.joueur1
                if i < 4 or i >= 6:
                    if i % 2 == 0:
                        if l % 2 != 0:
                            pion = Pion(l, i, joueur)
                            joueur.pions.append(pion)
                            self.jeu[l][i] = Pion
                    else:
                        if l % 2 == 0:
                            pion = Pion(l, i, joueur)
                            joueur.pions.append(pion)
                            self.jeu[l][i] = Pion
                    idPions += 1

    def dessinerPions(self, joueur):
        for pion in joueur.pions:
            x = 10 + pion.x * self.caseSide
            y = 10+ self.caseSide + pion.y * self.caseSide
            self.can.create_oval(x + 5, y+5, x + self.caseSide- 5, y + self.caseSide- 5, fill=pion.joueur.couleur)

    def _changerCouleurCase(self, couleurActuelle):
        if couleurActuelle == 'white':
            return 'black'
        else:
            return 'white'

    def clear(self):
        "Nettoyage du canvas +réinitialisation des variables"
        self.can.delete("all")
        self.caseColor = 'white'
        self.jeu = []
        for i in range(10):
            self.jeu.append(['']*10)

    def catch_object(self, event):
        "clic gauche sur l'objet à déplacer"
        self.x1, self.y1 = event.x, event.y
        print("oi")
        self.select_object = self.can.find_closest(self.x1, self.y1)
        print(self.select_object)
        if self.select_object[0] > 102 and self.select_object[0] < 143:
            self.can.lift(self.select_object)

    def move_object(self, event):
        """Déplacement de l'objet en maintenant
           le bouton gauche de la souris enfoncé"""
        x2, y2 = event.x, event.y
        dx, dy = x2 - self.x1, y2 - self.y1
        if self.select_object[0] > 102 and self.select_object[0] < 143:
            self.can.move(self.select_object, dx, dy)
            self.x1, self.y1 = x2, y2

    def leave(self, event):
        """Objet déplacé, le joueur relâche
           le bouton gauche de la souris"""
        if self.select_object[0] > 102 and self.select_object[0] < 143:
            self.x1, self.y1 = 10 + int(self.x1/self.caseSide) *self.caseSide, 10 + int(self.y1/self.caseSide) *self.caseSide
            print(self.x1, self.y1)
            self.can.coords(self.select_object, self.x1+5, self.y1+5, self.x1 + self.caseSide - 5, self.y1 + self.caseSide - 5)


class Joueur():
    def __init__(self, id, nom, couleur):
        self.id = id
        self.nom = nom
        self.couleur = couleur
        self.pions = []
        self.cimetiere = []

    def ajouterAuCimetiere(self, pion):
        self.cimetiere.append(pion)

    def perdrePion(self, pion):
        for p in self.pions:
            if p == self.pions:
                self.pions.remove(p)


# ------ Programme principal ------

# Création du widget principal ("maître") :
fen1 = Tk()
fen1.resizable(0, 0)
fen1.title("Checkers")

# Création des widgets "esclaves" :
can1 = Canvas(fen1, bg='dark grey', height=740, width=740)
can1.pack(side=LEFT)

j1 = Joueur(1, 'Lucas', 'blue')
j2 = Joueur(2, 'Matthieu', 'red')
# Creation des dames
j = Jeu(can1, j1, j2)

bou1 = Button(fen1, text='Damier', command=j.PlateauDeJeu())
bou1.pack(side=TOP)

bou2 = Button(fen1, text='clear', command=j.clear)
bou2.pack(side=TOP)

fen1.mainloop()  # démarrage du réceptionnaire d'événement
fen1.destroy()  # destruction (fermeture) de la fenêtre
