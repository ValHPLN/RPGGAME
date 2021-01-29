import pygame as pg

# Player movement speed
vel = 2
run = True
sprite_height = 64
sprite_width = 64
sprite_still = "img/char/char_face_"
sprite_move = "img/char/char_walk_"

keys = {  # move keys
    # [x, y, "direction", "movement", free?]
    # free = is char free ? True/False
    pg.K_UP:    [0, vel, "up", "walk", True],
    pg.K_LEFT:  [vel, 0, "left", "walk", True],
    pg.K_DOWN:  [0, -vel, "down", "walk", True],
    pg.K_RIGHT: [-vel, 0, "right", "walk", True],
    pg.K_z:    [0, vel, "up", "walk", True],
    pg.K_q:  [vel, 0, "left", "walk", True],
    pg.K_s:  [0, -vel, "down", "walk", True],
    pg.K_d: [-vel, 0, "right", "walk", True],
    }

####################################################
timing = {
    "base": [None],
    "walk": [4, 5, True, False],
    }
