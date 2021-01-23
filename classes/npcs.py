# -*- coding: utf-8 -*-
"""Objet monstre
Créer des monstres, ennemis.
Auteur : Dorian Voland
"""
import pygame as pg
import random as rd

from constants import game_settings as gs
from constants import entity_settings as ns
from constants import collisions_settings as cs
from classes import entity as ent
from classes import collision as col


class Npc(ent.Entity):
    """ Classe Monstre qui herite de Entite
            redefini methode déplacement() ==> type_deplacement: - aleatoire
                                                                 - base
                                                                 - zone (en cours)
    """
    nb_npc = 0
    def __init__(self, npc_type, parametre):
        """
            * parametre =  [position, taille, type_deplacement, vie, attaque]
        """
        Npc.nb_npc +=1  # On augemente le nombre de monstre
        npc = "npc_" + npc_type  # Préparation du nom du monstre pour l'initialisation
        super(Npc, self).__init__(npc)  # Initialisation de la superclasse
        # Mise en place des différents paramètres..
        x, y = parametre[0]  # Coordonnées relatives a la map
        x += gs.map.x_camera
        y += gs.map.y_camera
        self.position = [x, y]
        self.taille = parametre[1]
        self.type_deplacement = parametre[2]
        #self.vie = parametre[3]
        #self.attaque = parametre[4]
        ################
        self.hitbox = col.Hitbox("Npc")  # Les collisions du monstre
