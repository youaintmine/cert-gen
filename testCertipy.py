import pygame
from pygame_test import *
import csv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os, sys

#pygame.init() #remove 5th June
def center_rect(text,xy, font):
    fsize_x, fsize_y = PIL_draw.textsize(text, font)
    x = int(xy[0]-float((fsize_x))/2)
    y = int(xy[1]-float((fsize_y))/2)

    return (x,y)


def scale_img(xy):
    x,y = xy

    x = float(x)
    y = float(y)

    #scale in setup is set to screen_width/width


    x_scale = scale
    y_scale = scale

    if y>height/2:
        y*=y_scale
    if y<height/2:
        y*=y_scale
    if x>width/2:
        x*=x_scale
    if x<=width/2:
        x*=x_scale
    return (int(x),int(y))

def row_count(csv_fileTemp):
    with open(csv_fileTemp) as in_file:
        return sum(1 for _ in in_file)

last_line_csv = row_count(csv_url)

#fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
#font  = null
#ImageFont.truetype(os.path.join(fonts_path, font_style),font_h)

def generate_cert(rect_list):

    #output_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Output')
    with open(csv_url,"r") as csv_list:
        reader = csv.reader(csv_list)

        count = 1
        for row in reader :
            print(row)
            if count == last_line_csv:
                print("All Certificates generated")
                sys.exit()
            else:
                PIL_image = Image.open(image_url)
                PIL_draw = ImageDraw.Draw(PIL_image)

                for i in range(len(rect_list)):
    				#Mapping it to the original File Size and centering it with the rectangle
                    font_h = rect_list[i].height
                    fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
                    font = ImageFont.truetype(os.path.join(fonts_path, font_style),font_h)
                    xy = scale_img(rect_list[i].center)
                    xy = center_rect(row[i],xy, font)
                    PIL_draw.text( xy ,row[i],(28,70,150),font)
                    output_name = output_url+'/'+ str(row[0])+'.pdf'
                    print(output_name)
                PIL_image.save(output_name)
                count = count + 1



draw_start = False
to_draw = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = mouse_pos
            draw_start = True

        if event.type == pygame.MOUSEBUTTONUP:
            final_pos = mouse_pos
            draw_start = False
            rect = pygame.Rect(pos,(final_pos[0]- pos[0], final_pos[1]-pos[1]))
            rect.normalize()
            to_draw+=[rect]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_RETURN:

                print(to_draw[0])

                generate_cert(to_draw)


            if event.key == pygame.K_BACKSPACE:
                to_draw.pop()

#dislpay

    screen.blit(image,(0,0))

    if draw_start:
        pygame.draw.rect(screen,(255,0,0), pygame.Rect(pos, (mouse_pos[0] - pos[0],mouse_pos[1]- pos[1])))
    for item in to_draw:
        pygame.draw.rect(screen,(0,255,0),item)

	#Update
    clock.tick(30)
    pygame.display.update()



#setresolution of photo or get resolution of photo
