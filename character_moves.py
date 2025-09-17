from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_rectangle():
    print('Moving rectangle')
    pass

def move_circle():
    print('Moving circle')
    clear_canvas()
    grass.draw_now(400, 30)
    character.draw_now(400, 90)
    pass

while True:
    move_rectangle()
    move_circle()

close_canvas()