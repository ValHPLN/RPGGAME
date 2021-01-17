import pygame as pg
pg.init()
mx, my = pg.mouse.get_pos()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Window settings
font = pg.font.SysFont(None, 20)
FPS = 60
char = None
win = None #Window
map = None #variable for map
WIDTH = 1200
HEIGHT = 800
TITLE = "HETIC LIFE"
BGCOLOR = DARKGREY #BACKGROUND COLOR
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
center_WIDTH = WIDTH/2
center_HEIGHT = HEIGHT/2


clock = None
run = None

# Initalises Pygame

