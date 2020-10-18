from tkinter import *

def matin():
    print('Bonjour\n')

def soir():
    print('Bonsoir\n')

def a():
    btn2 = Button(tk, text="C'est le matin", command=matin)
    btn2.pack()

def b():
    btn3 = Button(tk, text="C'est le soir", command=soir)
    btn3.pack()

tk = Tk()

#btn = Button(tk, text="cliquer ici1", command=hello)
btn = Button(tk, text="cliquer ici2", command=a)
btn.pack()

btn = Button(tk, text="cliquer ici3", command=b)
btn.pack()

input("Press any key to continue")

