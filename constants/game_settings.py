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
win = None #Window
map = None #variable for map
WIDTH = 1200
HEIGHT = 780
TITLE = "HETIC LIFE"
BGCOLOR = DARKGREY #BACKGROUND COLOR
TILESIZE = 32
INVTILESIZE = 48
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
center_WIDTH = WIDTH/2
center_HEIGHT = HEIGHT/2
clock = None
run = None


# NPC constants
entities_list = []
speech = None
npcId = None
npcX = None
npcY = None


# Player constants
name = ""
base_hp = 15
max_hp = 25
char = None
change_char = True
help_count = 0


# Dialogs & Audio constants
talk = False
voice = None
findStr = None
music = None

# collide variables
displayE2 = False
OKnb = None
OKindex = None
OKwin = None
OK1 = 0


