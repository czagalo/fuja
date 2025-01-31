from pgzero.builtins import sounds

import fuja_intro

music = True
sfx = True

stage = fuja_intro.stage

#################
# MÚSICAS DO GAME
def control_music(tf, s):
    global stage, music
    music = tf
    stage = s

    if stage == 0 and music == True:
        sounds.start_music.play()
    elif stage == 0 and music == False:
        sounds.start_music.stop()

    if stage == 1 and music == True:
        sounds.lost.play()
    elif stage == 1 and music == False:
        sounds.lost.stop()

    if stage == 2 and music == True:
        sounds.lost.play()
    elif stage == 2 and music == False:
        sounds.lost.stop()

    if stage == 3 and music == True:
        sounds.fear.play()
    elif stage == 3 and music == False:
        sounds.fear.stop()

    if stage == 4 and music == True:
        sounds.fear.play()
    elif stage == 4 and music == False:
        sounds.fear.stop()
    
    if stage == 5 and music == True:
        sounds.hopeless.play()
    elif stage == 5 and music == False:
        sounds.hopeless.stop()

    if stage == 6 and music == True:
        sounds.despair.play()
    elif stage == 6 and music == False:
        sounds.despair.stop()


"""
    if stage == 2 and music == True:
        sounds.hopeless.play()
    elif stage == 2 and music == False:
        sounds.hopeless.stop()
    
    if stage == 3 and music == True:
        sounds.dance_of_despair.play()
    elif stage == 3 and music == False:
        sounds.dance_of_despair.stop()

    if stage == 4 and music == True:
        sounds.fear.play()
    elif stage == 4 and music == False:
        sounds.fear.stop()
"""
#################
# SFX DO GAME
def control_sfx(tf, c):
    global sfx
    sfx = tf
    if sfx == False:
        sounds.click.stop()
        sounds.walk.stop()
        sounds.tic_tac.stop()
        sounds.alarm_clock.stop()
        sounds.happy.stop()
        sounds.death.stop()
        sounds.funebre.stop()
    
    if sfx == True:
        if c == 'click':
            sounds.click.play()
        if c == 'pc_walk':
            sounds.walk.play()
        if c == 'tic_tac':
            sounds.tic_tac.play()
        if c == 'alarm_clock':
            sounds.alarm_clock.play()
        if c == 'happy':
            sounds.happy.play()
        if c == 'death':
            sounds.death.play()
        if c == 'funebre':
            sounds.funebre.play()
    
    #print(sfx)