import pygame as pg

tuiles = {}

groupes = {
    "tuile": pg.sprite.Group(),     # Liste des hitboxs pour les tuiles
    "Player": pg.sprite.Group(),
    "object": pg.sprite.Group(),
    "tout": pg.sprite.Group()
}

collisions = (  # Liste des blocs sur lesquels on ne peux pas aller
    "7138",
    "7139",
    "7142",
    "7145",
    "7158",
    "7169",
    "7225"
)