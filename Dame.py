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
        for i in range(10):
            for l in range(10):
                self.can.create_rectangle(self.caseX, self.caseY, self.caseX + self.caseSide, self.caseY + self.caseSide, fill=self.caseColor)
                self._changerDamier()
                self.caseX += self.caseSide
            self._changerDamier()
            self.caseY += self.caseSide
            self.caseX = 10
        self._installationPions()

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

    def _changerDamier(self):
        if self.caseColor == 'white': self.caseColor = 'black'
        else: self.caseColor = 'white'

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