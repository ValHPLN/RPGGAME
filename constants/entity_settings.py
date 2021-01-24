
vitesse = 2


timings = { # Timings des animations
    # [tick, images, libre, reset]
    # tick = le nombre de tick pour changer une frame (Tick entre chaque frame)
    # images = le nombre d'images de l'animation - 1 (0 compte comme une frame)
    # libre = Libérer le personnage après l'animation ? True = oui False = non
    # reset = revenir sur base après la fin de l'animation ? (Sinon on répète)
    "npc" : {
        "npc1" : {
            "pathFile": "img/char/New/Bouncer_run_32x32.png",
            "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
            "walk": [4, 5, True, False],
            "pathChar": ["up", "left", "down", "right"]
        },
        "npc2": {
            "pathFile": "img/char/New/Amelia_run_32x32.png",
            "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
            "walk": [4, 5, True, False],
            "pathChar": ["up", "right", "down", "left"]
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
