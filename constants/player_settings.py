import pygame as pg

# Player movement speed
vel = 2
run = True
sprite_height = 64
sprite_width = 64
sprite_still = "img/char/char_face_"
sprite_move = "img/char/char_walk_"

keys = {  # move keys
    # [x, y, "direction", "mouvement", free?]
    # Nombre de pixels en x, nombre de pixels en y, direction, mouvement.
    # libre = Est-ce que le personnage est libre ? True/False
    pg.K_UP:    [0, vel, "up", "walk", True],
    pg.K_LEFT:  [vel, 0, "left", "walk", True],
    pg.K_DOWN:  [0, -vel, "down", "walk", True],
    pg.K_RIGHT: [-vel, 0, "right", "walk", True],
    }

####################################################
timing = {
 # [tick, images, libre, reset]
    # tick = le nombre de tick pour changer une frame (Tick entre chaque frame)
    # images = le nombre d'images de l'animation - 1 (0 compte comme une frame)
    # libre = Libérer le personnage après l'animation ? True = oui False = non
    # reset = revenir sur base après la fin de l'animation ? (Sinon on répète)
    "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
    "walk": [4, 5, True, False],
    }
