from tkinter import *
#from ..Controller import HomeController

def HomeView():
    mainWindow = Tk()
    mainWindow.title("Numeric SW")
    mainWindow.geometry("720x480")

    mainFrame = Frame(mainWindow)
    mainFrame.pack()

    def buttonContent(buttonName):
        print (buttonName)

    listUAP = ["Production", "Logistique", "Qualite"]

    for uapName in listUAP:
        Button(mainFrame, text=uapName, command=lambda buttonName=uapName: buttonContent(buttonName)).pack(side=LEFT)

    mainWindow.mainloop()

if __name__ == "__main__":
    HomeView()