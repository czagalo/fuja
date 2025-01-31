import math

#INSERIR PERSONAGEM DO JOGADOR (PC - PLAYER CHARACTER)
def set_pc():
    pc = 'player/idle/up_01'
    return pc

#INSERIR POSIÇÃO INICIAL DA PC
#Recebe como parâmetros os valores 'y' ou 'x' (pos)
#referente a posição y e x da janela do game
def set_pc_start_posicion(pos):
    y = math.ceil(600 / 2)
    x = math.ceil(800 / 2)

    if pos == 'y':
        return y
    elif pos == 'x':
        return x

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
        else:
            pc = 'player/idle/up_01'
    elif orientation == 'down':
        if pc == 'player/idle/down_01':
            pc = 'player/idle/down_02'
        elif pc == 'player/idle/down_02':
            pc = 'player/idle/down_03'
        else:
            pc = 'player/idle/down_01'
    elif orientation == 'left':
        if pc == 'player/idle/left_01':
            pc = 'player/idle/left_02'
        elif pc == 'player/idle/left_02':
            pc = 'player/idle/left_03'
        else:
            pc = 'player/idle/left_01'
    elif orientation == 'right':
        if pc == 'player/idle/right_01':
            pc = 'player/idle/right_02'
        elif pc == 'player/idle/right_02':
            pc = 'player/idle/right_03'
        else:
            pc = 'player/idle/right_01'

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
        else:
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
        else:
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
        else:
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
        else:
            pc = 'player/run/right_01'

    return pc

#################################
# INSERIR ANIMAÇÃO DA PC MORRENDO
def set_pc_dead(pc):
    if pc == 'dead_pc_01':
        pc = 'dead_pc_02'
    elif pc == 'dead_pc_02':
        pc = 'dead_pc_03'
    elif pc == 'dead_pc_03':
        pc = 'dead_pc_04'
    elif pc == 'dead_pc_04':
        pc = 'dead_pc_05'
    elif pc == 'dead_pc_05':
        pc = 'dead_pc_06'
    elif pc == 'dead_pc_06':
        pc = 'dead_pc_07'
    else:
        pc = 'dead_pc_01'