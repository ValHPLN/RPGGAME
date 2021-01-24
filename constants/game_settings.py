import pygame as pg
pg.init()
mx, my = pg.mouse.get_pos()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (41, 242, 148)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Window settings
font = pg.font.SysFont(None, 20)
menuFont = "Retro.ttf"
FPS = 60
name = ""
speech = None
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
entities_list = []

clock = None
run = None


