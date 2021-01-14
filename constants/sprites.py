import pygame as pg
import os
from constants import tiles_settings as ts
from .game_settings import *

# Assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "../img")

def map_sprites():
    """Charger un tileset
    Associe a chaque tuiles d'un tileset un ID, divise un tileset
    en plusieurs lignes
    Permets de bosser avec Tiled
    """
    # Charger l'image du tileset
    img = pg.image.load("img/tilesets/Tileset_Full.png").convert_alpha()
    img_largeur, img_hauteur = img.get_size()  # Prendre les dimensions
    id = 0  # J'initialise les IDs
    for y in range(int(img_hauteur/32)):  # Je parcours les lignes
        for x in range(int(img_largeur/32)):  # Je parcours les colonnes
            rectangle = (x*32, y*32, 32, 32)  # Je divise les tuiles de l'image
            # J'ajoute au dictionnaire des tuiles
            ts.tuiles[str(id)] = img.subsurface(rectangle)
            id += 1  # J'incrémente les IDs



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
