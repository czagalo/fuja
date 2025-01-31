import pgzrun

import fuja_sounds
import fuja_intro
import fuja_menu
import fuja_stages
import fuja_player
import fuja_enemy
import fuja_object

import random

menu = fuja_menu.menu
music = fuja_sounds.music
sfx = fuja_sounds.sfx
stage = fuja_intro.stage
floors = fuja_stages.floors
clocks = fuja_object.alarm_clock_points


WIDTH=800
HEIGHT=600
TITLE= 'FUJA'

#######################
# PERSONAGEM DO JOGADOR
fugitive = Actor(fuja_player.set_pc())
fugitive.x = -100

#######################
# INIMIGOS
enemies = fuja_enemy.enemies

#############
# DESPERTADOR
alarm_clock = fuja_object.alarm_clock
fuja_object.hide_alarm_clock()

#######
# FINAL
final = fuja_stages.final
final.x = -1000
tic_tac = fuja_stages.tic_tac
tic_tac.y = 1300
fugitive_final = fuja_stages.fugitive_final
fugitive_final.x = -1000

####################
# PAREDES ALEATÓRIAS
walls = fuja_stages.walls
objects = fuja_stages.objects

###########################
# DESENHAR OS ATORES NA TELA
def draw():
    #global eye
    screen.clear()
    screen.fill((0,0,0))

    fuja_intro.introduction.draw()
    fuja_intro.f.draw()
    fuja_intro.u.draw()
    fuja_intro.j.draw()
    fuja_intro.a.draw()
    fuja_intro.start_button.draw()

    if floors:
        for floor in floors:
            floor.draw()

    fuja_stages.wall.draw()

    fuja_stages.door_1.draw()
    fuja_stages.door_2.draw()
    fuja_stages.door_3.draw()
    fuja_stages.door_4.draw()

    for object in objects:
        object.draw()

    for obstacle in walls:
        obstacle.draw()

    alarm_clock.draw()

    if enemies:
        for enemy in enemies:
            enemy.draw()

    fugitive.draw()

    if clocks:
        for clock_point in clocks:
            clock_point.draw()

    final.draw()
    tic_tac.draw()
    fugitive_final.draw()

    fuja_intro.menu_button.draw()

    fuja_menu.menu_screen.draw()
    fuja_menu.checkbox_music.draw()
    fuja_menu.checkbox_sfx.draw()
    fuja_menu.button_return.draw()
    fuja_menu.button_exit.draw()

##################
# EVENTOS DO MOUSE

def on_mouse_down(pos): 
    global menu, sfx, music, stage

    #Clicar no ícone do menu
    if fuja_intro.menu_button.collidepoint(pos):
        fuja_sounds.control_sfx(sfx, 'click')
        fuja_menu.change_menu_posicion(True)
        menu = fuja_menu.menu

    #Controle do menu
    if menu == True:
        if fuja_menu.button_return.collidepoint(pos):
            fuja_sounds.control_sfx(sfx, 'click')
            fuja_menu.start_menu_posicion() 
            fuja_intro.menu_final_posicion()
        
        if fuja_menu.button_exit.collidepoint(pos):
            fuja_sounds.control_sfx(sfx, 'click')
            exit()

        if music == True:
            if fuja_menu.checkbox_music.collidepoint(pos):
                fuja_sounds.control_sfx(sfx, 'click')
                music = False
                fuja_menu.checkbox_music.image = 'button/uncheck'
                fuja_menu.checkbox_music.x = 117
                fuja_sounds.control_music(music, stage)
                
        else:
            if fuja_menu.checkbox_music.collidepoint(pos):
                fuja_sounds.control_sfx(sfx, 'click')
                music = True
                fuja_menu.checkbox_music.image = 'button/check'
                fuja_menu.checkbox_music.x = 120
                fuja_sounds.control_music(music, stage)

        if sfx == True:
            if fuja_menu.checkbox_sfx.collidepoint(pos):
                sfx = False
                fuja_sounds.control_sfx(sfx, 'click')
                fuja_menu.checkbox_sfx.image = 'button/uncheck'
                fuja_menu.checkbox_sfx.x = 117
        else:
            if fuja_menu.checkbox_sfx.collidepoint(pos):
                sfx = True
                fuja_sounds.control_sfx(sfx, 'click')
                fuja_menu.checkbox_sfx.image = 'button/check'
                fuja_menu.checkbox_sfx.x = 120
    
    #Clicar no botão iniciar  
    if fuja_intro.start_button.collidepoint(pos):
        fuja_sounds.control_sfx(sfx, 'click')
        fuja_sounds.control_music(False, stage)
        stage = 1
        fuja_stages.set_stage(stage)
        fugitive.x = 800 // 2
        fugitive.y = 600 // 2

# Ponteiro do mouse sobre os objetos
def on_mouse_move(pos):
    if fuja_intro.start_button.collidepoint(pos):
        fuja_intro.start_button.image = 'button/iniciar_hover'
    else:
        fuja_intro.start_button.image = 'button/iniciar'

    if fuja_intro.menu_button.collidepoint(pos):
        fuja_intro.menu_button.image = 'button/menu_hover'
    else:
        fuja_intro.menu_button.image = 'button/menu'
    
    if fuja_menu.button_return.collidepoint(pos):
        fuja_menu.button_return.image = 'button/voltar_hover'
    else:
        fuja_menu.button_return.image = 'button/voltar'

    if fuja_menu.button_exit.collidepoint(pos):
        fuja_menu.button_exit.image = 'button/sair_hover'
    else:
        fuja_menu.button_exit.image = 'button/sair'

##########################
# ATUALIZAR A TELA DO GAME
pc_idle = True
pc_orientation = 'up'
pc_fps_idle = 0
pc_fps_run = 0
pc_fps_dead = 0
time_intro = 0
time_pc_walk = 0
alarm_clock_collected = 0
pause_enemy = False
pause_fugitive = False
enemy_choice = ''

def update():
    global pc_idle, pc_orientation, pc_fps_idle, pc_fps_run, pause_enemy, pause_fugitive, enemy_choice
    global stage, time_intro, time_pc_walk, sfx, alarm_clock_collected, pc_fps_dead, walls, objects
    pc_idle = True
    pc_fps_idle += 1
    pc_fps_run += 1
    time_pc_walk += 1

    time_intro += 1
    
    # Reiniciar a introdução
    if stage == 0:
        if time_intro == 4500:
            fuja_intro.set_intro()
            time_intro = 0

    # Verifica colisão com paredes
    for obstacle in walls:
        if fugitive.colliderect(obstacle):
            if pc_orientation == 'up':
                fugitive.y += 1
            elif pc_orientation == 'left':
                fugitive.x += 1
            elif pc_orientation == 'right':
                fugitive.x -= 1
            elif pc_orientation == 'down':
                fugitive.y -= 1
            #pause_fugitive = True

    # Controle do PC e animação em movimento
    if not pause_fugitive:
        if keyboard.up:
            if fugitive.y >= 40:
                if time_pc_walk >= 40:
                    fuja_sounds.control_sfx(sfx, 'pc_walk')
                    time_pc_walk = 0
                pc_idle = False
                pc_orientation = 'up'
                if pc_fps_run >= 10:
                    fugitive.image = fuja_player.set_pc_run_animation(pc_orientation, fugitive.image)
                    pc_fps_run = 0    
                fugitive.y -= 1
        elif keyboard.left:
            if fugitive.x >= 42:
                if time_pc_walk >= 40:
                    fuja_sounds.control_sfx(sfx, 'pc_walk')
                    time_pc_walk = 0
                pc_idle = False
                pc_orientation = 'left'
                if pc_fps_run >= 10:
                    fugitive.image = fuja_player.set_pc_run_animation(pc_orientation, fugitive.image)
                    pc_fps_run = 0
                fugitive.x -= 1
        elif keyboard.right:
            if fugitive.x <= 756:
                if time_pc_walk >= 40:
                    fuja_sounds.control_sfx(sfx, 'pc_walk')
                    time_pc_walk = 0
                pc_idle = False
                pc_orientation = 'right'
                if pc_fps_run >= 10:
                    fugitive.image = fuja_player.set_pc_run_animation(pc_orientation, fugitive.image)
                    pc_fps_run = 0
                fugitive.x += 1
        elif keyboard.down:
            if fugitive.y <= 551:
                if time_pc_walk >= 40:
                    fuja_sounds.control_sfx(sfx, 'pc_walk')
                    time_pc_walk = 0
                pc_idle = False
                pc_orientation = 'down'
                if pc_fps_run >= 10:
                    fugitive.image = fuja_player.set_pc_run_animation(pc_orientation, fugitive.image)
                    pc_fps_run = 0
                fugitive.y += 1
    
    # Animação do PC quando parado
    if pc_fps_dead == 0:
        if pc_idle:
            if pc_orientation == 'up':
                if pc_fps_idle >= 60:
                    fugitive.image = fuja_player.set_pc_idle_animation(pc_orientation, fugitive.image)
                    pc_fps_idle = 0
            else:
                if pc_fps_idle >= 40:
                    fugitive.image = fuja_player.set_pc_idle_animation(pc_orientation, fugitive.image)
                    pc_fps_idle = 0

        # Colisão com as portas
        if fugitive.colliderect(fuja_stages.door_1) or fugitive.colliderect(fuja_stages.door_2) or fugitive.colliderect(fuja_stages.door_3) or fugitive.colliderect(fuja_stages.door_4):
            stage = random.randint(1, 7)
            fuja_stages.set_stage(stage)
            if stage == 2:
                enemy_choice = 'eye'
                fuja_enemy.create_enemies('enemy/eye_down_01', random.randint(1, 20))
            elif stage == 4:
                enemy_choice = 'doppelganger'
                fuja_enemy.create_enemies('player/run/down_01', random.randint(1, 10))
            elif stage == 5:
                enemy_choice = 'tree'
                fuja_enemy.create_enemies('enemy/tree', random.randint(1, 5))
            elif stage == 6:
                enemy_choice = 'troll'
                fuja_enemy.create_enemies('enemy/troll_1', random.randint(1, 8))

        if fugitive.colliderect(fuja_stages.door_1):
            fugitive.x = 400
            fugitive.y = 533
            fugitive.image = 'player/idle/up_01'
        elif fugitive.colliderect(fuja_stages.door_2):
            fugitive.x = 63
            fugitive.y = 297
            fugitive.image = 'player/idle/right_01'
        elif fugitive.colliderect(fuja_stages.door_3):
            fugitive.x = 400
            fugitive.y = 64
            fugitive.image = 'player/idle/down_01'
        elif fugitive.colliderect(fuja_stages.door_4):
            fugitive.x = 736
            fugitive.y = 295
            fugitive.image = 'player/idle/left_01'

    # Animação dos Inimigos
    if not pause_enemy:
        if enemy_choice == 'eye':
            fuja_enemy.move_enemies('eye')
        elif enemy_choice == 'doppelganger':
            fuja_enemy.move_enemies('doppelganger')
        elif enemy_choice == 'tree':
            None
        elif enemy_choice == 'troll':
            fuja_enemy.move_troll()


    # Verifica colisão e pausa o jogo
    for enemy in enemies:
        if fugitive.colliderect(enemy):
            pause_enemy = True
            pause_fugitive = True

    # Incrementa pc_fps_dead apenas se o jogo estiver pausado
    if pause_enemy and pause_fugitive:
        fuja_sounds.control_music(False, stage)
        pc_fps_dead += 1

        # Altera a imagem do fugitivo conforme pc_fps_dead
        if pc_fps_dead == 10:
            fuja_sounds.control_sfx(sfx, 'death')
            fugitive.image = 'player/death/dead_pc_01'
        elif pc_fps_dead == 40:
            fugitive.image = 'player/death/dead_pc_02'
        elif pc_fps_dead == 80:
            fugitive.image = 'player/death/dead_pc_03'
        elif pc_fps_dead == 120:
            fugitive.image = 'player/death/dead_pc_04'
        elif pc_fps_dead == 160:
            fugitive.image = 'player/death/dead_pc_05'
        elif pc_fps_dead == 200:
            fugitive.image = 'player/death/dead_pc_06'
        elif pc_fps_dead == 240:
            fuja_sounds.control_sfx(sfx, 'funebre')
            fugitive.image = 'player/death/dead_pc_07'
        elif pc_fps_dead == 700:
            pause_enemy = False
            pause_fugitive = False
            pc_fps_dead = 0
            fuja_stages.set_stage(1)
            fugitive.x = WIDTH // 2
            fugitive.y = HEIGHT // 2
            alarm_clock_collected = 0
            fuja_stages.clock_colected_stage_1 = False
            fuja_stages.clock_colected_stage_2 = False
            fuja_stages.clock_colected_stage_3 = False
            fuja_stages.clock_colected_stage_4 = False
            fuja_stages.clock_colected_stage_5 = False
            fuja_stages.clock_colected_stage_6 = False
            clocks.clear()
    
    # Animação do despertador
    fuja_object.animate_alarm_clock()

    # Pegar o despertador
    if fugitive.colliderect(alarm_clock):
        fuja_sounds.control_sfx(sfx, 'tic_tac')
        alarm_clock_collected += 1
        fuja_object.hide_alarm_clock()
        fuja_object.clock_point(alarm_clock_collected)
        if fuja_stages.stage == 1:
            fuja_stages.clock_colected_stage_1 = True
        if fuja_stages.stage == 2:
            fuja_stages.clock_colected_stage_2 = True
        if fuja_stages.stage == 3:
            fuja_stages.clock_colected_stage_3 = True
        if fuja_stages.stage == 4:
            fuja_stages.clock_colected_stage_4 = True
        if fuja_stages.stage == 5:
            fuja_stages.clock_colected_stage_5 = True
        if fuja_stages.stage == 6:
            fuja_stages.clock_colected_stage_6 = True

    # Final do game
    fuja_stages.final_game()

################
# INICIAR O GAME
fuja_intro.set_intro()

pgzrun.go()