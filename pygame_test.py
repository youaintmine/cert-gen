import pygame
import csv
import os
from tkinter import Tk
from tkinter import *
from PIL import Image, ImageDraw, ImageFont
from string import Template
#pygame.init() #remove 5th June
f = open("files.txt","r")
url_path = f.read().split("\n")
image_url = url_path[0]
csv_url = url_path[1]
output_url = url_path[2]
font_style = url_path[3]
#print(image_url+csv_url+font_url)
def getRow():
    with open(csv_url,"r") as f:
        reader = csv.reader(f)
        row1 = next(reader)
        return row1


with open(csv_url,'a') as fd:
    field = getRow()
    writer = csv.writer(fd)
    writer.writerow(["__","___"])

image = pygame.image.load(image_url)

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


width, height = image.get_rect().size
scale = 1


while width>screen_width or height>screen_height:
    width/=2
    height/= 2
    scale*=2


image = pygame.transform.scale(image,(int(width), int(height)))


PIL_image = Image.open(image_url)
PIL_draw = ImageDraw.Draw(PIL_image)



clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Certifyproj')


running = True

#set picture to load to be matched with the frame
#    width,height = image.get_rect().size
##
#    while width>screen_width or height>screen_height
