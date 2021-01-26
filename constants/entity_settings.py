
vitesse = 0.5


timings = { # animation timings
    # [tick, images, free, reset]
    # tick = number of ticks between frames
    # images = how many images per anim (don't forget 0)
    # free = Free character after animation? True = yes False = no
    # reset = come to "base" after anim, else animation repeats itself

    ####################################
    # Also gathers all NPCs and objects that can be picked up:
        # Init = x, y, size, position
        # pathfile = sprite
        # base = animation if tick = None, no animation
        # walk = timings (see above)
        # pathchar = path taken by NpC
    "MapHeticV2": {
        "npc": {
            "npc1": {
                "init":[[[500, 660], [64,64], "base"]],
                "pathFile": "img/char/New/Bouncer_run_32x32.png",
                "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
                "walk": [4, 5, True, False],
                "pathChar": ["up", "up", "left", "left", "down", "down", "right", "right"]
            },
            "npc2": {
                "init":[[[400, 660], [64,64], "base"]],
                "pathFile": "img/char/New/Amelia_run_32x32.png",
                "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
                "walk": [4, 5, True, False],
                "pathChar": ["up", "right", "down", "left"]
            },
        },
        "obj": {
            "coin": {
                "init":[[[640, 720], [32, 32], "base"]],
                "pathFile": "img/objects/coin.png",
                "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
                "walk": [None],
                "pathChar": [None]
            },
            "coin2": {
                "init": [[[700, 720], [32, 32], "base"]],
                "pathFile": "img/objects/coin.png",
                "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
                "walk": [None],
                "pathChar": [None]
            },
            "coin3": {
                "init": [[[750, 720], [32, 32], "base"]],
                "pathFile": "img/objects/coin.png",
                "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
                "walk": [None],
                "pathChar": [None]
            },
            "glasses":{
                "init": [[[663, 463], [32, 32], "base"]],
                "pathFile": "img/objects/glasses.png",
                "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
                "walk": [None],
                "pathChar": [None]
            },
            "cable":{
                "init": [[[863, 863], [32, 32], "base"]],
                "pathFile": "img/objects/cable2.png",
                "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
                "walk": [None],
                "pathChar": [None]
            }
        }
    }
}

action = {
    "up":    [0, -vitesse, "up", "walk", True],
    "left":  [-vitesse, 0, "left", "walk", True],
    "down":  [0, vitesse, "down", "walk", True],
    "right": [vitesse, 0, "right", "walk", True],
}
