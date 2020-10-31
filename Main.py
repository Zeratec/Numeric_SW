from tkinter import *
import View.HomeView as hv

mainWindow = Tk()
mainWindow.title("Numeric SW")
mainWindow.geometry("720x480")

interface = hv.HomeViewClass(mainWindow)

interface.mainloop()