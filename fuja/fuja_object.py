from pgzero.actor import Actor

import random

#############
# DESPERTADOR
alarm_clock = Actor('object/alarm_clock_01')
fps_alarm_clock = 0

########################
# INSERIR DESPERTADOR
def set_alarm_clock():
    alarm_clock.x = random.randint(200, 600)
    alarm_clock.y = random.randint(200, 400)

#################
# ESCONDER DESPERTADOR
def hide_alarm_clock():
    alarm_clock.x = -1000
    return alarm_clock

#########################
# ANIMAÇÃO DO DESPERTADOR
def animate_alarm_clock():
    global fps_alarm_clock
    fps_alarm_clock += 1

    if fps_alarm_clock >= 5:
        if alarm_clock.image == 'object/alarm_clock_01':
            alarm_clock.image = 'object/alarm_clock_02'
            fps_alarm_clock = 0
        elif alarm_clock.image == 'object/alarm_clock_02':
            alarm_clock.image = 'object/alarm_clock_03'
            fps_alarm_clock = 0
        elif alarm_clock.image == 'object/alarm_clock_03':
            alarm_clock.image = 'object/alarm_clock_04'
            fps_alarm_clock = 0
        else:
            alarm_clock.image = 'object/alarm_clock_01'
            fps_alarm_clock = 0

#########################
# CONTADOR DE DESPERTADOR
alarm_clock_points = []

def clock_point(quantidade):
    for i in range(quantidade):
        clock_point = Actor('object/alarm_clock_01')
        clock_point.x = i * 50 + 95
        clock_point.y = 580
        alarm_clock_points.append(clock_point)
        quantidade += 1


