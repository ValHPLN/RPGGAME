import pygame as pg
import random as rd
from constants import game_settings as gs
from constants import entity_settings as es
from constants import collisions_settings as cs
from classes import collision as col

class Entity():

    def __init__(self, id=None):
        self.pos_last_cam = [gs.map.x_camera, gs.map.y_camera]
        self.position = [gs.map.x_camera, gs.map.y_camera]
        self.id = id
        self.taille=[1,1]
        self.count = 0
        self.action_count = 0
        self.frame = 0
        self.sprite = None
        self.direction = "down"
        self.mouvement = "base"
        self.free = True
        self.type_deplacement = "base"

        self.load_sprite()

    def load_sprite(self):

        identifier = self.id.split("_",1)
        self.type = identifier[0]
        self.id = identifier[1]

        animation = es.animation[self.type][self.id]

        for direction in animation:  # Parcours des directions
            for mouvement in animation[direction]:  # Parcours des move
                number = 0  # Compteur utilisé dans le parcours des sprites
                for sprite in animation[direction][mouvement]:  # sprites
                    if isinstance(sprite, str):  # Si le sprite est un txt
                        img = pg.image.load(sprite).convert_alpha()  # Charger
                        animation[direction][mouvement][number] = img  # Var
                    number += 1  # Numéro du sprite actuel + 1

    def bouger_hitbox(self, coord):
        """ Gere le mouvement de la hitbox
        """
        self.hitbox.rect = self.sprite.get_rect(center=(self.position[0] + coord[0] + self.taille[0]/2,
                                                        self.position[1] + coord[1] + self.taille[1]/2))
        self.hitbox.mask = pg.Mask((self.taille[0], self.taille[1]))
        self.hitbox.mask.fill()  # Remplir le hitbox pour créer un bloc

    def deplacement(self):
        """ Défini le mouvement de base
        pour une entitée la fait tourner sur elle meme
        """
        if self.hitbox.mask is None:  # Si le hitbox est pas défini
            return  # Quitter la fonction pour éviter un déplacement précoce

        if self.action_count >= len(es.deplacement[self.type_deplacement]): # On reinitialise le compteur d'action
            self.action_count = 0

        # Charge le type deplacement
        action = es.deplacement["base"][self.action_count]
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
        if not self.hitbox.collision("player"):  # S'il n'y a pas:

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
            self.compteur = 0
            self.frame = 0
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

    def actualiser_sprite(self):
        #charge les animations du mouvement
        animation = es.animation[self.type][self.id][self.direction][self.mouvement]
        # On prend le bon sprite
        self.sprite = animation[self.frame]
        # On actualise le hitbox
        self.bouger_hitbox((0, 0))


    def display(self):
        """ Procedure qui gere l'affichage de mon personnage
        Gère l'affichage des animations
        """
        self.actualiser_frame()
        self.actualiser_sprite()
        x = self.position[0]
        y = self.position[1]

        # Affiche le sprite
        gs.win.blit(self.sprite, (x, y))