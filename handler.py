# The handler
from tkinter import Tk
from tkinter import *
import tkinter as tk
import os, sys

window = Tk()
window.geometry('500x500')

def main():
    os.system('python main.py')

def Certifice():
    os.system('python testCertipy.py')

def Close():
    window.quit()


button1 = tk.Button(window, text='Setup the files', command=main)
button1.grid(row=0, sticky='w')

button1 = tk.Button(window, text='Run certificate Generator', command=Certifice)
button1.grid(row=1, sticky='w')

button1 = tk.Button(window, text='Close', command=Close)
button1.grid(row=2, sticky='w')

window.mainloop()
