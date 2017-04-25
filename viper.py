#!/usr/bin/env python3

from tkinter import *
from time import sleep

def createWindow():
    label = Label(app, text = "Welcome to Viper!!")
    label.grid()
    button = Button(app, text = "Run!")
    button.grid()

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
root.geometry("200x100")
app = Frame(root)
app.grid()
root.mainloop()

root.createWindow()

words = getTextFrom("./source.txt")
showEachWordFrom(words)

