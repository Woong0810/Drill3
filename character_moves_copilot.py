from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 현재 캐릭터의 위치를 추적하기 위한 전역 변수
current_x = 400
current_y = 90

def draw_character_and_grass(x: float, y: float):
    global current_x, current_y
    current_x, current_y = x, y
    clear_canvas()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

def move_rectangle():
    global current_x, current_y
    start_x, start_y = current_x, current_y

    # 현재 위치를 기준으로 사각형의 네 꼭지점 설정
    points = [(start_x, start_y),  # 시작점
             (780, start_y),       # 오른쪽
             (780, 560),          # 오른쪽 위
             (20, 560),           # 왼쪽 위
             (20, 90),            # 왼쪽 아래
             (start_x, start_y)]  # 다시 시작점으로

    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]

        steps = int(max(abs(x2 - x1), abs(y2 - y1)) / 2)
        if steps == 0:
            continue

        for step in range(steps + 1):
            t = step / steps
            x = (1-t) * x1 + t * x2
            y = (1-t) * y1 + t * y2
            draw_character_and_grass(x, y)

def move_triangle():
    global current_x, current_y
    start_x, start_y = current_x, current_y
    side_length = 300

    # 세 점의 좌표 계산
    x1, y1 = start_x, start_y
    x2 = x1 + side_length * math.cos(math.radians(30))
    y2 = y1 + side_length * math.sin(math.radians(30))
    x3 = x1 - side_length * math.cos(math.radians(30))
    y3 = y1 + side_length * math.sin(math.radians(30))

    points = [(x1, y1), (x2, y2), (x3, y3), (x1, y1)]

    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]

        for i in range(50):
            t = i / 49
            x = (1-t) * x1 + t * x2
            y = (1-t) * y1 + t * y2
            draw_character_and_grass(x, y)

def move_circle():
    global current_x, current_y
    start_x, start_y = current_x, current_y

    # 원의 중심과 반지름 계산
    r = 200
    cx = start_x
    cy = start_y + r  # 시작점이 원의 맨 아래가 되도록 중심점 조정

    # 시작점의 각도 계산
    start_angle = math.degrees(math.atan2(start_y - cy, start_x - cx))

    # 360도 회전 후 시작점으로 돌아오기
    for deg in range(0, 361, 2):
        angle = math.radians(start_angle + deg)
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        draw_character_and_grass(x, y)

while True:
    move_rectangle()
    move_triangle()
    move_circle()

close_canvas()
