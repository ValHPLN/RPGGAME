from constants import game_settings as gs
from constants import speech_settings as ss
from functions import load
import pygame as pg
from classes import player
from classes import mapping
from functions import speech

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
    gs.map = mapping.Map("MapHeticV2", (30, -720), "hetic.ogg")  # Chargement de la map
    #setup map
    #load enemies
    gs.char = player.Player()
    main_menu() # starts game

def draw_text(text, font, color, surface, x, y):
    textobj = gs.font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.center = (x,y)
    surface.blit(textobj,textrect)

def new_player():
    char_create = True
    click = False
    active = False
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive

    input_box = pg.Rect(gs.center_WIDTH,gs.center_HEIGHT, 100,100)
    confirm = False
    while char_create:
        while not confirm:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        if input_box.collidepoint(event.pos):
                            active = not active
                        else:
                            active = False
                        color = color_active if active else color_inactive
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        char_create = False
                        main_menu()
                    if event.key == pg.K_RETURN:
                        char_create = False
                        game_loop()
                        return gs.name
                    elif event.key == pg.K_BACKSPACE:
                        gs.name = gs.name[:-1]
                    else:
                        gs.name += event.unicode


            gs.win.fill((gs.DARKGREY))
            txt_surface = gs.font.render(gs.name, True, color)
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            gs.win.blit(txt_surface,(input_box.x+5, input_box.y+5))
            pg.draw.rect(gs.win, color, input_box, 2)
            draw_text("What's your name ?", gs.font, (gs.WHITE), gs.win, gs.center_HEIGHT, gs.center_WIDTH)
            pg.display.update()
            gs.clock.tick(gs.FPS)

def main_menu():
    menu = True
    click = False
    while menu:
        gs.win.fill((gs.DARKGREY))
        draw_text('main menu', gs.font, (gs.BLACK), gs.win, 50,25)
        mx, my = pg.mouse.get_pos()

        new_game = pg.Rect(gs.center_WIDTH-50,gs.center_HEIGHT-20, 100, 50)
        pg.draw.rect(gs.win, gs.WHITE, new_game)
        draw_text('New Game', gs.font, (gs.BLACK), gs.win, gs.center_WIDTH, gs.center_HEIGHT)
        if new_game.collidepoint((mx,my)):
            if click:
                menu = False
                new_player()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    menu = False
            elif event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False


        pg.display.update()
        gs.clock.tick(gs.FPS)

def inventory_menu():
    invent = True
    click = False
    selected = None
    while invent:
        inventory_box = pg.Rect(50, 50, 1000, 500)
        pg.draw.rect(gs.win, gs.WHITE, inventory_box)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    invent = False
                if event.key == pg.K_i:
                    invent = False
            elif event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pg.display.update()
        gs.clock.tick(gs.FPS)

def pause_menu():
    pause = True
    click = False
    while pause:
        mx, my = pg.mouse.get_pos()
        mainmenu = pg.Rect(500, 500, 100, 50)
        mmenu = pg.Surface((gs.WIDTH, gs.HEIGHT))
        mmenu.set_alpha(10)
        mmenu.fill(gs.BLACK)
        gs.win.blit(mmenu,(0,0))
        pg.draw.rect(gs.win, gs.WHITE, mainmenu)
        if mainmenu.collidepoint((mx,my)):
            if click:
                pause = False
                main_menu()
        inventory = pg.Rect(500, 600, 100, 50)
        pg.draw.rect(gs.win, gs.WHITE, inventory)
        draw_text(gs.name, gs.font, (gs.GREEN), gs.win, 50, 25) ###########PRINTS NAME TEST
        if inventory.collidepoint((mx,my)):
            if click:
                pause = False
                inventory_menu()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pause = False
            elif event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pg.display.update()
        gs.clock.tick(gs.FPS)

def speech1():
    talk = True
    while talk:
        Mleft = 400
        MTop = 250
        speech.TypeText(Mleft, MTop, ss.speechList["chomel"]["perso"], 200)
        #speech.TypeText(Mleft, MTop, ss.speechList["coffee"]["machine"], 200)
        if not gs.speech:
            talk = False
        gs.clock.tick(gs.FPS)
        # updates screen
        pg.display.update()

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
                    pause_menu()
                elif event.key == pg.K_i:
                    inventory_menu()
                elif event.key == pg.K_s:
                    speech1()
            elif event.type == pg.QUIT:
                pg.quit()

    #####TODO:insérer fonction teleportation (gère le changement de maps)

        ###gérer mort perso avec def death():
            ##if cp.char.health < 1
            ### return death()
        #   runs game at FPS defined in gs (game_settings)
        gs.clock.tick(gs.FPS)
        # updates screen
        pg.display.update()


#todo: def teleportation(): (gère changement de map)



