from pgzero.actor import Actor

import fuja_intro

menu = False

#################
# OBJETOS DO MENU
menu_screen = Actor('screen/menu')
checkbox_music = Actor('button/check')
checkbox_sfx = Actor('button/check')
button_return = Actor('button/voltar')
button_exit = Actor('button/sair')

def start_menu_posicion():
    menu_screen.x = -100
    menu_screen.y = 180
    checkbox_music.x = -100
    checkbox_music.y = 123
    checkbox_sfx.x = -100
    checkbox_sfx.y = 160
    button_return.x = -100
    button_return.y = 220
    button_exit.x = -100
    button_exit.y = 305

def change_menu_posicion(tf):
    global menu
    menu = tf
    if menu == False:
        fuja_intro.menu_button.x = 50

        menu_screen.x = -100
        checkbox_music.x = -100
        checkbox_sfx.x = -100
        button_return.x = -100
        button_exit.x = -100
    else:
        fuja_intro.menu_button.x = -100

        menu_screen.x = 80
        checkbox_music.x = 120
        checkbox_sfx.x = 120
        button_return.x = 80
        button_exit.x = 80