from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_top():
    pass

def move_right():
    pass

def move_bottom():
    pass

def move_left():
    pass

def move_rectangle():
    print('Moving rectangle')
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_circle():
    print('Moving circle')

    r = 200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    pass

while True:
    move_rectangle()
    move_circle()

close_canvas()