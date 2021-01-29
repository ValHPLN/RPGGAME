import pygame as pg
import random as rd
from constants import game_settings as gs, player_settings as ps
from constants import entity_settings as es
from classes import objects
from functions import game


class Entity(): #creates a class for all entities (NPC and objects will inherit it)

    def __init__(self, type=None, id=None, parametre=None):
        self.game = None
        self.pos_last_cam = [gs.map.x_camera, gs.map.y_camera]
        self.position = [gs.map.x_camera, gs.map.y_camera]
        self.id = id
        self.taille = [1, 1]
        self.count = 0
        self.action_count = 0
        self.frame = 5
        self.sprite = None
        self.direction = "down"
        self.mouvement = "base"
        self.free = True
        self.compteur = 0
        self.map = "MapHeticV2"

        self.type = type
        self.id = id
        self.param = parametre

        self.touch = False

    def bouger_hitbox(self, coord):
        #Handles hitbox
        if self.type != "npc":
            if not self.touch: #if no collision with object
                self.hitbox.rect = pg.Rect((self.position[0] + coord[0] + self.taille[0] / 2 - 46,
                                            self.position[1] + coord[1] + self.taille[1] / 2 - 45), (10, 10))
                self.hitbox.mask = pg.Mask((10, 10))
            else: # if collision
                self.hitbox.rect = pg.Rect((0, 0), (0, 0))
                self.hitbox.mask = pg.Mask((0, 0))

        if self.type == "npc":
            self.hitbox.rect = pg.Rect((self.position[0] + coord[0] + self.taille[0]/2 - 56,
                                                            self.position[1] + coord[1] + self.taille[1]/2 - 10), (56, 32))
            self.hitbox.mask = pg.Mask((25, 20))
        self.hitbox.mask.fill()  # fills hitbox

    def deplacement(self):
        #Defines NPC movement
        if self.hitbox.mask is None:  # if there's no hitbox defined
            return  # return
        if self.action_count >= len(es.timings[self.map][self.type][self.id]["pathChar"]): # reinit action count
            self.action_count = 0

        #Loads movement according to map, entity type and id; "patchar" refers to trajectory
        #action = es.deplacement["base"][self.action_count]
        action = es.timings[self.map][self.type][self.id]["pathChar"][self.action_count]
        self.mouvement = "walk"

        if es.timings[self.map][self.type][self.id]["walk"] == None:
            self.mouvement = "base"
            return


        self.direction = action

        #Calcul du delta de la camera entre deux frame
        delta_x = gs.map.x_camera - self.pos_last_cam[0] # Delta camera x
        delta_y = gs.map.y_camera - self.pos_last_cam[1] # Delta camera y

        if self.type != "npc":
            deplacement_x = 0  # en x
            deplacement_y = 0  # en y


        if self.type == "npc":
            self.direction = action
            # movement value in pixels
            deplacement_x = es.action[action][0]  # en x
            deplacement_y = es.action[action][1]  # en y

        # gets position of next movement
        x = self.position[0] + delta_x + deplacement_x
        y = self.position[1] + delta_y + deplacement_y

        # moves hitbox to position
        self.bouger_hitbox((deplacement_x, deplacement_y))

        if self.type != "npc": #if entity is NOT a npc (means: if it's an object)
            self.position[0] = x  # x position
            self.position[1] = y  # y position
            if self.hitbox.collision("player"):  # if it collides with player
                #print(self.id)
                #Adds corresponding item to inventory
                if self.id == "glasses":
                    objects.glassesNb = 1
                    game.inventory.addItemInv(objects.glasses)
                elif self.id == "cable":
                    objects.cableNb = 1
                    game.inventory.addItemInv(objects.cable)
                elif self.id == "coin":
                    objects.coinNb = 1
                    game.inventory.addItemInv(objects.coin)

                else:
                    pass
                self.touch = True


        if self.type == "npc": # if entity is a NPC
            #print(gs.displayE2)

            #This bloc is here to set up a var that enables speech with npcs
            if gs.displayE2:
                gs.OK1 = True
            if gs.displayE2:
                gs.OKindex = gs.OKnb
                #print(gs.OKindex)
            if gs.OK1 and gs.displayE2 is False:
                gs.OKnb = gs.OKnb + 1
                if gs.OKnb > 10:
                    gs.displayE2 = False
                    gs.OKnb = 0
                    gs.OKwin = False
                    gs.OK1 = False
            if gs.OKnb == gs.OKindex and gs.displayE2:
                gs.OKnb = 0
                gs.OKwin = True
                #print("win")

            if gs.OKwin: #Key to talk to NPCs
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_e :
                            game.reset_display()
                            game.speech2(gs.npcId, gs.npcX, gs.npcY)
                            gs.OK1 = False
                    elif event.type == pg.QUIT:
                        pg.quit()
                        quit()

            if self.hitbox.collision("player"):  # if collison with NPC
                gs.displayE2 = True
                self.position[0] = x - deplacement_x  # gets x pos
                self.position[1] = y - deplacement_y  # gets y pos
                self.mouvement = "base"
                self.direction = action
                img = pg.image.load("img/keyE.png")
                gs.win.blit(img, (self.position[0] - 27, self.position[1] - 42)) #displays the "E" bubble
                gs.npcId = self.id #saves id of the npc in Game settings (to display a different speech for each npc that you collide with)
                gs.npcX = (self.position[0] - 200) #saves npc position so the bubble is always on top of the right npc
                gs.npcY = (self.position[1] - 140)
            else:
                # updates position and doesn't display "E" bubble
                self.position[0] = x  # en x
                self.position[1] = y  # en y
                gs.displayE2 = False



        self.bouger_hitbox((-deplacement_x, -deplacement_y))

        # update camera
        self.pos_last_cam = [gs.map.x_camera, gs.map.y_camera]

    def actualiser_frame(self):
        # Loads current movement

        mouvement = es.timings[self.map][self.type][self.id][self.mouvement]

        # if Npc is not moving
        if mouvement[0] is None :
            #self.compteur = 0
            #self.frame = 5
            self.mouvement = "walk"
        else:
            # if npc is moving, increments animations
            if self.compteur < mouvement[0]:
                self.compteur = self.compteur + 1
            else :
                # increments frames
                self.compteur = 0
                if self.frame < mouvement[1]:
                    self.frame = self.frame + 1
                else:
                    # checks if entity is free afterwards
                    self.frame = 0
                    self.libre = mouvement[2]
                    #if movement set to "random" - (but we didn't actually put anything random because that would result in messy collisions)
                    if self.type_deplacement == "aleatoire":
                        self.action_count = rd.randint(0,3)
                    else :
                        self.action_count +=1

                    if mouvement[3]:  #back to base
                        self.mouvement = "base"

    def display(self):
        #Displays NPC and handle animation

        self.actualiser_frame()
        self.bouger_hitbox((0, 0))
        x = self.position[0]
        y = self.position[1]

        # Centers sprite
        x_rendu = x - ps.sprite_height / 2  # X
        y_rendu = y - ps.sprite_width / 2  # Y
        direction = ["right", "up", "left", "down"]
        numero = [0, 1, 2, 3, 4, 5]


        chosenPnj = es.timings[self.map][self.type][self.id]["pathFile"]

        if self.type != "npc" and self.touch == False:
            img = pg.image.load(chosenPnj)
            gs.win.blit(img, (x_rendu, y_rendu))
            self.mouvement = "base"

        if self.type == "npc":
            sprite_set = pg.image.load(chosenPnj)
            sprites = []
            for i in range(24):
                sprites.append(sprite_set.subsurface([i * 32, 0, 32, 64]))

            if self.direction == "still":
                indexDirection = direction.index(es.timings[self.map][self.type][self.id]["stillOrientation"])
            else:
                indexDirection = direction.index(self.direction)
            indexNumero = numero.index(self.frame)
            index = indexDirection * 6 + indexNumero

            for i, s in enumerate(sprites):
                if i == index:
                    gs.win.blit(s, (x_rendu, y_rendu))


