import pygame as pg
from constants import collisions_settings as cs


class Hitbox(pg.sprite.Sprite):  # La classe Hitbox hérite de pg.sprite.Sprite CAD qu'elle inclut les caracteristiques de pg.sprite.Sprite

    def __init__(self, groupe, rect=None, mask=None):
        """Creates collision Hitbox,
        with Img, Rect and Hitbox,
        Default is None,
        Groups : player, tuile, object, etc...
        All hitboxs are saved in collisions_settings
        """
        super().__init__()  # Initialisation de pg.sprite.Sprite
        # Ici "super()" fait référence a la classe mère (pg.sprite.Sprite ici)
        self.rect = rect    # Rectangle de la hitbox
        self.mask = mask    # "Mask" qui correspond au hitbox des collisions
        cs.groups["tout"].add(self)  # Ajouter a la liste de tout les hitboxs
        cs.groups[groupe].add(self)  # Ajouter a la liste correspondante

    def collision(self, groupe="tout"):
        """Checks collisions with a group
        Default is None
        Returns True if collision
        Returns False if there's no collision
        """
        # Retourne le boolean fourni par la fonction qui Permets
        # De vérifier si il y a des collisions entre 1 hitbox et 1 groupe
        # De hitbox. pg.sprite.collide_mask signifie que l'on veut utiliser
        # les hitboxs
        return pg.sprite.spritecollideany(self, cs.groups[groupe], pg.sprite.collide_mask)
