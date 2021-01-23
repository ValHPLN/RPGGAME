
vitesse = 2

sprite_npc1_still =  "img/char/char_face_"
sprite_npc1_move = "img/char/char_walk_"
#sprite_sdt = "images/sprites/chauve_souris_"
#sprite_npc2 = "images/sprites/chat_"
#sprite_npc3 = "images/sprites/oiseau_"
#sprite_npc4 = "images/sprites/poussin_"

timings = { # Timings des animations
    # [tick, images, libre, reset]
    # tick = le nombre de tick pour changer une frame (Tick entre chaque frame)
    # images = le nombre d'images de l'animation - 1 (0 compte comme une frame)
    # libre = Libérer le personnage après l'animation ? True = oui False = non
    # reset = revenir sur base après la fin de l'animation ? (Sinon on répète)
    "npc" : {
        "npc1" : {

            "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
            "walk": [4, 3, True, False]
        },
       #"chauve_souris" : {

       #    "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
       #    "marche": [4, 2, True, False]
       #},
       #"oiseau" : {

       #    "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
       #    "marche": [10, 2, True, False]
       #},
       #"chat" : {

       #    "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
       #    "marche": [10, 2, True, False]
       #},
       #"poussin":  {

       #    "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
       #    "marche": [8, 2, True, False]
       #}
    }
}
action = {
    "up":    [0, -vitesse, "up", "walk", True],
    "left":  [-vitesse, 0, "left", "walk", True],
    "down":  [0, vitesse, "down", "walk", True],
    "right": [vitesse, 0, "right", "walk", True],
   # "attaque":     [0, 0, None, "attaque", False]
}
deplacement = {
    "base" : [
        "up", "left", "down", "right"
    ],
    "path" : [
        "right", "left", "down", "right"
    ],
    "random" : [
            0,1,2,3
    ],
}
animation = {
    "npc": {
        "npc1": {

             "down": {
                "base": [
                    sprite_npc1_still + "down.png"   # Base
                ],
                "walk": [
                    sprite_npc1_move + "down1.png",
                    sprite_npc1_move + "down2.png",
                    sprite_npc1_move + "down3.png",
                    sprite_npc1_move + "down4.png",
                    sprite_npc1_move + "down5.png",
                    sprite_npc1_move + "down6.png",
                    sprite_npc1_move + "down7.png",
                    sprite_npc1_move + "down8.png",
                    sprite_npc1_move + "down9.png",
                ],
            },
            "right": {
                "base": [
                    sprite_npc1_still + "right.png"  # Base
                ],
                "walk": [
                    sprite_npc1_move + "right1.png",
                    sprite_npc1_move + "right2.png",
                    sprite_npc1_move + "right3.png",
                    sprite_npc1_move + "right4.png",
                    sprite_npc1_move + "right5.png",
                    sprite_npc1_move + "right6.png",
                    sprite_npc1_move + "right7.png",
                    sprite_npc1_move + "right8.png",
                    sprite_npc1_move + "right9.png",
                 ],
             },

            "left": {
                "base": [
                    sprite_npc1_still + "left.png"  # Base
                ],
                "walk": [
                    sprite_npc1_move + "left1.png",
                    sprite_npc1_move + "left2.png",
                    sprite_npc1_move + "left3.png",
                    sprite_npc1_move + "left4.png",
                    sprite_npc1_move + "left5.png",
                    sprite_npc1_move + "left6.png",
                    sprite_npc1_move + "left7.png",
                    sprite_npc1_move + "left8.png",
                    sprite_npc1_move + "left9.png",
                ],
            },

            "up": {
               "base": [
                   sprite_npc1_still + "up.png"  # Base
               ],
               "walk": [
                   sprite_npc1_move + "up1.png",
                   sprite_npc1_move + "up2.png",
                   sprite_npc1_move + "up3.png",
                   sprite_npc1_move + "up4.png",
                   sprite_npc1_move + "up5.png",
                   sprite_npc1_move + "up6.png",
                   sprite_npc1_move + "up7.png",
                   sprite_npc1_move + "up8.png",
                   sprite_npc1_move + "up9.png",
               ],
            }
        }
    }
}
