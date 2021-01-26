import pygame as pg

groups = {
    "tuile": pg.sprite.Group(),     # Liste des hitboxs pour les tuiles
    "entity": pg.sprite.Group(),   # Liste des hitboxs pour les entiees
    "player": pg.sprite.Group(),    # Liste des hitboxs pour les joueurs
    "Npc": pg.sprite.Group(),   # Liste des hitboxs pour les pnj
    "object": pg.sprite.Group(),     # Liste des hitboxs pour les objets
    "tout": pg.sprite.Group()       # Liste des hitboxs pour tout
}