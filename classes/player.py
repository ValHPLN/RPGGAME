from constants import game_settings as gs, player_settings as ps
import pygame as pg
from constants.sprites import player_sprites
image = player_sprites()

class Player():
    def __init__(self, x, y):

        self.sprite = None #initialises PLayer
        self.free = True #is player busy
        #player hitbox (TODO: create collisions file)
        #self.hitbox = col.Hitbox("Player")
        #self.hitbox = col.Hitbox("object")
        self.health = 10 #player health
        self.hurt = False #player hurt state
        #self.hitbox.rect = pg.Rect((0,0),(25,20)) #creat rect on player feet for collisions
        #self.hitbox.rect.center = gs.center_WIDTH, gs.center_HEIGHT
        self.x = x
        self.y = y

#charges sprites for the player
#image 0=standing 1=down 2=up 3=left 4=right

    def player_controls(self):
        global x
        global y
        global move_up
        global move_left
        global move_down
        global move_right
        global vel
        # Controls (Arrow keys or ZQSD)
        userInput = pg.key.get_pressed()
        if userInput[pg.K_LEFT] or userInput[pg.K_q]:
            ps.x -= ps.vel
            ps.move_left = True
            ps.move_right = False
            ps.move_up = False
            ps.move_down = False
        elif userInput[pg.K_RIGHT] or userInput[pg.K_d]:
            ps.x += ps.vel
            ps.move_left = False
            ps.move_right = True
            ps.move_up = False
            ps.move_down = False
        elif userInput[pg.K_UP] or userInput[pg.K_z]:
            ps.y -= ps.vel
            ps.move_left = False
            ps.move_right = False
            ps.move_up = True
            ps.move_down = False
        elif userInput[pg.K_DOWN] or userInput[pg.K_s]:
            ps.y += ps.vel
            ps.move_left = False
            ps.move_right = False
            ps.move_up = False
            ps.move_down = True
        else:
            ps.move_left = False
            ps.move_right = False
            ps.move_up = False
            ps.move_down = False
            ps.stepIndex = 0

    def player_anim(self):
        global stepIndex
        global lastKey
        global win
        #player animation
        if ps.stepIndex >= 36:
            ps.stepIndex = 0
        if ps.move_left:
            gs.win.blit(image[3][ps.stepIndex//10], (ps.x, ps.y))
            ps.stepIndex += 1
            ps.lastKey = "Left"
        elif ps.move_right:
            gs.win.blit(image[4][ps.stepIndex//10], (ps.x ,ps.y))
            ps.stepIndex += 1
            ps.lastKey = "Right"
        elif ps.move_down:
            gs.win.blit(image[1][ps.stepIndex//10], (ps.x ,ps.y))
            ps.stepIndex += 1
            ps.lastKey = "Down"
        elif ps.move_up:
            gs.win.blit(image[2][ps.stepIndex//10], (ps.x ,ps.y))
            ps.stepIndex += 1
            ps.lastKey = "Up"
        else:
            # Displays the image corresponding to the direction the character is facing
            if ps.lastKey is None or ps.lastKey == "Down":
                gs.win.blit(image[0][0], (ps.x, ps.y))
            if ps.lastKey == "Up":
                gs.win.blit(image[0][3], (ps.x, ps.y))
            if ps.lastKey == "Left":
                gs.win.blit(image[0][1], (ps.x, ps.y))
            if ps.lastKey == "Right":
                gs.win.blit(image[0][2], (ps.x, ps.y))


