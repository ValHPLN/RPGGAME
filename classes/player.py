from constants import game_settings as gs, player_settings as ps
from constants import collisions_settings as cs
from classes import collision as col
import pygame as pg


def text_format(message, textFont, textSize, textColor):
    newFont = pg.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText


class Player():
    def __init__(self, randomPlayer, hp):

        self.randomPlayer = "img/char/New/" + randomPlayer + "_run_32x32.png"
        self.sprite = None #initialises PLayer
        self.free = True #is player busy
        self.count = 0
        self.frame = 0
        self.direction = "up"
        self.mouvement = "base"
        self.hitbox = col.Hitbox("player")
        self.hitbox_object = col.Hitbox("object")
        self.health = gs.base_hp #player health
        self.hurt = False #player hurt state
        self.hitbox.rect = pg.Rect((0,0),(56,0)) #creat rect on player feet for collisions
        self.hitbox.rect.center = (gs.center_WIDTH, gs.center_HEIGHT+13)
        self.hitbox.mask = pg.Mask((25,20))
        self.hitbox.mask.fill()

        #creat rect on player feet for collisions
        self.hitbox_object.rect = pg.Rect((gs.center_WIDTH - 20, gs.center_HEIGHT + 10), (32, 22))
        self.hitbox_object.rect.center = (gs.center_WIDTH - 4, gs.center_HEIGHT - 11)
        self.hitbox_object.mask = pg.Mask((32, 22))
        self.hitbox_object.mask.fill()  # fills hitbox


    def player_controls(self):
        # Controls (Arrow keys or ZQSD)
        userInput = pg.key.get_pressed()
        if not self.free:
            return
        if self.hitbox.mask is None:
            return
        for key in ps.keys:  # Gets Keys
            if userInput[key]:
                key = ps.keys[key]

                # ([0]: X, [1]: Y ,[2]: direction ,[3] movement ,[4] state of player)
                if key[2] is not None:   #if animation changes direction:
                    self.direction = key[2]  # changes direction of the player
                if self.mouvement != key[3]:  # if the movement changes
                    self.mouvement = key[3]  # Changer le mouvement du perso
                    self.compteur = 0  # start animation all over again
                    self.frame = 0  # reinit frames
                self.free = key[4]  # change state (free : true/false)

                # gets movement in pixels
                x = key[0]  # number of x pixels
                y = key[1]  # number of y pixels
                # moves hitbox
                gs.map.bouger_hitbox(x, y)
                if self.hitbox.collision("tuile"):  # if player collides with tiles dict (this dict defines the tiles where the player can't walk)
                    # then cancel movement
                    gs.map.bouger_hitbox(-x, -y)
                else:  # if no collision, player can move
                    gs.map.bouger(x, y)


                break

        else:  # if no userinput, puts player at rest on base position
            self.free = True
            self.mouvement = "base"
            self.frame = 3


    def actualiser_frame(self):
        # Updates animation frames with ticks
        # Checks how many frames there are between each tick
        if ps.timing[self.mouvement][0] is None:  # if None
            self.compteur = 0
            self.frame = 5
        else:  # if there are
            # increments animation counter
            if self.compteur < ps.timing[self.mouvement][0]:
                self.compteur = self.compteur + 1
                # if it reaches max
            else:
                self.compteur = 0  # reset
                # increments frames
                if self.frame < ps.timing[self.mouvement][1]:
                    self.frame = self.frame + 1
                    # if max
                else:
                    self.frame = 0  # Reset
                    self.libre = ps.timing[self.mouvement][2]  # free char
                    if ps.timing[self.mouvement][3]:
                        self.mouvement = "base"  # back to "base"


    def actualiser_sprite(self):
        #updates frame according to direction, movement, frame
        cs.groups["player"] = [self.hitbox]


    def update(self):
      #updates player sprites and settings
        self.actualiser_frame()
        self.actualiser_sprite()

        # centers sprite
        x_rendu = gs.center_WIDTH - ps.sprite_height / 2
        y_rendu = gs.center_HEIGHT - ps.sprite_width / 2

        direction = ["right", "up", "left", "down"]
        numero = [0, 1, 2, 3, 4, 5]

        sprite_set = pg.image.load(self.randomPlayer)
        sprites = []
        for i in range(24):
            sprites.append(sprite_set.subsurface([i * 32, 0, 32, 64]))

        indexDirection = direction.index(self.direction)
        indexNumero = numero.index(self.frame)
        index = indexDirection * 6 + indexNumero

        for i, s in enumerate(sprites):
            if i == index:
                gs.win.blit(s, (x_rendu, y_rendu))



