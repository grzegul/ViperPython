#!/usr/bin/env python3

from tkinter import *
from time import sleep

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()
        self.words = self.getTextFrom("source.txt")

    def create_widgets(self):
        self.label = Label(self)
        self.label["text"] = "..." 
        self.label.grid()

        self.button = Button(self)
        self.button["text"] = "Run!!"
        self.button["command"] = self.update_text
        self.button.grid()

    def getTextFrom(self, filename):
        text_file = open(filename, "r")
        words = text_file.read().split()
        text_file.close()
        return words 

    def showEachWordFrom(self, words):
        for word in words:
            sleep(0.5)
            self.label["text"] = word
            print(word)

    def update_text(self):
#        words = self.getTextFrom("source.txt")
        self.showEachWordFrom(self.words)
        self.label["text"] = "Done"


root = Tk()
root.title("Viper")
root.geometry("200x70")
app = Application(root)
app.mainloop()
