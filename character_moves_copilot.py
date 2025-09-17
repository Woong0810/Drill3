from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_character_and_grass(x: float, y: float):
    clear_canvas()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

def move_rectangle():
    # bottom to right
    for x in range(20, 780, 2):
        draw_character_and_grass(x, 90)

    # right to top
    for y in range(90, 560, 2):
        draw_character_and_grass(780, y)

    # top to left
    for x in range(780, 20, -2):
        draw_character_and_grass(x, 560)

    # left to bottom
    for y in range(560, 90, -2):
        draw_character_and_grass(20, y)

def move_triangle():
    # bottom to right
    for x in range(20, 780, 2):
        draw_character_and_grass(x, 90)

    # right-top to left
    for i in range(0, 360, 2):
        x = 780 - (i * 2)
        y = 90 + i
        draw_character_and_grass(x, y)

    # left to bottom
    for i in range(0, 360, 2):
        x = 400 - i
        y = 450 - i
        draw_character_and_grass(x, y)

def move_circle():
    cx, cy = 400, 300  # center position
    r = 200  # radius
    for deg in range(0, 360, 2):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        draw_character_and_grass(x, y)

while True:
    move_rectangle()
    move_triangle()
    move_circle()

close_canvas()
