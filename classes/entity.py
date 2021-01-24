import pygame as pg
import random as rd
from constants import game_settings as gs, player_settings as ps
from constants import entity_settings as es
from constants import collisions_settings as cs
from classes import collision as col

class Entity():

    def __init__(self, id=None):
        self.pos_last_cam = [gs.map.x_camera, gs.map.y_camera]
        self.position = [gs.map.x_camera, gs.map.y_camera]
        print(id)
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

        identifier = self.id.split("_",1)
        self.type = identifier[0]
        self.id = identifier[1]



    def bouger_hitbox(self, coord):
        """ Gere le mouvement de la hitbox
        """
        #self.hitbox.rect = self.sprite.get_rect(center=(self.position[0] + coord[0] + self.taille[0]/2 - 56,
        #                                                self.position[1] + coord[1] + self.taille[1]/2))
        self.hitbox.rect = pg.Rect((self.position[0] + coord[0] + self.taille[0]/2 - 56,
                                                        self.position[1] + coord[1] + self.taille[1]/2 - 10), (56, 32))
        self.hitbox.mask = pg.Mask((25, 20))
        self.hitbox.mask.fill()  # Remplir le hitbox pour créer un bloc

    def deplacement(self):
        """ Défini le mouvement de base
        pour une entitée la fait tourner sur elle meme
        """
        if self.hitbox.mask is None:  # Si le hitbox est pas défini
            return  # Quitter la fonction pour éviter un déplacement précoce

        if self.action_count >= len(es.timings[self.type][self.id]["pathChar"]): # On reinitialise le compteur d'action
            self.action_count = 0

        # Charge le type deplacement
        #action = es.deplacement["base"][self.action_count]
        action = es.timings[self.type][self.id]["pathChar"][self.action_count]
        self.mouvement = "walk"
        self.direction = action

        #Calcul du delta de la camera entre deux frame
        delta_x = gs.map.x_camera - self.pos_last_cam[0] # Delta camera x
        delta_y = gs.map.y_camera - self.pos_last_cam[1] # Delta camera y

        #Donne la valeur des deplacement ex: + 4 px
        deplacement_x = es.action[action][0]  # en x
        deplacement_y = es.action[action][1]  # en y

        # Donne la position du prochain déplacement
        x = self.position[0] + delta_x + deplacement_x
        y = self.position[1] + delta_y + deplacement_y

        # On bouge le hitbox a cette emplacement
        self.bouger_hitbox((deplacement_x, deplacement_y))
        if not self.hitbox.collision("tuile"):  # S'il n'y a pas:

            # On actualise les positon
            self.position[0] = x   #en x
            self.position[1] = y  #en y
        else:
            self.position[0] = x - deplacement_x   #en x
            self.position[1] = y - deplacement_y #en y
            self.mouvement = "base"
            self.direction = action

        self.bouger_hitbox((-deplacement_x, -deplacement_y))

        # On actualise la camera
        self.pos_last_cam = [gs.map.x_camera, gs.map.y_camera]


    def actualiser_frame(self):
        # charge attribut mouvement en cours

        mouvement = es.timings[self.type][self.id][self.mouvement]

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
        """ Procedure qui gere l'affichage de mon personnage
        Gère l'affichage des animations
        """
        self.actualiser_frame()
        #self.actualiser_sprite()
        self.bouger_hitbox((0, 0))
        x = self.position[0]
        y = self.position[1]

        # Je calcule la position de rendu du sprite afin qu'il soit bien centré
        x_rendu = x - ps.sprite_height / 2  # Le x de rendu
        y_rendu = y - ps.sprite_width / 2  # Le y de rendu

        direction = ["right", "up", "left", "down"]
        numero = [0, 1, 2, 3, 4, 5]

        chosenPnj = es.timings[self.type][self.id]["pathFile"]
        sprite_set = pg.image.load(chosenPnj)
        sprites = []
        for i in range(24):
            sprites.append(sprite_set.subsurface([i * 32, 0, 32, 64]))

        indexDirection = direction.index(self.direction)
        indexNumero = numero.index(self.frame)
        index = indexDirection * 6 + indexNumero

        for i, s in enumerate(sprites):
            if i == index:
                gs.win.blit(s, (x_rendu, y_rendu))


