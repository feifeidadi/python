from tkinter import *

count_matin = 0
count_soir = 0

tk = Tk()

def matin():
    global count_matin
    if count_matin == 0:
        print('Bonjour\n')
        count_matin += 1

def soir():
    global count_soir
    if count_soir == 0:
        print('Bonsoir\n')
    else:
        print(count_soir)

    count_soir += 1

btn2 = Button(tk, text="C'est le matin", command=matin)
btn2.pack()

btn3 = Button(tk, text="C'est le soir", command=soir)
btn3.pack()


input("Press any key to continue\n\n")

