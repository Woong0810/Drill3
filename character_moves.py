from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_top():
    print('Moving top')
    for x in range(780, 20, -2):
        draw_character_and_grass(x, 560)
    pass

def move_right():
    print('Moving right')
    for y in range(90, 560, 2):
        draw_character_and_grass(780, y)
    pass

def move_bottom_start():
    print('Moving bottom')
    for x in range(400, 780, 2):
        draw_character_and_grass(x, 90)
    pass

def move_bottom_finish():
    for x in range(20, 400, 2):
        draw_character_and_grass(x, 90)
    pass

def move_left():
    print('Moving left')
    for y in range(560, 90, -2):
        draw_character_and_grass(20, y)
    pass

def move_rectangle():
    print('Moving rectangle')
    move_bottom_start()
    move_right()
    move_top()
    move_left()
    move_bottom_finish()
    pass

def move_circle():
    print('Moving circle')

    r = 210
    for deg in range(-90, 270):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_character_and_grass(x, y)
    pass

def draw_character_and_grass(x: float, y: float):
    clear_canvas()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)


while True:
    move_rectangle()
    move_circle()

close_canvas()