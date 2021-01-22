from constants import game_settings as gs, player_settings as ps
from constants import tiles_settings as ts
from constants import collisions_settings as cs
from classes import collision as col
import pygame as pg


class Player():
    def __init__(self, randomPlayer):

        self.randomPlayer = "img/char/New/" + randomPlayer + "_run_32x32.png"
        self.sprite = None #initialises PLayer
        self.free = True #is player busy
        self.count = 0
        self.frame = 0
        self.direction = "up"
        self.mouvement = "base"
        self.hitbox = col.Hitbox("player")
        self.hitbox_object = col.Hitbox("object")
        self.health = 10 #player health
        self.hurt = False #player hurt state
        self.hitbox.rect = pg.Rect((0,0),(56,0)) #creat rect on player feet for collisions
        self.hitbox.rect.center = (gs.center_WIDTH, gs.center_HEIGHT+13)
        self.hitbox.mask = pg.Mask((25,20))
        self.hitbox.mask.fill()


        # Créer un rectangle centré sur les jambes du personnage pour les collisions
        self.hitbox_object.rect = pg.Rect((gs.center_WIDTH - 20, gs.center_HEIGHT + 10), (32, 22))
        self.hitbox_object.rect.center = (gs.center_WIDTH - 4, gs.center_HEIGHT - 11)
        # Créer et assigner le hitbox
        self.hitbox_object.mask = pg.Mask((32, 22))
        self.hitbox_object.mask.fill()  # Remplir le hitbox pour créer un bloc

#charges sprites for the player
#image 0=standing 1=down 2=up 3=left 4=right

    def player_controls(self):
        # Controls (Arrow keys or ZQSD)
        userInput = pg.key.get_pressed()
        if not self.free:
            return
        if self.hitbox.mask is None:
            return
        for key in ps.keys:  # Je parcours les touches enfoncées
            if userInput[key]:  # Si la touche est définie dans constantes
                key = ps.keys[key]  # touche = sa liste correspondante

                if key[2] is not None:  # Si l'animation change la direction
                    self.direction = key[2]  # Modif direction
                if self.mouvement != key[3]:  # Si le mouvement change
                    self.mouvement = key[3]  # Changer le mouvement du perso
                    self.compteur = 0  # Recommencer les animations
                    self.frame = 0  # Réinitialiser les frames
                self.free = key[4]  # Changer disponibilité du perso

                # Capturer les déplacements
                x = key[0]  # Nombre de pixels en x
                y = key[1]  # Nombre de pixels en x
                # Déplacer le hitbox pour tester la position
                gs.map.bouger_hitbox(x, y)
                if self.hitbox.collision("tuile"):  # Si il y a collision:
                    # Annuler le déplacement de la hitbox de la map
                    gs.map.bouger_hitbox(-x, -y)
                elif self.hitbox.collision("object"):  # Si il y a collision:
                    # Annuler le déplacement de la hitbox de la map
                    gs.map.bouger(x, y)
                    print("contact")
                else:  # Sinon, si il y a pas collision
                    gs.map.bouger(x, y)

                break  # Casser la boucle: Touche trouvée. On évite les autres

        else:  # Si la boucle n'est pas cassée: Aucune touche trouvée
            self.free = True
            self.mouvement = "base"
            self.frame = 3


    def actualiser_frame(self):
        # MISE A JOUR DES FRAMES EN FONCTION DES TICKS
        # On vérifie si il y a un nombre de tick entre frame défini
        if ps.timing[self.mouvement][0] is None:  # Si il y en a pas
            self.compteur = 0
            self.frame = 5
        else:  # Si il y en a un
            # Maintenant on incrémente le compteur des animations si besoin
            if self.compteur < ps.timing[self.mouvement][0]:
                self.compteur = self.compteur + 1
                # Sinon si il est déjà à son max
            else:
                self.compteur = 0  # On le reset
                # On incrémente la frame si besoin d'être incrémenté
                if self.frame < ps.timing[self.mouvement][1]:
                    self.frame = self.frame + 1
                    # Sinon si elle est déjà a son max
                else:
                    self.frame = 0  # Reset
                    self.libre = ps.timing[self.mouvement][2]  # Liberer perso
                    if ps.timing[self.mouvement][3]:  # Si on veux revenir
                        self.mouvement = "base"  # Sur base, on le fait

    def actualiser_sprite(self):
        """ Met à jour le sprite
        Mise à jour du sprite en fonction de:
            - La direction
            - Le mouvement
            - La frame
        """
        cs.groups["player"] = [self.hitbox]

    def update(self):
        """Actualise les stats du personnage"""
        self.actualiser_frame()  # Actualiser les frames
        self.actualiser_sprite()  # Actualiser le sprite

        # Je calcule la position de rendu du sprite afin qu'il soit bien centré
        x_rendu = gs.center_WIDTH - ps.sprite_height / 2  # Le x de rendu
        y_rendu = gs.center_HEIGHT - ps.sprite_width / 2  # Le y de rendu

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

