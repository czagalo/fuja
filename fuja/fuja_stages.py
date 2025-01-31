import fuja_intro
import fuja_sounds
import fuja_enemy
import fuja_object

from pgzero.actor import Actor

import math
import random

floors = []
walls = []
objects = []
stage = fuja_intro.stage
enemys = []
sfx = fuja_sounds.sfx
music = fuja_sounds.music

WIDTH = 800
HEIGHT = 600

##################
# CENÁRIOS DO GAME
# Inserir o chão do cenário
def main_ground(g, d):
    global floors

    for x in range(math.ceil(WIDTH / d)):
        for y in range(math.ceil(HEIGHT / d)):
            floor = Actor(g)
            floor.x = x * d
            floor.y = y * d
            floors.append(floor)

# Borda do cenário
wall = Actor('wall/wall')
wall.x = -1000

# Portas do cenário
door_1 = Actor('object/door')
door_1.x = WIDTH // 2
door_1.y = -100

door_2 = Actor('object/door')
door_2.angle = -90
door_2.x = 900
door_2.y = HEIGHT // 2

door_3 = Actor('object/door')
door_3.angle = 180
door_3.x = WIDTH // 2
door_3.y = 700

door_4 = Actor('object/door')
door_4.angle = 90
door_4.x = -100
door_4.y = HEIGHT // 2

def set_doors():
    door_1.y = 30
    door_2.x = 770
    door_3.y = 570
    door_4.x = 30

###############
# LIMPAR A TELA
def clear_screen():
    fuja_intro.introduction.x = -200
    fuja_intro.f.x = 900
    fuja_intro.u.x = 900
    fuja_intro.j.x = 900
    fuja_intro.a.x = 900
    fuja_intro.start_button.x = -100

    fuja_sounds.control_music(False, stage)

    door_1.y = -100
    door_2.x = 900
    door_3.y = 700
    door_4.x = -100

    wall.x = -1000

    floors.clear()

    fuja_enemy.enemies.clear()

    fuja_object.hide_alarm_clock()

    final.x = -1000
    tic_tac.y = 1200
    fugitive_final.x = -400

    walls.clear()

    objects.clear()



###############
# FASES DO GAME
clock_colected_stage_1 = False
clock_colected_stage_2 = False
clock_colected_stage_3 = False
clock_colected_stage_4 = False
clock_colected_stage_5 = False
clock_colected_stage_6 = False

def set_stage(s):
    global stage
    if s == 1:
        clear_screen()
        stage = s

        fuja_sounds.control_music(True, s)
        main_ground('ground/01', 30)
        wall.x = 400
        set_doors()

        if not clock_colected_stage_1:
            if random.randint(1, 3) == 2:
                fuja_object.set_alarm_clock()

    elif s == 2:
        clear_screen()
        stage = s

        fuja_sounds.control_music(True, s)
        main_ground('ground/01', 30)
        wall.x = 400
        set_doors()

        if not clock_colected_stage_2:
            if random.randint(1, 3) == 2:
                fuja_object.set_alarm_clock()
        

    elif s == 3:
        clear_screen()
        stage = s

        fuja_sounds.control_music(True, s)
        main_ground('ground/02', 31)
        random_wall('wall/column', 15, 46, 200)
        wall.x = 400
        set_doors()

        if not clock_colected_stage_3:
            if random.randint(1, 3) == 2:
                fuja_object.set_alarm_clock()

    elif s == 4:
        clear_screen()
        stage = s

        fuja_sounds.control_music(True, s)
        main_ground('ground/02', 31)
        random_wall('wall/column', 15, 46, 200)
        wall.x = 400
        set_doors()

        if not clock_colected_stage_4:
            if random.randint(1, 3) == 2:
                fuja_object.set_alarm_clock()

    elif s == 5:
        clear_screen()
        stage = s

        fuja_sounds.control_music(True, s)
        main_ground('ground/03', 84)
        random_object('object/grain_01', 40, 20, 150)
        random_wall('enemy/tree', 34, 64, 200)
        wall.x = 400
        set_doors()

        if not clock_colected_stage_5:
            if random.randint(1, 3) == 2:
                fuja_object.set_alarm_clock()
      
    elif s == 6:
        clear_screen()
        stage = s

        fuja_sounds.control_music(True, s)
        main_ground('ground/04', 34)
        random_wall('enemy/troll_1', 26, 30, 950)
        random_object('object/blood_01', 4, 10, 250)
        wall.x = 400
        #random_enemy('enemy/troll_1', 46, 90, 150)
        set_doors()

        if not clock_colected_stage_6:
            if random.randint(1, 3) == 2:
                fuja_object.set_alarm_clock()

###############
# FINAL DO GAME
final = Actor('final/dormindo')
tic_tac = Actor('final/despertador_01')
fugitive_final = Actor('final/fugitivo')
final_triiiim = False
fps_tim = 0
delay_trim = 0
time_restart_game = 0
def final_game():
    global final_triiiim, fps_tim, tic_tac, delay_trim, stage, music
    global time_restart_game, clock_colected_stage_1, clock_colected_stage_2
    if clock_colected_stage_1 == True and clock_colected_stage_2 == True and clock_colected_stage_3 == True and clock_colected_stage_4 == True  and clock_colected_stage_5 == True  and clock_colected_stage_6 == True:
        #time_restart_game += 1
        stage = 7
        clear_screen()
        fuja.fugitive.x = -100
        for clock in fuja_object.alarm_clock_points:
            clock.y = 700
        final.x = 400
        final.y = 300
        tic_tac.x = 180
        tic_tac.y = 400
        global sfx
        delay_trim += 1
        if delay_trim == 100:
            if not final_triiiim:
                fuja_sounds.control_sfx(sfx, 'alarm_clock')
                final_triiiim = True
        elif delay_trim > 100 and delay_trim < 400:
            fps_tim += 1
            if fps_tim >= 10:
                triiiim()
                fps_tim = 0
        elif delay_trim == 400:
            clear_screen()
            final.x = 400
            final.y = 300
            tic_tac.y = 1000
            fuja_sounds.control_sfx(sfx, 'happy')
            final.image = 'final/acordado'
            
            fugitive_final.x = 580
            fugitive_final.y = 300
            
            clock_colected_stage_2 = False


    fugitive_animate()

            
def triiiim():
    global tic_tac
    if tic_tac.image == 'final/despertador_01':
        tic_tac.image = 'final/despertador_02'
    elif tic_tac.image == 'final/despertador_02':
        tic_tac.image = 'final/despertador_03'
    elif tic_tac.image == 'final/despertador_03':
        tic_tac.image = 'final/despertador_04'
    else:
        tic_tac.image = 'final/despertador_01'

animate_side = 'left'
def fugitive_animate():
    global fugitive_final, animate_side
    if animate_side == 'left':
        if fugitive_final.angle > -15:
            fugitive_final.angle = fugitive_final.angle - 1
        elif fugitive_final.angle <= -15:
            animate_side = 'right'
    if animate_side == 'right':
        if fugitive_final.angle < 15:
            fugitive_final.angle = fugitive_final.angle + 1
        elif fugitive_final.angle >= 15:
            animate_side = 'left'

############################
# INSERIR PAREDES ALEATÓRIAS
def random_wall(rw, w, h, r):
    global walls
    
    margin_left_right = 40
    margin_bottom = 24
    clear_area_radius = 190

    def is_within_clear_area(x, y, door_x, door_y):
        return (x - door_x) ** 2 + (y - door_y) ** 2 < clear_area_radius ** 2

    for x in range((WIDTH - 2 * margin_left_right) // w):
        for y in range((HEIGHT - 2 * margin_bottom) // h):
            wall_x = x * w + margin_left_right + 7
            wall_y = y * h + margin_bottom + 5
            if random.randint(0, r) < 50:
                if (not is_within_clear_area(wall_x, wall_y, door_1.x, door_1.y) and
                    not is_within_clear_area(wall_x, wall_y, door_2.x, door_2.y) and
                    not is_within_clear_area(wall_x, wall_y, door_3.x, door_3.y) and
                    not is_within_clear_area(wall_x, wall_y, door_4.x, door_4.y)):
                    random_wall = Actor(rw)
                    random_wall.x = wall_x
                    random_wall.y = wall_y
                    walls.append(random_wall)

############################
# INSERIR OBJETOS ALEATÓRIOS
def random_object(rw, w, h, r):
    global objects
    
    margin_left_right = 40
    margin_bottom = 24
    clear_area_radius = 190

    def is_within_clear_area(x, y, door_x, door_y):
        return (x - door_x) ** 2 + (y - door_y) ** 2 < clear_area_radius ** 2

    for x in range((WIDTH - 2 * margin_left_right) // w):
        for y in range((HEIGHT - 2 * margin_bottom) // h):
            object_x = x * w + margin_left_right + 7
            object_y = y * h + margin_bottom + 5
            if random.randint(0, r) < 50:
                if (not is_within_clear_area(object_x, object_y, door_1.x, door_1.y) and
                    not is_within_clear_area(object_x, object_y, door_2.x, door_2.y) and
                    not is_within_clear_area(object_x, object_y, door_3.x, door_3.y) and
                    not is_within_clear_area(object_x, object_y, door_4.x, door_4.y)):
                    object_wall = Actor(rw)
                    object_wall.x = object_x
                    object_wall.y = object_y
                    objects.append(object_wall)

