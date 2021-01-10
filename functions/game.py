from constants import game_settings as gs
from functions import load
from constants import sprites
import pygame as pg
from classes import player


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
    sprites.player_sprites()
    #setup map
    #load enemies
    gs.player = player.Player
    game_loop() #starts game


def draw_grid():

    for x in range(0, gs.WIDTH, gs.TILESIZE):
        pg.draw.line(gs.win,gs.LIGHTGREY,(x, 0), (x, gs.WIDTH))
    for y in range(0, gs.HEIGHT, gs.TILESIZE):
        pg.draw.line(gs.win,gs.LIGHTGREY,(0, y), (gs.WIDTH, y))


def draw_player():
    plClass = player.Player(0, 0)
    plClass.player_anim()
    plClass.player_controls()


def game_loop():
    # Game Loop
    while gs.run:
        gs.win.fill((gs.BGCOLOR)) #fills screen with background color
        draw_grid()
        draw_player()

    # Events (if you press ESC or close window, leaves game)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    gs.run = False
            elif event.type == pg.QUIT:
                gs.run = False

        #   runs game at FPS defined in gs (game_settings)
        gs.clock.tick(gs.FPS)
        # updates screen
        pg.display.update()




