from constants import game_settings as gs
from constants import tiles_settings as ts
from classes import collision as col
import pygame as pg

class Map:

    def __init__(self, nom, camera=(0, 0), musique=None):

        self.compteur = 0  # Variable du compteur d'animation initialisé à 0
        x, y = camera  # On extrait les coordonnées de la tuple
        self.nom = nom  # Définition du nom de la map
        # On met -x et -y afin d'utiliser des coordonnées positives.
        # En effet la map utilise un repère orthonormé standard partageant son 0 avec le repère pygame.
        # Elle est donc très souvent négative.
        self.x_camera = x  # Camera X (position de la camera en fonction de l'axe des abcysses)
        self.y_camera = y  # Camera Y (position de la camera en fonction de l'ordonnée)
        self.matrices = {  # Dictionnaire des matrices
            0: [],  # Matrice qui stockera le fond
            1: [],  # Matrice qui stockera le milieu
            2: [],  # Matrice qui stockera le 1er plan
            3: [],  # Matrice qui stockera le plan spécial
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: []
        }
        self.charger_matrice()  # Chargement de la matrice, du fichier carte
        # Pour le nombre de colonnes et de lignes on utilise la matrice du fond
        self.x = len(self.matrices[0][0])  # Variable contenant le nombre de colonnes
        self.y = len(self.matrices[0])  # Variable contenant le nombre de lignes
        # Variable contenant l'arrière plan de la map (pg.SCRALPHA permet de rendre la surface transparente)
        self.arriere_plan = pg.Surface((self.x * 32, self.y * 32),
                                       pg.SRCALPHA)  # On crée une surface de la taille de la map
        # Variable contenant le premier plan de la map
        self.premier_plan = pg.Surface((self.x * 32, self.y * 32),
                                       pg.SRCALPHA)  # On crée une surface de la taille de la map
        # self.charger_hitboxs()  # Charger les collisions de la map (Hitboxs)
        self.charger_images()  # Charger l'arrière plan et le premier plan
        # self.vider_monstres()  # Supprimer les monstres de l'ancienne map (si il y en a)
        self.afficher_arriere_plan()

    def afficher_arriere_plan(self):
        """ Affiche les 3 premières couches de la map
        3 premières couches (0,1,2) = Arrière plan
        """
        gs.win.blit(self.arriere_plan, (self.x_camera,
                                          self.y_camera))  # Affiche l'arrière plan
    def afficher_premier_plan(self):
        """ Affiche la 4 eme couche de la map
        Quatrième couche (3) = Premier plan devant le personnage
        """
        gs.win.blit(self.premier_plan, (self.x_camera,
                                          self.y_camera))  # Affiche le premier plan


    def charger_matrice(self):
        """Charger les matrices
        Lire le fichier de la carte et stocker les tuiles dans une matrice
        Permets de convertir un .csv en tableau/matrice.
        Permets de convertir plusieurs .csv en tableaux 3D
        """
        for i in range(10):  # On a 4 calques, ici on parcours les calques
            nom_fichier = "maps/" + self.nom + "_" + str(i) + ".csv"  # Nom du fichier
            #                                          # Ex: nom_0.csv
            f = open(nom_fichier, "r")    # Ouvrir le fichier
            for ligne in f.readlines():   # Je regarde chaque lignes
                ligne = ligne.replace("\n", "")  # Je supprime les \n
                ligne = ligne.split(",")  # On convertis la ligne en liste
                if ligne != []:  # Si la ligne en liste n'est pas nulle
                    self.matrices[i].append(ligne)  # On ajoute la liste
            f.close()  # Fermer fichier

    def charger_hitboxs(self):
        """ Crée les rectangles de collisions de la map
        Permets de charger les rectangles de collision de la map
        (Peut génèrer des latences !)
        """
        for groupe in ts.groupes:  # Je parcours les groupes de collision
            ts.groupes[groupe] = pg.sprite.Group()  # Je les réinitialise

        for i in range(10):  # Je parcours les 3 premières couches de la map
            for y in range(self.y):  # Parcours les colonnes
                for x in range(self.x):  # Je parcours les lignes
                    if self.matrices[i][y][x] in ts.tuiles:  # Si la tuile existe
                        if self.matrices[i][y][x] in ts.collisions:  # Si on lui a assigné des collisions
                            x_tuile = self.x_camera + x*32  # Position de la tuile (abscisses)
                            y_tuile = self.y_camera + y*32  # Position de la tuile (ordonnée)
                            tuile = ts.tuiles[self.matrices[i][y][x]]  # On extrait l'image
                            mask = pg.mask.from_surface(tuile)  # On fait le mask a partir de cette image
                            rect = pg.Rect(x_tuile, y_tuile, 32, 32)  # On créé le rectangle associé a l'image
                            col.Hitbox("tuile", rect, mask)  # Sauvegarder la liste (rect + mask)


    def charger_images(self):
        """ Charge dans la variable self.arriere_plan l'image superposée des 3 premieres couches (0, 1, 2)
            Charge dans la variable self.premier_plan l'image de la dernière couche (3)
        """

        for i in range(10):  # Je parcours les couches
            for y in range(self.y):  # Parcours les colonnes
                for x in range(self.x):  # Je parcours les lignes
                    if self.matrices[i][y][x] in ts.tuiles:  # Si elle existe
                        tuile = ts.tuiles[self.matrices[i][y][x]]  # On extrait
                        if i < 5:  # Si on parcours les couches 2, 1 et 0
                            self.arriere_plan.blit(tuile, (x*32, y*32))  # On colle les images sur l'arrière plan tuile par tuile
                        else:
                            self.premier_plan.blit(tuile, (x*32, y*32))  # On colle les images sur le premier plan tuile par tuile
