from constants import game_settings as gs
from constants import tiles_settings as ts
from constants import collisions_settings as cs
from constants import entity_settings as es
from classes import collision as col
from classes import npcs
import pygame as pg

class Map:

    def __init__(self, nom, camera=(0, 0), musique=None):

        self.compteur = 0  #can be used for animated map tiles (we didn't have enough time for that)
        x, y = camera  # get camera position in class parameters
        self.nom = nom  # map name
        self.x_camera = x  # Camera X
        self.y_camera = y  # Camera Y
        self.matrices = {  # Dict for all matrixes (layers)
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: []
        }
        self.charger_matrice()  # Loads matrix
        # matrix 0 is used to split the map in rows and columns
        self.x = len(self.matrices[0][0])  # columns var
        self.y = len(self.matrices[0])  # rows var
        # background (pg.SCRALPHA for transparency)
        self.arriere_plan = pg.Surface((self.x * 32, self.y * 32),
                                       pg.SRCALPHA)  # map sized surface
        # foreground
        self.premier_plan = pg.Surface((self.x * 32, self.y * 32),
                                       pg.SRCALPHA)  # map sized surface

        self.charger_hitboxs()  # loads hitboxes
        self.charger_images()  # loads background/foreground
        self.afficher_arriere_plan()

    def afficher_arriere_plan(self):
        #displays background layers
        gs.win.blit(self.arriere_plan, (self.x_camera,
                                          self.y_camera))

    def afficher_premier_plan(self):
        #displays foreground layers
        gs.win.blit(self.premier_plan, (self.x_camera,
                                          self.y_camera))

    def bouger_hitbox(self, x, y):
        #moves collision hitbox, when player/camera moves
        # nouvelle_liste va écraser la liste des constantes de collision pour les tuiles
        for hitbox in cs.groups["tuile"]:  # goes through group
            hitbox.rect.move_ip(x, y)  # moves rect
        for hitbox in cs.groups["object"]:  # goes through group
            hitbox.rect.move_ip(x, y)  # moves rect

    def bouger(self, x, y):
        #moves tiles as the camera moves
        gs.map.x_camera += x
        gs.map.y_camera += y

    def charger_matrice(self):
        #loads matrixes and allows game to use .csv files
        for i in range(10):  # goes through all layers
            nom_fichier = "maps/" + self.nom + "_" + str(i) + ".csv"  # filename
            #                                          # Ex: MapHeticV2_0.csv
            f = open(nom_fichier, "r")    # opens file
            for ligne in f.readlines():   # for loop to check every line
                ligne = ligne.replace("\n", "")  # deletes line break
                ligne = ligne.split(",")  # changes line to list
                if ligne != []:
                    self.matrices[i].append(ligne)  # adds list to matrixes
            f.close()

    def charger_hitboxs(self):
        #creates hitboxes for map tiles
        for groupe in cs.groups:  # goes through all groups
            cs.groups[groupe] = pg.sprite.Group()  # reinit groups

        for i in range(10):  #goes through matrixes
            for y in range(self.y):  # columns
                for x in range(self.x):  # rows
                    if self.matrices[i][y][x] in ts.tuiles:  # if tile exists in tile settings
                        if self.matrices[i][y][x] in ts.collisions:  # if collisions
                            x_tuile = self.x_camera + x*32  # X pos
                            y_tuile = self.y_camera + y*32  # Y pos
                            tuile = ts.tuiles[self.matrices[i][y][x]]  # Get img
                            mask = pg.mask.from_surface(tuile)  # creates mask
                            rect = pg.Rect(x_tuile, y_tuile, 32, 32)  # gets rect from img
                            col.Hitbox("tuile", rect, mask)  # saves list

    def vider_monstres(self):
        #clears all entities from the map when we change it (we didn't have the chance to created another map so it's unused for now)
        gs.entities_list = []

    def load_npc(self):
        #Loads npcs
        liste_type = []
        liste_npcs = []

        for add_type in es.timings[self.nom]:
            for add_id in es.timings[self.nom][add_type]:
                for add_value in es.timings[self.nom][add_type][add_id]["init"]:
                    npcss = npcs.Npc(add_type, add_id, add_value)
                    gs.entities_list.append(npcss)

        for npc in gs.entities_list:
            npc.deplacement()
            npc.display()

    def charger_images(self):
        #loads layers in background and foreground vars

        for i in range(10):  # Je parcours les couches
            for y in range(self.y):  # Parcours les colonnes
                for x in range(self.x):  # Je parcours les lignes
                    if self.matrices[i][y][x] in ts.tuiles:  # Si elle existe
                        tuile = ts.tuiles[self.matrices[i][y][x]]  # Gets tile from dict
                        if i < 5:  # Goes through layers
                            self.arriere_plan.blit(tuile, (x*32, y*32))  # blits every tile on the background
                        else:
                            self.premier_plan.blit(tuile, (x*32, y*32))  # blits every tile on the foreground
