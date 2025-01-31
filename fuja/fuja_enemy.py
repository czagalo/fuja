from pgzero.actor import Actor

import fuja_stages

import random

####
#EYE
enemies = []
enemy = None
fps_enemy = 0
fps_troll = 0

# Quantidade de inimigos
def create_enemies(sprite, n):
    global enemy
    if not enemies:
        for enemy in range(n):
            enemy = Actor(sprite)
            enemy.x = random.randint(0, 10) * random.randint(0, 60) + 100
            enemy.y = random.randint(0, 10) * random.randint(0, 40) + 100
            enemy.orientation = random.choice(['up', 'right', 'down', 'left'])
            enemy.move_count = 0
            enemies.append(enemy)

# Movimentar Inimigos
def move_enemies(enemy_type):
    global enemy, fps_enemy
    fps_enemy += 1
    for enemy in enemies:
        choice = random.randint(0, 2)
        if enemy_type != 'troll':
            if enemy.move_count > 0:
                enemy.move_count = enemy.move_count - 1

                original_x = enemy.x
                original_y = enemy.y
                
                if enemy.orientation == 'right':
                    enemy.x = enemy.x + 2
                elif enemy.orientation == 'up':
                    enemy.y = enemy.y - 2
                elif enemy.orientation == 'left':
                    enemy.x = enemy.x - 2
                elif enemy.orientation == 'down':
                    enemy.y = enemy.y + 2

                if enemy.x <= 60 or enemy.x >= 740 or enemy.y <= 60 or enemy.y >= 540:
                    enemy.x = original_x
                    enemy.y = original_y
                    enemy.moveCount = 0

            elif choice == 0:
                enemy.move_count = 60
            elif choice == 1:
                enemy.orientation = random.choice(['up', 'right', 'down', 'left'])

    # Animação dos sprites dos inimigos
    if fps_enemy >= 10:
        for enemy in enemies:
            # Animação do Olho
            if enemy_type == 'eye':
                if enemy.orientation == 'up':
                    if enemy.image == 'enemy/eye_up_01':
                        enemy.image = 'enemy/eye_up_02'
                    elif enemy.image == 'enemy/eye_up_02':
                        enemy.image = 'enemy/eye_up_03'
                    elif enemy.image == 'enemy/eye_up_03':
                        enemy.image = 'enemy/eye_up_04'
                    else:
                        enemy.image = 'enemy/eye_up_01'
                elif enemy.orientation == 'right':
                    if enemy.image == 'enemy/eye_right_01':
                        enemy.image = 'enemy/eye_right_02'
                    elif enemy.image == 'enemy/eye_right_02':
                        enemy.image = 'enemy/eye_right_03'
                    elif enemy.image == 'enemy/eye_right_03':
                        enemy.image = 'enemy/eye_right_04'
                    else:
                        enemy.image = 'enemy/eye_right_01'
                elif enemy.orientation == 'down':
                    if enemy.image == 'enemy/eye_down_01':
                        enemy.image = 'enemy/eye_down_02'
                    elif enemy.image == 'enemy/eye_down_02':
                        enemy.image = 'enemy/eye_down_03'
                    elif enemy.image == 'enemy/eye_down_03':
                        enemy.image = 'enemy/eye_down_04'
                    else:
                        enemy.image = 'enemy/eye_down_01'
                elif enemy.orientation == 'left':
                    if enemy.image == 'enemy/eye_left_01':
                        enemy.image = 'enemy/eye_left_02'
                    elif enemy.image == 'enemy/eye_left_02':
                        enemy.image = 'enemy/eye_left_03'
                    elif enemy.image == 'enemy/eye_left_03':
                        enemy.image = 'enemy/eye_left_04'
                    else:
                        enemy.image = 'enemy/eye_left_01'

            # Animação do Doppelganger
            if enemy_type == 'doppelganger':
                if enemy.orientation == 'up':
                    if enemy.image == 'player/run/up_01':
                        enemy.image = 'player/run/up_02'
                    elif enemy.image == 'player/run/up_02':
                        enemy.image = 'player/run/up_03'
                    elif enemy.image == 'player/run/up_04':
                        enemy.image = 'player/run/up_05'
                    elif enemy.image == 'player/run/up_05':
                        enemy.image = 'player/run/up_06'
                    elif enemy.image == 'player/run/up_06':
                        enemy.image = 'player/run/up_07'
                    elif enemy.image == 'player/run/up_07':
                        enemy.image = 'player/run/up_08'
                    else:
                        enemy.image = 'player/run/up_01'
                elif enemy.orientation == 'right':
                    if enemy.image == 'player/run/right_01':
                        enemy.image = 'player/run/right_02'
                    elif enemy.image == 'player/run/right_02':
                        enemy.image = 'player/run/right_03'
                    elif enemy.image == 'player/run/right_04':
                        enemy.image = 'player/run/right_05'
                    elif enemy.image == 'player/run/right_05':
                        enemy.image = 'player/run/right_06'
                    elif enemy.image == 'player/run/right_06':
                        enemy.image = 'player/run/right_07'
                    elif enemy.image == 'player/run/right_07':
                        enemy.image = 'player/run/right_08'
                    else:
                        enemy.image = 'player/run/right_01'
                elif enemy.orientation == 'down':
                    if enemy.image == 'player/run/down_01':
                        enemy.image = 'player/run/down_02'
                    elif enemy.image == 'player/run/down_02':
                        enemy.image = 'player/run/down_03'
                    elif enemy.image == 'player/run/down_04':
                        enemy.image = 'player/run/down_05'
                    elif enemy.image == 'player/run/down_05':
                        enemy.image = 'player/run/down_06'
                    elif enemy.image == 'player/run/down_06':
                        enemy.image = 'player/run/down_07'
                    elif enemy.image == 'player/run/down_07':
                        enemy.image = 'player/run/down_08'
                    else:
                        enemy.image = 'player/run/down_01'
                elif enemy.orientation == 'left':
                    if enemy.image == 'player/run/left_01':
                        enemy.image = 'player/run/left_02'
                    elif enemy.image == 'player/run/left_02':
                        enemy.image = 'player/run/left_03'
                    elif enemy.image == 'player/run/left_04':
                        enemy.image = 'player/run/left_05'
                    elif enemy.image == 'player/run/left_05':
                        enemy.image = 'player/run/left_06'
                    elif enemy.image == 'player/run/left_06':
                        enemy.image = 'player/run/left_07'
                    elif enemy.image == 'player/run/left_07':
                        enemy.image = 'player/run/left_08'
                    else:
                        enemy.image = 'player/run/left_01'
              
        fps_enemy = 0

##############
# ANIMAR TROLL
def move_troll():
    global fps_troll
    fps_troll += 1

    # Animação dos sprites dos trolls
    if fps_troll >= 30:
        for enemy in enemies:
            if enemy.image == 'enemy/troll_1':
                enemy.image = 'enemy/troll_2'
                fps_troll = 0
            elif enemy.image == 'enemy/troll_2':
                enemy.image = 'enemy/troll_3'
                fps_troll = 0
            elif enemy.image == 'enemy/troll_3':
                enemy.image = 'enemy/troll_4'
                fps_troll = 0
            elif enemy.image == 'enemy/troll_4':
                enemy.image = 'enemy/troll_5'
                fps_troll = 0
            elif enemy.image == 'enemy/troll_5':
                enemy.image = 'enemy/troll_6'
                fps_troll = 0
            else:
                enemy.image = 'enemy/troll_1'
                fps_troll = 0


"""


def eye():
    npc = 'enemy/eye_down_01'
    return npc

#################################
# INSERIR INIMIGOS ALEATORIAMENTE
def random_enemy(enemy, w, h, r):
    global enemys
    enemys = []
    margin_left_right = 40
    margin_bottom = 24
    clear_area_radius = 190

    def is_within_clear_area(x, y, door_x, door_y):
        return (x - door_x) ** 2 + (y - door_y) ** 2 < clear_area_radius ** 2
    
    for x in range((800 - 2 * margin_left_right) // w):
        for y in range((600 - 2 * margin_bottom) // h):
            enemy_x = x * w + margin_left_right + 7
            enemy_y = y * h + margin_bottom + 5
            if random.randint(0, r) < 50:
                if (not is_within_clear_area(enemy_x, enemy_y, fuja_stages.door_1.x, fuja_stages.door_1.y) and
                    not is_within_clear_area(enemy_x, enemy_y, fuja_stages.door_2.x, fuja_stages.door_2.y) and
                    not is_within_clear_area(enemy_x, enemy_y, fuja_stages.door_3.x, fuja_stages.door_3.y) and
                    not is_within_clear_area(enemy_x, enemy_y, fuja_stages.door_4.x, fuja_stages.door_4.y)):
                    #random_enemy = Actor(enemy)
                    enemy.x = enemy_x
                    enemy.y = enemy_y
                    enemys.append(enemy)


# Inserir Paredes Aleatórias
def random_wall(enemy, w, h, r):
    global enemys
    enemys = []
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










#INSERIR POSIÇÃO INICIAL DA PC
#Recebe como parâmetros os valores 'y' ou 'x' (pos)
#referente a posição y e x da janela do game
def set_pc_start_posicion(pos):
    y = 288
    x = 393

    if pos == 'y':
        return y
    elif pos == 'x':
        return x

#MUDAR O SPRITE DA PC QUANDO PARADA
#Recebe como parâmetro os valores 'up', 'down', 'left' ou 'right' (orientation)
#referente a direção que a PC está olhando
def set_pc_idle_sprite(orientation):
    if orientation == 'up':
        pc = 'player/idle/up_04'
    elif orientation == 'down':
        pc = 'player/idle/down_03'
    elif orientation == 'left':
        pc = 'player/idle/left_03'
    elif orientation == 'right':
        pc = 'player/idle/right_03'

    #return pc

#INSERIR ANIMAÇÃO DA PC QUANDO PARADA
#Recebe como parâmetros os valores 'up', 'down', 'left' ou 'right' (orientation)
#e o valores da função set_pc_idle_sprite(orientation)
#referente a direção que a PC está olhando
#e o sprite da PC que está sendo exibido no momento
def set_pc_idle_animation(orientation, pc):
    if orientation == 'up':
        if pc == 'player/idle/up_01':
            pc = 'player/idle/up_02'
        elif pc == 'player/idle/up_02':
            pc = 'player/idle/up_03'
        elif pc == 'player/idle/up_03':
            pc = 'player/idle/up_04'
        elif pc == 'player/idle/up_04':
            pc = 'player/idle/up_01'
    elif orientation == 'down':
        if pc == 'player/idle/down_01':
            pc = 'player/idle/down_02'
        elif pc == 'player/idle/down_02':
            pc = 'player/idle/down_03'
        elif pc == 'player/idle/down_03':
            pc = 'player/idle/down_01'
    elif orientation == 'left':
        if pc == 'player/idle/left_01':
            pc = 'player/idle/left_02'
        elif pc == 'player/idle/left_02':
            pc = 'player/idle/left_03'
        elif pc == 'player/idle/left_03':
            pc = 'player/idle/left_01'
    elif orientation == 'right':
        if pc == 'player/idle/right_01':
            pc = 'player/idle/right_02'
        elif pc == 'player/idle/right_02':
            pc = 'player/idle/right_03'
        elif pc == 'player/idle/right_03':
            pc = 'player/idle/right_01'

    return pc

#MUDAR O SPRITE DA PC QUANDO CORRENDO
#Recebe como parâmetro os valores 'up', 'down', 'left' ou 'right' (orientation)
#referente a direção que a PC está correndo
def set_pc_run_sprite(orientation):
    if orientation == 'up':
        pc = 'player/run/up_01'
    elif orientation == 'down':
        pc = 'player/run/down_01'
    elif orientation == 'left':
        pc = 'player/run/left_01'
    elif orientation == 'right':
        pc = 'player/run/right_01'

    return pc

#INSERIR ANIMAÇÃO DA PC QUANDO CORRENDO
#Recebe como parâmetros os valores 'up', 'down', 'left' ou 'right' (orientation)
#e o valores da função set_pc_idle_sprite(orientation)
#referente a direção que a PC está correndo
#e o sprite da PC que está sendo exibido no momento
def set_pc_run_animation(orientation, pc):
    if orientation == 'up':
        if pc == 'player/run/up_01':
            pc = 'player/run/up_02'
        elif pc == 'player/run/up_02':
            pc = 'player/run/up_03'
        elif pc == 'player/run/up_03':
            pc = 'player/run/up_04'
        elif pc == 'player/run/up_04':
            pc = 'player/run/up_05'
        elif pc == 'player/run/up_05':
            pc = 'player/run/up_06'
        elif pc == 'player/run/up_06':
            pc = 'player/run/up_07'
        elif pc == 'player/run/up_07':
            pc = 'player/run/up_08'
        elif pc == 'player/run/up_08':
            pc = 'player/run/up_01'
    elif orientation == 'down':
        if pc == 'player/run/down_01':
            pc = 'player/run/down_02'
        elif pc == 'player/run/down_02':
            pc = 'player/run/down_03'
        elif pc == 'player/run/down_03':
            pc = 'player/run/down_04'
        elif pc == 'player/run/down_04':
            pc = 'player/run/down_05'
        elif pc == 'player/run/down_05':
            pc = 'player/run/down_06'
        elif pc == 'player/run/down_06':
            pc = 'player/run/down_07'
        elif pc == 'player/run/down_07':
            pc = 'player/run/down_08'
        elif pc == 'player/run/down_08':
            pc = 'player/run/down_01'
    elif orientation == 'left':
        if pc == 'player/run/left_01':
            pc = 'player/run/left_02'
        elif pc == 'player/run/left_02':
            pc = 'player/run/left_03'
        elif pc == 'player/run/left_03':
            pc = 'player/run/left_04'
        elif pc == 'player/run/left_04':
            pc = 'player/run/left_05'
        elif pc == 'player/run/left_05':
            pc = 'player/run/left_06'
        elif pc == 'player/run/left_06':
            pc = 'player/run/left_07'
        elif pc == 'player/run/left_07':
            pc = 'player/run/left_08'
        elif pc == 'player/run/left_08':
            pc = 'player/run/left_01'
    elif orientation == 'right':
        if pc == 'player/run/right_01':
            pc = 'player/run/right_02'
        elif pc == 'player/run/right_02':
            pc = 'player/run/right_03'
        elif pc == 'player/run/right_03':
            pc = 'player/run/right_04'
        elif pc == 'player/run/right_04':
            pc = 'player/run/right_05'
        elif pc == 'player/run/right_05':
            pc = 'player/run/right_06'
        elif pc == 'player/run/right_06':
            pc = 'player/run/right_07'
        elif pc == 'player/run/right_07':
            pc = 'player/run/right_08'
        elif pc == 'player/run/right_08':
            pc = 'player/run/right_01'

    return pc
    """