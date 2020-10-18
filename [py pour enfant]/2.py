from tkinter import *

def hello():
   print('Bonjour\n')


tk = Tk()
btn = Button(tk, text="cliquer ici", command=hello)
btn.pack()

input("Press any key to continue")

