import csv
from tkinter import Tk
from tkinter import *
import tkinter as tk
from tkinter import filedialog, Button
import os


temp_path = None
excel_path = None
output_path = None

f = open("files.txt","w")

window = Tk()
window.geometry('500x500')



def img():
    global temp_path
    root = tk.Tk()
    root.withdraw()
    temp_path = filedialog.askopenfilename()
    print(temp_path)
    f.write(temp_path+"\n")


def excel():
    global excel_path
    root = tk.Tk()
    root.withdraw()
    excel_path = filedialog.askopenfilename()
    print(excel_path)
    f.write(excel_path+"\n")

def outFolder():
    global output_path
    root = tk.Tk()
    root.withdraw()
    output_path = filedialog.askdirectory()
    print(output_path)
    f.write(output_path+"\n")

def exit_status():
    f.write(var.get()+"\n")
    print(var.get()+"\n")
    window.quit()



button1 = tk.Button(window, text='Click to go Template',command=img)
button1.grid(row=0, sticky='w')


button2 = Button(window, text='Click to Excel',command=excel)
button2.grid(row=1, sticky='w')

var = StringVar(window)
var.set("MLSJN.TTF")
fontoption = OptionMenu(window, var, "MLSJN.TTF","Lato-Black.ttf","MATURASC.TTF","OLDENGL.TTF","VIVALDII.TTF","copperplate gothic font.ttf","best_font.otf")
fontoption.grid(row=2, sticky='w')

button3 = Button(window, text='Select output folder',command=outFolder)
button3.grid(row=3, sticky='w')

buttonend = Button(window, text='Click if all Set Run CertiPy after this', command=exit_status)
buttonend.grid(row=4, sticky='w')


window.mainloop()
f.close()
