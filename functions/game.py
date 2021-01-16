from constants import game_settings as gs
from functions import load
import pygame as pg
from classes import player
from classes import mapping


def win_init():
    pg.display.set_caption("HETIC LIFE") #window title
    # Game Icon (HETIC LOGO)
    pg.display.set_icon(pg.image.load("img/game_icon.png"))
    gs.win = pg.display.set_mode((gs.WIDTH, gs.HEIGHT))
    gs.run = True
    gs.clock = pg.time.Clock()
    init_game()


def init_game():
    #loading_screen()
    #load tileset
    load.load_tileset()
    load.load_sprites()
    gs.map = mapping.Map("MapHeticV2", (-50, -300), "hetic.ogg")  # Chargement de la map
    #setup map
    #load enemies
    gs.char = player.Player()
    game_loop() #starts game


def game_loop():
    # Game Loop
     while gs.run:
        gs.win.fill((gs.DARKGREY))
        gs.char.player_controls() #links function to char variable
        gs.map.afficher_arriere_plan()
        gs.char.update()
        gs.map.afficher_premier_plan()

     # Events (if you press ESC or close window, leaves game)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    gs.run = False
            elif event.type == pg.QUIT:
                gs.run = False
    #####TODO:insérer fonction teleportation (gère le changement de maps)

        ###gérer mort perso avec def death():
            ##if cp.char.health < 1
            ### return death()
        #   runs game at FPS defined in gs (game_settings)
        gs.clock.tick(gs.FPS)
        # updates screen
        pg.display.update()


#todo: def teleportation(): (gère changement de map)



