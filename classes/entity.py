import pygame as pg
import random as rd
from constants import game_settings as gs, player_settings as ps
from constants import entity_settings as es
from constants import collisions_settings as cs
from classes import collision as col, objects
from classes.inventory import Inventory
from constants.game_settings import speech
from functions import game


class Entity():

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
            if not self.touch: #si l'objet n'est pas touché
                self.hitbox.rect = pg.Rect((self.position[0] + coord[0] + self.taille[0] / 2 - 46,
                                            self.position[1] + coord[1] + self.taille[1] / 2 - 45), (10, 10))
                self.hitbox.mask = pg.Mask((10, 10))
            else: #si l'objet est touché
                self.hitbox.rect = pg.Rect((0, 0), (0, 0))
                self.hitbox.mask = pg.Mask((0, 0))

        if self.type == "npc":
            self.hitbox.rect = pg.Rect((self.position[0] + coord[0] + self.taille[0]/2 - 56,
                                                            self.position[1] + coord[1] + self.taille[1]/2 - 10), (56, 32))
            self.hitbox.mask = pg.Mask((25, 20))
        self.hitbox.mask.fill()  # Remplir le hitbox pour créer un bloc

    def deplacement(self):
        #Defines NPC movement
        if self.hitbox.mask is None:  # Si le hitbox est pas défini
            return  # Quitter la fonction pour éviter un déplacement précoce

        if self.action_count >= len(es.timings[self.map][self.type][self.id]["pathChar"]): # On reinitialise le compteur d'action
            self.action_count = 0

        # Charge le type deplacement
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
            #Donne la valeur des deplacement ex: + 4 px
            deplacement_x = es.action[action][0]  # en x
            deplacement_y = es.action[action][1]  # en y

        # Donne la position du prochain déplacement
        x = self.position[0] + delta_x + deplacement_x
        y = self.position[1] + delta_y + deplacement_y

        # On bouge le hitbox a cette emplacement
        self.bouger_hitbox((deplacement_x, deplacement_y))

        if self.type != "npc":
            self.position[0] = x  # en x
            self.position[1] = y  # en y
            if self.hitbox.collision("player"):  # S'il n'y a pas:
                print(self.id)
                if self.id == "glasses":
                    objects.glassesNb = 1
                    game.inventory.addItemInv(objects.glasses)
                elif self.id == "cable":
                    game.inventory.addItemInv(objects.cable)
                elif self.id == "coin1" or "coin2" or "coin3":
                    game.inventory.addItemInv(objects.hp_potion)

                else:
                    pass
                self.touch = True


        if self.type == "npc":
            #print(gs.displayE2)
            if gs.displayE2:
                gs.OK1 = True
            if gs.displayE2:
                gs.OKindex = gs.OKnb
                print(gs.OKindex)
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

            if gs.OKwin:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_e :
                            game.reset_display()
                            game.speech2(gs.npcId, gs.npcX, gs.npcY)
                            gs.OK1 = False

            if self.hitbox.collision("player"):  # S'il y en a :
                gs.displayE2 = True
                self.position[0] = x - deplacement_x  # en x
                self.position[1] = y - deplacement_y  # en y
                self.mouvement = "base"
                self.direction = action
                if self.direction == "still":
                    img = pg.image.load("img/keyE_red.png")
                else:
                    img = pg.image.load("img/keyE.png")
                gs.win.blit(img, (self.position[0] - 27, self.position[1] - 42))
                gs.npcId = self.id
                gs.npcX = (self.position[0] - 200)
                gs.npcY = (self.position[1] - 140)
            else:
                # On actualise les position
                self.position[0] = x  # en x
                self.position[1] = y  # en y
                gs.displayE2 = False



        self.bouger_hitbox((-deplacement_x, -deplacement_y))

        # On actualise la camera
        self.pos_last_cam = [gs.map.x_camera, gs.map.y_camera]

    def actualiser_frame(self):
        # charge attribut mouvement en cours

        mouvement = es.timings[self.map][self.type][self.id][self.mouvement]

        # Si le monstre est immobile, retour des conteurs à 0
        if mouvement[0] is None :
            #self.compteur = 0
            #self.frame = 5
            self.mouvement = "walk"
        else:
            # Maintenant on incrémente le compteur des animations si besoin
            if self.compteur < mouvement[0]:
                self.compteur = self.compteur + 1
            else :
                # On incremente le compteur de frame si besoins
                self.compteur = 0
                if self.frame < mouvement[1]:
                    self.frame = self.frame + 1
                else:
                    # verifi si on libere l'entitée apres l'animation et reset frame
                    self.frame = 0
                    self.libre = mouvement[2]
                    # une fois l'animation terminer, on efectue l'action suivante
                    if self.type_deplacement == "aleatoire":
                        self.action_count = rd.randint(0,3)
                    else :
                        self.action_count +=1

                    if mouvement[3]:  # Si on veux revenir
                        self.mouvement = "base"        # Sur base, on le fait

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


