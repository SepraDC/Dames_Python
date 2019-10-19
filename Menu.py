from tkinter import *
from Jeu import *
import webbrowser

class Menu:
    def __init__(self):
        pass

def setOptions():
    fenMenu.destroy()
    global fenOpt
    fenOpt = Tk()
    fenOpt.title("Checkers - Settings")
    fenOpt.geometry('%dx%d+%d+%d' % (300, 200, 800, 300)) # Opening position and width
    #region Player form
    title = Label(fenOpt, text="Préparation de la partie")
    title.config(width=200)
    title.pack()
    wName = Label(fenOpt, text="Nom du joueur 1 :")
    wName.pack()
    nomJoueur1 = Entry(fenOpt)
    nomJoueur1.pack()
    wName2 = Label(fenOpt, text="Nom du joueur 2 :")
    wName2.pack()
    nomJoueur2 = Entry(fenOpt)
    nomJoueur2.pack()
    #endregion
    start = Button(fenOpt, text="Next", command=ClearPlay)
    start.pack()

def checkRules():
    webbrowser.open('https://tinyurl.com/y54dxe4t')  # Ouverture de la page des rêgles du Jeu de Dames

def ClearPlay():
    fenOpt.destroy() # Close window
    startGame() # Execute next step

def startGame():
    # ------ Programme principal ------

    # Création du widget principal ("maître") :
    fen1 = Tk()
    fen1.resizable(0, 0)
    fen1.title("Checkers")
    fen1.geometry('%dx%d+%d+%d' % (740, 740, 600, 180)) # Opening position and width
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


#region Tk Creation
fenMenu = Tk()
fenMenu.title("Checkers - Main menu")
fenMenu.resizable(0, 0) # Désactive le changement de taille de la fenêtre

#Window position
global x, y, ws, hs

h = 740
w = 740

ws = fenMenu.winfo_screenwidth() # width of the screen
hs = fenMenu.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
fenMenu.geometry('%dx%d+%d+%d' % (w, h, x, y)) # Opening position and width

#Background image
can = Canvas(fenMenu, width=w, height=h)
can.pack(side=LEFT)
img = PhotoImage(file='assets/Checkers.png')
can.create_image(w, h, image=img, anchor='se')
#endregion

#region Play/Rules buttons

buttonPosX = h/2 + 60
buttonPosY = w/2 + 90

# Impossible d'afficher l'image d'un bouton en objet
imagePlay = PhotoImage(file="assets/Play.png").subsample(5, 5)
imageRules = PhotoImage(file="assets/Rules.png").subsample(5, 5)

playB = Button(fenMenu, command=setOptions, image=imagePlay, borderwidth=0)
playB.pack()
playB.place(x=buttonPosX, y=buttonPosY, anchor="center")

rulesB = Button(fenMenu, command=checkRules, image=imageRules, borderwidth=0)
rulesB.pack()
rulesB.place(x=buttonPosX, y=buttonPosY + 100, anchor="center")
#endregion

fenMenu.mainloop()                 # démarrage du réceptionnaire d'événement
fenMenu.destroy()                  # destruction (fermeture) de la fenêtre