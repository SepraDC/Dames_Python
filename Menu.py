from tkinter import *

class Menu():
    def __init__(self, canevas, width, height, img):
        self.can = canevas
        self.width = width
        self.height = height
        self.dessinerMenu(img)

    def dessinerMenu(self, img):
        # MAIN MENU
        self.can.create_image(self.width, self.height, image=img, anchor='se')
        self._initButton()

    def _initButton(self):
        # region Buttons
        buttonPosX = self.height / 2 + 15
        buttonPosY = self.width / 2 + 10

        playB = Button(fenMenu, text="Play", command=self.ClearPlay)
        playB.pack()
        playB.place(x=buttonPosX, y=buttonPosY, width=50)

        optionB = Button(fenMenu, text="Options", command=self.ClearOptions)
        optionB.pack()
        optionB.place(x=buttonPosX, y=buttonPosY + 50, width=50)

        creditsB = Button(fenMenu, text="Credits", command=self.ClearOptions)
        creditsB.pack()
        creditsB.place(x=buttonPosX, y=buttonPosY + 100, width=50)
        # endregion

    def dessinerSelection(self):
        # PRESELECT MENU
        preMenu = Tk()
        preMenu.title("Checkers")
        preMenu.resizable(0, 0)
        ws = preMenu.winfo_screenwidth()  # width of the screen
        hs = preMenu.winfo_screenheight()  # height of the screen
        x = (ws / 2) - (self.width / 2)
        y = (hs / 2) - (self.height / 2)
        preMenu.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))
        canPreMenu = Canvas(preMenu, bg='dark grey', height=self.height, width=self.width)
        canPreMenu.pack(side=LEFT)

    def ClearPlay(self):
        fenMenu.destroy()
        self.dessinerSelection()

    def ClearOptions(self):
        pass

h = 740
w = 740

fenMenu = Tk()
fenMenu.title("Checkers")
fenMenu.resizable(0, 0) # Désactive le changement de taille de la fenêtre

#region Window position
ws = fenMenu.winfo_screenwidth() # width of the screen
hs = fenMenu.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
fenMenu.geometry('%dx%d+%d+%d' % (w, h, x, y))
#endregion

can = Canvas(fenMenu, bg='dark grey', width=w, height=h)
can.pack(side=LEFT)
img = PhotoImage(file='assets/Checkers.png')
monMenu = Menu(can, w, h, img)

fenMenu.mainloop()                 # démarrage du réceptionnaire d'événement
fenMenu.destroy()                  # destruction (fermeture) de la fenêtre