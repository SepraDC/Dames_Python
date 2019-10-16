from tkinter import *

class Dame:
    def __init__(self, canevas):
        self.can = canevas
        self.caseX = 10
        self.caseY = 10
        self.caseSide = 60
        self.caseColor = 'white'

    def damier(self):
        for i in range(10):
            for l in range(10):
                self.can.create_rectangle(self.caseX, self.caseY, self.caseX + self.caseSide, self.caseX + self.caseSide, fill=self.caseColor)
                if self.caseColor == 'white':
                    self.caseColor = 'black'
                else:
                    self.caseColor = 'white'
                self.caseX += self.caseSide
            self.caseY += self.caseSide
            self.caseX = 0

#------ Programme principal ------

# Création du widget principal ("maître") :
fen1 = Tk()

# Création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=620,width=620)
can1.pack(side=LEFT)

#Creation des dames
d = Dame(can1)
bou1 = Button(fen1,text='Damier', command=d.damier)
bou1.pack(side=TOP)

fen1.mainloop()                 # démarrage du réceptionnaire d'événement
fen1.destroy()                  # destruction (fermeture) de la fenêtre