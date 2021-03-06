
vitesse = 0.5


timings = { # animation settings
    ####################################
    # Also gathers all NPCs and objects that can be picked up:
        # speechmem : state of dialog
        # Init = x, y, size, movement
        # pathfile = sprite
        # base = animation if tick = None, no animation
        # walk = tick, images, free, reset
        # pathchar = path taken by NpC
    "MapHeticV2": {
        "npc": {
            "npc1": {
                "speechMem": "0",
                "init":[[[600, 660], [64,64], "base"]],
                "pathFile": "img/char/New/Bouncer_run_32x32.png",
                "base": [None],
                "walk": [4, 5, True, False],
                "pathChar": [ "left", "left","left", "left","left", "left", "right", "right","right", "right","right", "right"]
            },
            "npc2": {
                "speechMem": "0", #[556, 1036
                "init":[[[506, 1066], [64,64], "base"]],
                "pathFile": "img/char/New/Amelia_run_32x32.png",
                "base": [None],
                "walk": [4, 5, True, False],
                "pathChar": ["right", "left"]
            },
             "npc3":{
                "speechMem": "0",
                "init":[[[854, 1015], [64,64], "base"]],
                "pathFile": "img/char/New/Old_woman_Jenny_run_32x32.png",
                "base": [None],
                "walk": [4, 5, True, False],
                "pathChar": ["down", "down","down", "down","left","left", "up", "up", "up","up", "right", "right"]
            },
            "npc4":{
                "speechMem": "0",
                "init":[[[224, 954], [64,64], "base"]],
                "pathFile": "img/char/New/Rob_run_32x32.png",
                "base": [None],
                "walk": [None],
                "pathChar": ["still"],
                "stillOrientation": "left"
            },
            "npc5": {
                "speechMem": "0",
                "init": [[[835, 970], [64, 64], "base"]],
                "pathFile": "img/char/New/transparent.png",
                "base": [None],
                "walk": [None],
                "pathChar": ["still"],
                "stillOrientation": "left"
            },
            "npc6": {
                "speechMem": "0",
                "init": [[[220, 425], [64, 64], "base"]],#
                "pathFile": "img/char/New/Dan_run_32x32.png",
                "base": [None],  # Si tick =
                "walk": [None],
                "pathChar": ["still"],
                "stillOrientation": "right"
            }
        },
        "obj": {
            "coin": {
                "init":[[[1100, 630], [32, 32], "base"]],
                "pathFile": "img/objects/coin.png",
                "base": [None],
                "walk": [None],
                "pathChar": [None]
            },
            "glasses":{
                "init": [[[663, 463], [32, 32], "base"]],
                "pathFile": "img/objects/glasses.png",
                "base": [None],
                "walk": [None],
                "pathChar": [None]
            },
            "cable":{
                "init": [[[1153, 863], [32, 32], "base"]],
                "pathFile": "img/objects/cable2.png",
                "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
                "walk": [None],
                "pathChar": [None]
            }
        }
    }
}

action = { # [x, y, direction, movement, free]
    "up":    [0, -vitesse, "up", "walk", True],
    "left":  [-vitesse, 0, "left", "walk", True],
    "down":  [0, vitesse, "down", "walk", True],
    "right": [vitesse, 0, "right", "walk", True],
    "still_up": [0, 0, "up", "walk", True],
    "still": [0, 0, "down", "base", True]
}
