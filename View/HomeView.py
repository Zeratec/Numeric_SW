from tkinter import *

from Controller import HomeController as hc
#import Numeric_SW.Controller.HomeController as hc
#from ..Controller import HomeController

def HomeView():
    mainWindow = Tk()
    mainWindow.title("Numeric SW")
    mainWindow.geometry("720x480")

    mainFrame = Frame(mainWindow)
    mainFrame.pack()

    #def buttonContent(buttonName):
        #print (buttonName)

    listUAP = ["Production", "Logistique", "Qualite"]

    for uapName in listUAP:
        Button(mainFrame, text=uapName, command=lambda buttonName=uapName: hc.buttonContent(buttonName)).pack(side=LEFT)

    mainWindow.mainloop()