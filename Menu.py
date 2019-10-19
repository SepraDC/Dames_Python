from tkinter import *
from Jeu import *
import webbrowser

class Menu:
    def __init__(self,fenetre, canvas, imgBg, imgPlay, imgRules):
        self.fen = fenetre
        self.can = canvas
        self.imgBg = imgBg
        self.imgPlay = imgPlay
        self.imgRules = imgRules

        can.create_image(w, h, image=self.imgBg, anchor='se')
        self.init_buttons()

    def init_buttons(self):
        buttonPosX = h / 2 + 60
        buttonPosY = w / 2 + 90

        playB = Button(self.fen, command=self.setOptions, image=self.imgPlay, borderwidth=0)
        playB.pack()
        playB.place(x=buttonPosX, y=buttonPosY, anchor="center")

        rulesB = Button(self.fen, command=self.checkRules, image=self.imgRules, borderwidth=0)
        rulesB.pack()
        rulesB.place(x=buttonPosX, y=buttonPosY + 100, anchor="center")

    def setOptions(self):
        for l in self.fen.grid_slaves() + self.fen.pack_slaves() + self.fen.place_slaves():
            l.destroy()

        self.fen.title("Checkers - Settings")
        self.fen.geometry('%dx%d+%d+%d' % (300, 200, 800, 300)) # Opening position and width
        #region Player form
        title = Label(self.fen, text="Préparation de la partie")
        title.config(width=200)
        title.pack()

        self.nomJoueur1 = StringVar()
        self.nomJoueur2 = StringVar()
        entryJoueur1 = self.makeentry(self.fen, "Nom du joueur 1 :", text='test1',textvariable=self.nomJoueur1)
        entryJoueur2 = self.makeentry(self.fen, "Nom du joueur 2 :", text='test', textvariable=self.nomJoueur2)
        #endregion
        start = Button(self.fen, text="Next", command=self.ClearPlay)
        start.pack()

    def makeentry(self, parent, texte, **options):
        Label(self.fen, text=texte).pack()
        entry = Entry(parent, **options).pack()
        return entry


    def checkRules(self):
        webbrowser.open('https://tinyurl.com/y54dxe4t')  # Ouverture de la page des rêgles du Jeu de Dames

    def ClearPlay(self):
        for l in self.fen.grid_slaves() + self.fen.pack_slaves() + self.fen.place_slaves():
            l.destroy()
        self.startGame(self.nomJoueur1.get(), self.nomJoueur2.get()) # Execute next step

    def startGame(self, nomJ1, nomJ2):
        # Création du widget principal ("maître") :
        self.fen.resizable(0, 0)
        self.fen.title("Checkers")
        self.fen.geometry('%dx%d+%d+%d' % (740, 740, 600, 180)) # Opening position and width
        # Création des widgets "esclaves"
        j1 = Joueur(1, nomJ1, 'Black')
        j2 = Joueur(2, nomJ2, 'white')
        # Creation des dames
        can1 = Canvas(self.fen, bg='dark grey', height=740, width=740)
        can1.pack(side=LEFT)
        j = Jeu(can1, j1, j2)

        bou1 = Button(self.fen, text='Damier', command=j.PlateauDeJeu())
        bou1.pack(side=TOP)
        bou2 = Button(self.fen, text='clear', command=j.clear)
        bou2.pack(side=TOP)


    # ------ Programme principal ------
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
#endregion

#region Play/Rules buttons
imageBg = PhotoImage(file='assets/Checkers.png')
imagePlay = PhotoImage(file="assets/Play.png").subsample(5, 5)
imageRules = PhotoImage(file="assets/Rules.png").subsample(5, 5)

monMenu = Menu(fenMenu, can, imageBg, imagePlay, imageRules)
#endregion

fenMenu.mainloop()                 # démarrage du réceptionnaire d'événement
fenMenu.destroy()                  # destruction (fermeture) de la fenêtre