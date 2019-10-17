from tkinter import *
import os

h = 740
w = 740

class Menu:
    def __init__(self, canevas):
        self.can = canevas

def Jouer():
    print("Changement d'écran")

def ClearPlay():
    fenMenu.destroy()
    # PRESELECT MENU
    preMenu = Tk()
    preMenu.title("Checkers")
    preMenu.resizable(0, 0)
    ws = preMenu.winfo_screenwidth()  # width of the screen
    hs = preMenu.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    preMenu.geometry('%dx%d+%d+%d' % (w, h, x, y))
    canPreMenu = Canvas(preMenu, bg='dark grey', height=h, width=w)
    canPreMenu.pack(side=LEFT)

def ClearOptions():
    pass

fenMenu = Tk()
fenMenu.title("Checkers")
fenMenu.resizable(0, 0)
ws = fenMenu.winfo_screenwidth() # width of the screen
hs = fenMenu.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
fenMenu.geometry('%dx%d+%d+%d' % (w, h, x, y))

# MAIN MENU
can = Canvas(fenMenu, bg='dark grey',height=h,width=w)
can.pack(side=LEFT)
img = PhotoImage(file='assets/Checkers.png')
can.create_image(h, w, image=img, anchor='se')

#region Buttons
buttonPosX = h/2 + 15
buttonPosY = w/2 + 10

playB = Button(fenMenu, text="Play", command=ClearPlay)
playB.pack()
playB.place(x=buttonPosX, y=buttonPosY, width=50)

optionB = Button(fenMenu, text="Options", command=ClearOptions)
optionB.pack()
optionB.place(x=buttonPosX, y=buttonPosY+50, width=50)

creditsB = Button(fenMenu, text="Credits", command=ClearOptions)
creditsB.pack()
creditsB.place(x=buttonPosX, y=buttonPosY+100, width=50)
#endregion

fenMenu.mainloop()                 # démarrage du réceptionnaire d'événement
fenMenu.destroy()                  # destruction (fermeture) de la fenêtre