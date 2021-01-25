
vitesse = 2


timings = { # Timings des animations
    # [tick, images, libre, reset]
    # tick = le nombre de tick pour changer une frame (Tick entre chaque frame)
    # images = le nombre d'images de l'animation - 1 (0 compte comme une frame)
    # libre = Libérer le personnage après l'animation ? True = oui False = non
    # reset = revenir sur base après la fin de l'animation ? (Sinon on répète)
    "MapHeticV2": {
        "npc": {
            "npc1": {
                "init":[[[500, 660], [64,64], "base"]],
                "pathFile": "img/char/New/Bouncer_run_32x32.png",
                "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
                "walk": [4, 5, True, False],
                "pathChar": ["up", "left", "down", "right"]
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
        }
    }
}

action = {
    "up":    [0, -vitesse, "up", "walk", True],
    "left":  [-vitesse, 0, "left", "walk", True],
    "down":  [0, vitesse, "down", "walk", True],
    "right": [vitesse, 0, "right", "walk", True],
}
