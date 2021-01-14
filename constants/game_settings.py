import pygame as pg


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Window settings
FPS = 60
player = None
win = None #Window
WIDTH = 1200
HEIGHT = 800
TITLE = "HETIC LIFE"
BGCOLOR = DARKGREY #BACKGROUND COLOR
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
center_WIDTH = WIDTH/2
center_HEIGHT = HEIGHT/2

map = None #variable for map
clock = None
run = None

# Initalises Pygame
pg.init()
