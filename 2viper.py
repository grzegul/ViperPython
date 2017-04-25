#!/usr/bin/env python3

from tkinter import *
from time import sleep

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.new_word = ""
        self.create_widgets()


    def create_widgets(self):
        self.button = Button(self)
        self.button["text"] = "Run!!"
#        self.button["command"] = self.run_text
        self.button.grid()

        self.label = Label(self)
        self.label["text"] = "..." 
#        self.label["command"] = self.update_text
        self.label.grid()

    def update_text(self):
        self.label["text"] = "nowy tekst"




def getTextFrom(filename):
    text_file = open(filename, "r")
    words = text_file.read().split(' ')
    text_file.close()
    return words 

def showEachWordFrom(words):
    for word in words:
        print(word)
        sleep(0.1)


root = Tk()
root.title("Viper")
root.geometry("200x70")

app = Application(root)

root.mainloop()
