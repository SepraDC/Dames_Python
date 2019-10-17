from tkinter import *

class Menu:
    def __init__(self, canevas):
        self.can = canevas

h = 620
w = 620

fenMenu = Tk()
can = Canvas(fenMenu, bg='dark grey',height=h,width=w)
can.pack(side=LEFT)
img = PhotoImage(file='assets/Checkers.png')
can.create_image(h, w, image=img, anchor='se')

fenMenu.mainloop()                 # démarrage du réceptionnaire d'événement
fenMenu.destroy()                  # destruction (fermeture) de la fenêtre