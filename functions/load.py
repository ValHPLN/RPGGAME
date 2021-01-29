import pygame as pg
from constants import player_settings as ps
from constants import tiles_settings as ts
from constants import game_settings as gs
from constants import collisions_settings as cs

def load_tileset():
    #loads tileset
    #gives an Id to each tile in tileset
    #allows us to use Tiled

    # Load Tileset
    img = pg.image.load("img/tilesets/Tileset_Full.png").convert_alpha()
    img_largeur, img_hauteur = img.get_size()  # Prendre les dimensions
    id = 0  # J'initialise les IDs
    for y in range(int(img_hauteur/32)):  # Je parcours les lignes
        for x in range(int(img_largeur/32)):  # Je parcours les colonnes
            rectangle = (x*32, y*32, 32, 32)  # Je divise les tuiles de l'image
            # J'ajoute au dictionnaire des tuiles
            ts.tuiles[str(id)] = img.subsurface(rectangle)
            id += 1  # J'incrémente les IDs
