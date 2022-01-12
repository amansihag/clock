from tkinter import *

from time import strftime
import tkinter

def tym():
     t = strftime( "%H :%M :%S %p")
    # t = time.strftime()
     lbl.config(text=t)
     lbl.pack(anchor='center')
     lbl.after(1000 , tym)
     
     pass
 
     

clock=tkinter.Tk()
lbl_2 = tkinter.Label(clock, text="Time is ",background="cyan", font=("Comic Sans MS",50,"italic"))
lbl_2.pack()
lbl = tkinter.Label(clock,background="black",foreground="red",font=("Comic Sans MS",80,"bold"))
tym()

clock.mainloop()