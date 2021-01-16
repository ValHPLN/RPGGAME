import pygame as pg
from constants import player_settings as ps
from constants import tiles_settings as ts
from constants import game_settings as gs
from constants import collisions_settings as cs

def load_tileset():
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


def load_sprites():
    """Charge les sprites
    Permets de charger les sprites des différents dictionnaires
    """
    for direction in ps.animation:  # Parcours des directions
        for mouvement in ps.animation[direction]:  # Parcours des mouvements
            numero = 0  # Compteur utilisé dans le parcours des sprites
            for sprite in ps.animation[direction][mouvement]:  # Parcourir images
                if isinstance(sprite, str):  # Si le sprite est un txt
                    img = pg.image.load(sprite).convert_alpha()  # Charger
                    ps.animation[direction][mouvement][numero] = img  # Sauver
                numero += 1  # Numéro du sprite actuel + 1 (Le compteur)