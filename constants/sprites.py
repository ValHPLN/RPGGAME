import pygame as pg
import os
from constants import tiles_settings as ts
from .game_settings import *

# Assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "../img")





def player_sprites():
    image = []

    # Stationary sprites
    standing = [pg.image.load(os.path.join(img_folder, "char", "char_face_down.png")),
                pg.image.load(os.path.join(img_folder, "char", "char_face_left.png")),
                pg.image.load(os.path.join(img_folder, "char", "char_face_right.png")),
                pg.image.load(os.path.join(img_folder, "char", "char_face_up.png"))]

    image.append(standing)

    # Removes black background from images
    for frame in standing:
        frame.set_colorkey(BLACK)

    # Animation sprites

    down = [pg.image.load(os.path.join(img_folder, "char", "char_walk_down1.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_down2.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_down3.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_down4.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_down5.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_down6.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_down7.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_down8.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_down9.png"))]

    image.append(down)

    for frame in down:
        frame.set_colorkey(BLACK)

    up = [pg.image.load(os.path.join(img_folder, "char", "char_walk_up1.png")),
          pg.image.load(os.path.join(img_folder, "char", "char_walk_up2.png")),
          pg.image.load(os.path.join(img_folder, "char", "char_walk_up3.png")),
          pg.image.load(os.path.join(img_folder, "char", "char_walk_up4.png")),
          pg.image.load(os.path.join(img_folder, "char", "char_walk_up5.png")),
          pg.image.load(os.path.join(img_folder, "char", "char_walk_up6.png")),
          pg.image.load(os.path.join(img_folder, "char", "char_walk_up7.png")),
          pg.image.load(os.path.join(img_folder, "char", "char_walk_up8.png")),
          pg.image.load(os.path.join(img_folder, "char", "char_walk_up9.png"))]

    image.append(up)

    for frame in up:
        frame.set_colorkey(BLACK)

    left = [pg.image.load(os.path.join(img_folder, "char", "char_walk_left1.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_left2.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_left3.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_left4.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_left5.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_left6.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_left7.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_left8.png")),
            pg.image.load(os.path.join(img_folder, "char", "char_walk_left9.png"))]

    image.append(left)

    for frame in left:
        frame.set_colorkey(BLACK)

    right = [pg.image.load(os.path.join(img_folder, "char", "char_walk_right1.png")),
             pg.image.load(os.path.join(img_folder, "char", "char_walk_right2.png")),
             pg.image.load(os.path.join(img_folder, "char", "char_walk_right3.png")),
             pg.image.load(os.path.join(img_folder, "char", "char_walk_right4.png")),
             pg.image.load(os.path.join(img_folder, "char", "char_walk_right5.png")),
             pg.image.load(os.path.join(img_folder, "char", "char_walk_right6.png")),
             pg.image.load(os.path.join(img_folder, "char", "char_walk_right7.png")),
             pg.image.load(os.path.join(img_folder, "char", "char_walk_right8.png")),
             pg.image.load(os.path.join(img_folder, "char", "char_walk_right9.png"))]

    image.append(right)

    for frame in right:
        frame.set_colorkey(BLACK)

    return image
