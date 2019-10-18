from tkinter import *
from Jeu import *
import time
import os

class Menu:
    def __init__(self):
        pass

def ClearPlay():
    fenMenu.destroy()
    startGame()

def startGame():
    # ------ Programme principal ------

    # Création du widget principal ("maître") :
    fen1 = Tk()
    fen1.resizable(0, 0)
    fen1.title("Checkers")

    # Création des widgets "esclaves" :

    j1 = Joueur(1, 'Lucas', 'Black')
    j2 = Joueur(2, 'Matthieu', 'white')
    # Creation des dames
    can1 = Canvas(fen1, bg='dark grey', height=740, width=740)
    can1.pack(side=LEFT)
    j = Jeu(can1, j1, j2)

    bou1 = Button(fen1, text='Damier', command=j.PlateauDeJeu())
    bou1.pack(side=TOP)
    bou2 = Button(fen1, text='clear', command=j.clear)
    bou2.pack(side=TOP)
    fen1.mainloop()  # démarrage du réceptionnaire d'événement
    fen1.destroy()  # destruction (fermeture) de la fenêtre

h = 740
w = 740

fenMenu = Tk()
fenMenu.title("Checkers - Main menu")
fenMenu.resizable(0, 0) # Désactive le changement de taille de la fenêtre

#Background image
can = Canvas(fenMenu, width=w, height=h)
can.pack(side=LEFT)
img = PhotoImage(file='assets/Checkers.png')
can.create_image(w, h, image=img, anchor='se')

#region Buttons

buttonPosX = h/2 + 50
buttonPosY = w/2 + 50

# Impossible d'afficher l'image d'un bouton en objet
imagePlay = PhotoImage(file="assets/Play.png").subsample(5, 5)
playB = Button(fenMenu, text="Play", command=ClearPlay, image=imagePlay)
playB.pack()
playB.place(x=buttonPosX, y=buttonPosY, anchor="center")

#endregion

#region Window position
ws = fenMenu.winfo_screenwidth() # width of the screen
hs = fenMenu.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
fenMenu.geometry('%dx%d+%d+%d' % (w, h, x, y))
#endregion

fenMenu.mainloop()                 # démarrage du réceptionnaire d'événement
fenMenu.destroy()                  # destruction (fermeture) de la fenêtre

