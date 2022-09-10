import imp
from time import time
from tkinter import *
from threading import Timer

from importlib_metadata import entry_points




window = Tk()
window.geometry("500x500")

choose_time = int(input("how many seconds: "))
turn = 0
cps = 0
num = 0

def cps2():
    global num
    cps = num/choose_time
    cps = str(cps)
    print("your cps is : " + cps)
    ClickToStart["text"] = "OVER!"
    your_cps = Entry(window)
    your_cps.insert(END, "your cps is : " + cps)
    your_cps.pack() 

cpstrack = Timer(choose_time, cps2)

def addcps():
    global num
    num += 1


def runcps():
    global turn

    if turn == 1:
        addcps()

    if turn == 0:
        cpstrack.start()
        turn += 1
        ClickToStart["text"] = "Click!"
    
ClickToStart = Button(window, text="click to start!", padx = 100, pady = 100, command=runcps)
ClickToStart.pack()


window.mainloop()