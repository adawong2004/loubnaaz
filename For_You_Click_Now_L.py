import tkinter.messagebox as mb 
from tkinter import *
import random
def show():
    mb.showinfo("Tnx","i know it")
    root.destroy()
def move_btn(Event):
   x = random.randint(0,350)
   y = random.randint(0, 350)
   no_button.place(x=x, y=y)
root = Tk()
root.geometry("400x400")
question_label = Label(root, text="Do You Love me Loubna")
question_label.pack(pady=20)
yes_button = Button(root, text="yes", command=show)
yes_button.pack()
no_button = Button(root, text="no")
no_button.pack()
no_button.bind("<Enter>",move_btn)
root.mainloop()

