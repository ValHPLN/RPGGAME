import pygame as pg

# Player movement speed
vel = 2
run = True
sprite_height = 64
sprite_width = 64
# Player position default
x = 500
y = 710
# Counter for frames/animation
stepIndex = 0
# Saves last movement for correct display of Standing image
lastKey = None
sprite_still = "img/char/char_face_"
sprite_move = "img/char/char_walk_"

keys = {  # Les touches pour les déplacements
    # [x, y, "direction", "mouvement", libre?]
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
    "walk": [4, 8, True, False],
    }

###################################################
animation = {
 "down": {
        "base": [
            sprite_still + "down.png"   # Base
        ],
        "walk": [
            sprite_move + "down1.png",
            sprite_move + "down2.png",
            sprite_move + "down3.png",
            sprite_move + "down4.png",
            sprite_move + "down5.png",
            sprite_move + "down6.png",
            sprite_move + "down7.png",
            sprite_move + "down8.png",
            sprite_move + "down9.png",
        ],
        },
 "right": {
        "base": [
            sprite_still + "right.png"  # Base
        ],
     "walk": [
            sprite_move + "right1.png",
            sprite_move + "right2.png",
            sprite_move + "right3.png",
            sprite_move + "right4.png",
            sprite_move + "right5.png",
            sprite_move + "right6.png",
            sprite_move + "right7.png",
            sprite_move + "right8.png",
            sprite_move + "right9.png",
     ],
 },

    "left": {
        "base": [
            sprite_still + "left.png"  # Base
        ],
        "walk": [
            sprite_move + "left1.png",
            sprite_move + "left2.png",
            sprite_move + "left3.png",
            sprite_move + "left4.png",
            sprite_move + "left5.png",
            sprite_move + "left6.png",
            sprite_move + "left7.png",
            sprite_move + "left8.png",
            sprite_move + "left9.png",
        ],
    },

    "up": {
        "base": [
            sprite_still + "up.png"  # Base
        ],
        "walk": [
            sprite_move + "up1.png",
            sprite_move + "up2.png",
            sprite_move + "up3.png",
            sprite_move + "up4.png",
            sprite_move + "up5.png",
            sprite_move + "up6.png",
            sprite_move + "up7.png",
            sprite_move + "up8.png",
            sprite_move + "up9.png",
        ],
    }
}

