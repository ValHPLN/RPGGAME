import pygame as pg

groups = {
    "tuile": pg.sprite.Group(),     # Liste des hitboxs pour les tuiles
    "entity": pg.sprite.Group(),   # Liste des hitboxs pour les entiees
    "player": pg.sprite.Group(),    # Liste des hitboxs pour les joueurs
    #"Monstre": pg.sprite.Group(),   # Liste des hitboxs pour les ennemis
    "object": pg.sprite.Group(),     # Liste des hitboxs pour les objets
    "pnj": pg.sprite.Group(),       # Liste des hitboxs pour les personnages non joueurs
    "tout": pg.sprite.Group()       # Liste des hitboxs pour tout
}