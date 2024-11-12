import random

from pico2d import *
import game_framework

import game_world
from game_world import add_collision_pair
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
    balls = [Ball(random.randint(100, 1500), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1) # 게임 월드에 추가

    # 충돌 대상들을 등록해주기
    add_collision_pair('boy:ball', boy, None)
    for ball in balls:
        add_collision_pair('boy:ball', None, ball)

    # zombie 생성
    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies, 1)

    add_collision_pair('boy:zombie', boy, None)
    for zombie in zombies:
        add_collision_pair('boy:zombie', None, zombie)
        add_collision_pair('ball:zombie', None, zombie)

def finish():
    game_world.clear()
    pass


def update():
    game_world.update() # 객체들의 위치가 다 결정됐다. 따라서 이어서 충돌 검사를 하면됨.

    # fill here
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

