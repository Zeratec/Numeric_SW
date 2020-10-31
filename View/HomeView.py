from tkinter import *
from Controller.HomeController import HomeControllerClass as hc

class HomeViewClass(Frame):

    def __init__(self, window):
        Frame.__init__(self, window)
        self.pack()




        #Création des boutons
        listUAP = ["Production", "Logistique", "Qualite"]

        for uapName in listUAP:
            #Button(Frame, text=uapName, command=lambda buttonName=uapName: hc.buttonContent(buttonName)).pack(side=LEFT)
            Button(self, text=uapName, command=lambda buttonName=uapName: hc.buttonContent(buttonName)).pack(side=LEFT)