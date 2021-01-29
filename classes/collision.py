import pygame as pg
from constants import collisions_settings as cs


class Hitbox(pg.sprite.Sprite):  # Hitbox class inherits pg.sprite.Sprite

    def __init__(self, groupe, rect=None, mask=None):
        #Creates collision Hitbox,
        #with Img, Rect and Hitbox,
        #Default is None,
        #Groups : player, tuile, object, etc...
        #All hitboxs are saved in collisions_settings
        #
        super().__init__()

        self.rect = rect
        self.mask = mask
        cs.groups["tout"].add(self)  # adds to general hitbox list
        cs.groups[groupe].add(self)  # adds to specific list

    def collision(self, groupe="tout"):
       #Checks collisions with a group
       #Default is None
       #Returns True if collision
       #Returns False if there's no collision
        return pg.sprite.spritecollideany(self, cs.groups[groupe], pg.sprite.collide_mask)
