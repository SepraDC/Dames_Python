from tkinter import *

class Dame:
    def __init__(self, canevas):
        self.can = canevas
        self.caseX = 10
        self.caseY = 10
        self.caseSide = 60
        self.caseColor = 'white'
        self.jeu = []
        for i in range(10):
            self.jeu.append(['','','','','','','','','',''])

    def damier(self):
        for largeur in range(self.caseX):
            decalage_couleur = 0 if largeur % 2 == 0 else 1
            for longueur in range(10) :
                color = "white" if longueur % 2 == decalage_couleur else "black"
                position = (60 * 10 / self.caseX)
                self.can.create_rectangle( position * longueur, position * largeur, (position * longueur) + 60, (position * largeur) + 60, fill=color)

    def _installationPions(self):
        #installation des pions du joueur 1
        for i in range(4):
            for l in range(10):
                x = 10 + l * self.caseSide
                y = 10 + i * self.caseSide
                if i % 2 == 0:
                    if l % 2 != 0:
                        self.jeu[i][l] = 'J1'
                        self.can.create_oval(x + 5, y + 5, x + self.caseSide - 5, y + self.caseSide-5, fill='red')
                else:
                    if l % 2 == 0:
                        self.jeu[i][l] = 'J1'
                        self.can.create_oval(x + 5, y + 5, x + self.caseSide - 5, y + self.caseSide-5, fill='red')
        for i in range(6, 10):
            for l in range(10):
                x = 10 + l * self.caseSide
                y = 10 + i * self.caseSide
                if i % 2 == 0:
                    if l % 2 != 0:
                        self.jeu[l][i] = 'J2'
                        self.can.create_oval(x + 5, y + 5, x + self.caseSide - 5, y + self.caseSide - 5, fill='blue')
                else:
                    if l % 2 == 0:
                        self.jeu[i][l] = 'J2'
                        self.can.create_oval(x + 5, y + 5, x + self.caseSide - 5, y + self.caseSide - 5, fill='blue')

    def clear(self):
        "Nettoyage du canevas +réinitialisation des variables"
        self.can.delete("all")
        self.caseX = 10
        self.caseY = 10
        self.caseColor = 'white'
        self.jeu = []
        for i in range(10):
            self.jeu.append(['', '', '', '', '', '', '', '', '', ''])

#------ Programme principal ------

# Création du widget principal ("maître") :
fen1 = Tk()
fen1.resizable(0, 0)
fen1.title("Checkers")

# Création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=740,width=740)
can1.pack(side=LEFT)


#Creation des dames
d = Dame(can1)
bou1 = Button(fen1,text='Damier', command=d.damier)
bou1.pack(side=TOP)

bou2 = Button(fen1,text='clear', command=d.clear)
bou2.pack(side=TOP)

fen1.mainloop()                 # démarrage du réceptionnaire d'événement
fen1.destroy()                  # destruction (fermeture) de la fenêtre