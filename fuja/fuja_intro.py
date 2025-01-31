import fuja_sounds
import fuja_menu

from pgzero.actor import Actor
from pgzero.builtins import clock

stage = 0

###############################
# IMAGEM DA INTRODUÇÃO DO GAME
introduction = Actor('logo/cz')
introduction.x = 400
introduction.y = 300

############################
# IMAGENS DO TÍTULO DO JOGO
f = Actor('title/f')
u = Actor('title/u')
j = Actor('title/j')
a = Actor('title/a')

def title_start_posicion(letter):
    if letter == 'f':
        f.x = 900
        f.y = 175
    elif letter == 'u':
        u.x = 900
        u.y = 240
    elif letter == 'j':
        j.x = 900
        j.y = 435
    elif letter == 'a':
        a.x = 900
        a.y = 480

def f_final_posicion():
    f.x = 680
def u_final_posicion():
    u.x = 735
def j_final_posicion():
    j.x = 650
def a_final_posicion():
    a.x = 730

################################
# IMAGENS DOS BOTÕES DA ABERTURA
start_button = Actor('button/iniciar')
menu_button = Actor('button/menu')

def button_start_posicion(button):
    if button == 'start':
        start_button.x = -100
        start_button.y = 550
    elif button == 'menu':
        menu_button.x = -100
        menu_button.y = 50

def start_final_posicion():
    start_button.x = 110
def menu_final_posicion():
    menu_button.x = 50

##################
# ABERTURA DO GAME
def change_intro():
    introduction.image = 'screen/opening'

def set_intro():
    global stage
    fuja_sounds.control_music(False, stage)
    if stage == 0:
        fuja_sounds.control_music(True, stage)
        introduction.image = 'logo/cz'
        clock.schedule_unique(change_intro, 4.0)
        title_start_posicion('f')
        title_start_posicion('u')
        title_start_posicion('j')
        title_start_posicion('a')
        clock.schedule_unique(f_final_posicion, 5.0)
        clock.schedule_unique(u_final_posicion, 6.0)
        clock.schedule_unique(j_final_posicion, 7.0)
        clock.schedule_unique(a_final_posicion, 8.0)
        button_start_posicion('start')
        button_start_posicion('menu')
        clock.schedule_unique(start_final_posicion, 8.0)
        clock.schedule_unique(menu_final_posicion, 8.0)

        fuja_menu.start_menu_posicion()