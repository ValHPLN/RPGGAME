from classes.inventory import Inventory
from constants import game_settings as gs
from constants import voice_settings as vs
from constants import speech_settings as ss
from constants import entity_settings as es
from functions import load
import pygame as pg
from classes import player, objects
from classes import mapping
from functions import speech

inventory = Inventory(player, 10, 5, 2)

playerList = (
"Adam", "Alex", "Amelia", "Bob", "Bouncer", "Conference_man",
"Conference_woman", "Dan", "Edward", "Halloween_Kid_1", "kid_Abby", "kid_Oscar", "Lucy", "Molly", "Old_man_Josh",
"Old_woman_Jenny", "Pier", "Rob", "Roki", "Samuel", "Santa_claus")
clickArrow = False
compteur = 0


def win_init():
    pg.display.set_caption("HETIC LIFE") #window title
    # Game Icon (HETIC LOGO)
    pg.display.set_icon(pg.image.load("img/game_icon.png"))
    gs.win = pg.display.set_mode((gs.WIDTH, gs.HEIGHT))
    pg.mouse.set_cursor(*pg.cursors.diamond)
    gs.run = True
    gs.clock = pg.time.Clock()
    init_game()


def init_music():
    pg.mixer.pre_init(44100, -16, 2, 1024)  # sets hps audio mixer
    pg.mixer.init()  # init mixer
    pg.mixer.set_num_channels(8)
    pg.mixer.Channel(1)


def init_game():
    load.load_tileset()
    init_music()
    gs.map = mapping.Map("MapHeticV2", (40, -720), "hetic.ogg")  # Loads map
    gs.map.load_npc()
    randomPlayer = playerList[compteur]
    gs.char = player.Player(randomPlayer, gs.base_hp)
    main_menu()


def play_music():
    gs.music = pg.mixer.music
    gs.music.load("sound/elif.ogg") # THAT'S MY SONG !! IT'S COOL RIGHT ? Do you feel the good ol' GameBoy nostalgia ? (I know I'm old af)
    gs.music.set_volume(0.5) #sets up volume
    gs.music.play(loops=-1) #loops song


def draw_text(text, font, color, surface, x, y):
    textobj = gs.font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.center = (x,y)
    surface.blit(textobj,textrect)

################ ALL MENUS WORK KINDA THE SAME ###############
#gets mouse position to know which text you're hovering
# sets up variables to record clicking and currently selected text
# changes color of the selected text when mouse hovering
# and performs actions according to click

def new_player(): #creates a new player,
    global compteur
    compteur = 0
    gs.win.fill((gs.DARKGREY))
    choosePlayer(compteur)
    char_create = True
    clickArrow = True
    active = False
    selected = None
    color_inactive = pg.Color(gs.LIGHTGREY)
    color_active = pg.Color(gs.GREEN)
    color = color_inactive
    name_title = text_format("Entre ton pseudo", gs.menuFont, 60, gs.GREEN)
    name_title_rect = name_title.get_rect()
    input_box = pg.Rect(gs.center_WIDTH - (name_title_rect[2] / 3.5),300, 10,30)
    confirm = False

    while char_create:
        while not confirm:
            if selected == "leftA":
                leftArrow = text_format("<", gs.menuFont, 75, gs.WHITE)
            else:
                leftArrow = text_format("<", gs.menuFont, 75, gs.BLACK)
            if selected == "rightA":
                rightArrow = text_format(">", gs.menuFont, 75, gs.WHITE)
            else:
                rightArrow = text_format(">", gs.menuFont, 75, gs.BLACK)
            if selected == "start":
                text_start = text_format("JOUER", gs.menuFont, 75, gs.WHITE)
            else:
                text_start = text_format("JOUER", gs.menuFont, 75, gs.BLACK)


            gs.win.fill((gs.DARKGREY))
            choosePlayer(compteur)
            txt_surface = gs.font.render(gs.name, True, color)
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            gs.win.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pg.draw.rect(gs.win, color, input_box, 2)
            gs.win.blit(name_title, (gs.WIDTH / 2 - (name_title_rect[2] / 2), 150))
            leftArrow_rect = leftArrow.get_rect()
            rightArrow_rect = rightArrow.get_rect()
            gs.win.blit(leftArrow, (gs.WIDTH / 2 - (leftArrow_rect[2] / 2) - 150, 400))
            gs.win.blit(rightArrow, (gs.WIDTH / 2 - (rightArrow_rect[2] / 2) + 150, 400))
            leftArrow_rect.x, leftArrow_rect.y = 450 - (leftArrow_rect[2] / 2), 400
            rightArrow_rect.x, rightArrow_rect.y = 750 - (leftArrow_rect[2] / 2), 400
            start_rect = text_start.get_rect()
            gs.win.blit(text_start, (gs.WIDTH / 2 - (start_rect[2] / 2), 600))
            updateX = (gs.WIDTH / 2 - (start_rect[2] / 2))
            updateY1 = 600
            start_rect.x, start_rect.y = updateX, updateY1

            mx, my = pg.mouse.get_pos()
            for event in pg.event.get():
                #print(mx, my)
                if start_rect.collidepoint((mx, my)): #if collision with mouse cursor
                    selected = "start"
                elif leftArrow_rect.collidepoint((mx, my)):
                    selected = "leftA"
                elif rightArrow_rect.collidepoint((mx, my)):
                    selected = "rightA"
                else:
                    selected = None
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        clickArrow = None
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if selected == "start":
                            if gs.name != '':
                                char_create = False
                                game_loop()
                                return gs.name
                        if selected == "leftA":
                            gs.win.fill((gs.DARKGREY))
                            compteur = compteur - 1
                            choosePlayer(compteur) #changes selected player upon arrow clicking
                        if selected == "rightA":
                            gs.win.fill((gs.DARKGREY))
                            compteur = compteur + 1
                            choosePlayer(compteur)
                        if input_box.collidepoint(event.pos):
                            active = not active
                        else:
                            active = False
                        color = color_active if active else color_inactive #changes color of text and box when active
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        char_create = False
                        active = False
                        main_menu()
                    if active: #input box mus be active to enter name
                        if event.key == pg.K_BACKSPACE:
                            gs.name = gs.name[:-1]
                        else:
                            gs.name += event.unicode


            pg.display.update()
            gs.clock.tick(gs.FPS)


def text_format(message, textFont, textSize, textColor): #function to set up text
    newFont=pg.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


def choosePlayer(number): #change player sprite in char creation menu
    global compteur
    max = len(playerList)
    if number < 0:
        number = max - 1
        compteur = number
    if number > max - 1:
        number = 0
        compteur = number

    player1 = "img/char/New/" + playerList[number] + "_run_32x32.png" #takes sprite from player list
    sprite_set = pg.image.load(player1)
    sprites = []
    for i in range(24):
        sprites.append(sprite_set.subsurface([i * 32, 0, 32, 64]))

    for i, s in enumerate(sprites):
        gs.win.blit(s, (580, 400))


def controls(): #controls menu
    ctrls= True
    click = False
    selected = None
    while ctrls:
        gs.win.fill((gs.DARKGREY))
        mx, my = pg.mouse.get_pos()
        title = text_format("TOUCHES", gs.menuFont, 90, gs.GREEN)
        if selected == "start":
            text_start = text_format("OK", gs.menuFont, 75, gs.WHITE)
        else:
            text_start = text_format("OK", gs.menuFont, 75, gs.BLACK)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()

        gs.win.blit(title, (gs.WIDTH / 2 - (title_rect[2] / 2), 80))
        gs.win.blit(text_start, (gs.WIDTH / 2 - (start_rect[2] / 2), 600))
        controlsimg = pg.image.load("img/controls2.png").convert_alpha() #PNG of the controls
        gs.win.blit(controlsimg, (60, 120))

        title_rect.x = gs.WIDTH / 2 - (title_rect[2] / 2)
        updateX = (gs.WIDTH / 2 - (start_rect[2] / 2))
        updateY1 = 600
        start_rect.x, start_rect.y = updateX, updateY1

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    menu = False
            elif event.type == pg.QUIT:
                pg.quit()
                quit()
            if start_rect.collidepoint((mx, my)):
                selected = "start"
            else:
                selected = None
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    if click:
                        if selected == "start":
                            ctrls = False
                            new_player()

        pg.display.update()
        gs.clock.tick(gs.FPS)


def main_menu():
    menu = True
    click = False
    selected = None
    play_music()
    while menu:
        gs.win.fill((gs.DARKGREY))
        mx, my = pg.mouse.get_pos()
        title = text_format("HETIC LIFE", gs.menuFont, 90, gs.GREEN)
        if selected == "start":
            text_start = text_format("JOUER", gs.menuFont, 75, gs.WHITE)
        else:
            text_start = text_format("JOUER", gs.menuFont, 75, gs.BLACK)
        if selected == "quit":
            text_quit = text_format("QUITTER", gs.menuFont, 75, gs.WHITE)
        else:
            text_quit = text_format("QUITTER", gs.menuFont, 75, gs.BLACK)


        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()
        gs.win.blit(title, (gs.WIDTH / 2 - (title_rect[2] / 2), 80))
        gs.win.blit(text_start, (gs.WIDTH / 2 - (start_rect[2] / 2), 300))
        gs.win.blit(text_quit, (gs.WIDTH / 2 - (quit_rect[2] / 2), 360))
        title_rect.x = gs.WIDTH / 2 - (title_rect[2] / 2)
        updateX = (gs.WIDTH / 2 - (start_rect[2] / 2))
        updateY1 = 300
        updateY2 = 360
        start_rect.x, start_rect.y = updateX, updateY1
        quit_rect.x, quit_rect.y = updateX, updateY2 #changes position of the clickable rect so it's right on the text


        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    menu = False
            elif event.type == pg.QUIT:
                pg.quit()
                quit()
            if start_rect.collidepoint((mx, my)):
                selected = "start"
            elif quit_rect.collidepoint((mx, my)):
                selected = "quit"
            else:
                selected = None
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    if click:
                        if selected == "start":
                            menu = False
                            if gs.name == '': #if no name is defined, shows controls, else, starts game
                                controls()
                            else:
                                game_loop() # prevents player to go through char creation and controls if he already started the game once
                        elif selected == "quit":
                            quit()

        pg.display.update()
        gs.clock.tick(gs.FPS)


def inventory_menu():
    invent = True
    click = False
    selected = None
    inventory.toggleInventory()
    while invent:
        inventory_box = pg.Rect(gs.center_WIDTH-300, gs.center_HEIGHT-200, 600, 400)
        pg.draw.rect(gs.win, gs.WHITE, inventory_box)
        title = text_format("Inventaire", gs.menuFont, 50, gs.GREEN)
        title_rect = title.get_rect()
        gs.win.blit(title, (gs.WIDTH / 2 - (title_rect[2] / 2), 250))
        title_rect.x = gs.WIDTH / 2 - (title_rect[2] / 2)
        inventory.draw(gs.win)

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    invent = False
                    inventory.toggleInventory()
                if event.key == pg.K_i:
                    invent = False
                    inventory.toggleInventory()
            elif event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                if inventory.display_inventory:
                    mouse_pos = pg.mouse.get_pos()
                    inventory.checkSlot(gs.win, mouse_pos)
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if inventory.display_inventory:
                    inventory.moveItem(gs.win)
            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                if inventory.display_inventory:
                    inventory.placeItem(gs.win)

        interface()
        pg.display.update()
        gs.clock.tick(gs.FPS)


def pause_menu():
    pause = True
    click = False
    selected = None
    while pause:
        mx, my = pg.mouse.get_pos()
        pause_title = text_format("Pause", gs.menuFont, 60, gs.GREEN)
        if selected == "Resume":
            text_resume = text_format("Reprendre", gs.menuFont, 75, gs.WHITE)
        else:
            text_resume = text_format("Reprendre", gs.menuFont, 75, gs.BLACK)
        if selected == "Main Menu":
            text_menu = text_format("Menu Principal", gs.menuFont, 75, gs.WHITE)
        else:
            text_menu = text_format("Menu Principal", gs.menuFont, 75, gs.BLACK)


        title_rect = pause_title.get_rect()
        resume_rect = text_resume.get_rect()
        menu_rect = text_menu.get_rect()
        gs.win.blit(pause_title, (gs.WIDTH / 2 - (title_rect[2] / 2), 80))
        gs.win.blit(text_resume, (gs.WIDTH / 2 - (resume_rect[2] / 2), 300))
        gs.win.blit(text_menu, (gs.WIDTH / 2 - (menu_rect[2] / 2), 360))
        title_rect.x = gs.WIDTH / 2 - (title_rect[2] / 2)
        updateX = (gs.WIDTH / 2 - (resume_rect[2] / 2))
        updateY1 = 300
        updateY2 = 360
        resume_rect.x, resume_rect.y = updateX, updateY1
        menu_rect.x, menu_rect.y = updateX, updateY2

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pause = False
            elif event.type == pg.QUIT:
                pg.quit()
                quit()
            if resume_rect.collidepoint((mx, my)):
                selected = "Resume"
            elif menu_rect.collidepoint((mx, my)):
                selected = "Main Menu"
            else:
                selected = None
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    if click:
                        if selected == "Resume":
                            pause = False
                        elif selected == "Main Menu":
                            pause = False
                            main_menu()
        pg.display.update()
        gs.clock.tick(gs.FPS)


def speech1(): #first iteration of our speech function, this one is unused because it was merely to test the speech bubbles
    talk = True
    while talk:
        handle_npc()
        Mleft = 400
        MTop = 250
        speech.TypeText(Mleft, MTop, ss.speechList["npc1"]["npcText"], 200)
        #speech.TypeText(Mleft, MTop, ss.speechList["coffee"]["machine"], 200)

        if not gs.speech:
            talk = False
        gs.clock.tick(gs.FPS)
        pg.display.update()


def play_voice(): #plays voice file according to npc id, and state of the dialog (different file for each npc and each speech line!)
    voice = True
    while voice:
        if gs.voice is not None:
            gs.voice.stop()
        gs.voice = pg.mixer.Sound("sound/voices/" + vs.voicedict[gs.npcId][gs.findStr] + ".ogg") # Gets voice file according to Npc ID and dialog ID
        gs.voice.set_volume(0.2)
        gs.music.set_volume(0.1)
        gs.voice.play()
        voice = False
        # npcId is taken from entity.py upon collision with Npc
        # voice file is stored in voice_settings dict
        # "findStr" allows us to know which line of dialog is active)


def speech2(npcId, xPos, yPos):
    gs.talk = True


    while gs.talk:
        gs.findStr = es.timings["MapHeticV2"]["npc"][npcId]["speechMem"] # = dictionnary in entity_settings with [current map][entity category][Id of the npc][speech line]
        play_voice() #plays audio file when you talk to a npc

        if npcId == "npc2":
            if es.timings["MapHeticV2"]["npc"][npcId]["speechMem"] == "00":
                inventory.addItemInv(objects.hp_potion) #adds a coffee to inv when you talk to the woman for the second time, and each time afterwards
        if npcId == "npc3":
            if gs.findStr.find('001', 0, 3) != -1: # if state of the speech is "001" or more, check inventory for glasses
                if objects.glassesNb == 1: #takes value from objects
                    es.timings["MapHeticV2"]["npc"][npcId]["speechMem"] = "0015"
                    inventory.removeItemInv(objects.glasses) #removes glasses from inventory
                    objects.glassesNb = 0
                    gs.help_count += 1 #adds 1 to "Personnes aidées" in game.interface()
            elif gs.findStr.find('002', 0, 3) != -1:
                if objects.glassesNb == 1: #same as above but that's if you said "No" when he asks for help, you can still return the quest if you have the item
                    es.timings["MapHeticV2"]["npc"][npcId]["speechMem"] = "0025"
                    inventory.removeItemInv(objects.glasses)
                    objects.glassesNb = 0
                    gs.help_count += 1
        elif npcId == "npc6":
            if gs.findStr.find('001', 0, 3) != -1:
                if objects.coinNb == 1: #same method as above, but with a different npc and questline
                    es.timings["MapHeticV2"]["npc"][npcId]["speechMem"] = "0015"
                    inventory.removeItemInv(objects.coin)
                    objects.coinNb = 0
                    gs.help_count += 1
            elif gs.findStr.find('002', 0, 3) != -1:
                if objects.coinNb == 1:
                    es.timings["MapHeticV2"]["npc"][npcId]["speechMem"] = "0015"
                    inventory.removeItemInv(objects.coin)
                    objects.coinNb = 0
                    gs.help_count += 1
        reset_display()
        Mleft = xPos
        MTop = yPos
        indexMem = es.timings["MapHeticV2"]["npc"][npcId]["speechMem"]
        speech.TypeText(Mleft, MTop, ss.speechList[npcId][indexMem], 200)

        # determines if the displayed sentence is information, or a question
        # because if it is a question, the value will have already been modified
        if indexMem == es.timings["MapHeticV2"]["npc"][npcId]["speechMem"]:
            #increments dialog id every time you talk to the Npc
            es.timings["MapHeticV2"]["npc"][npcId]["speechMem"] = es.timings["MapHeticV2"]["npc"][npcId]["speechMem"] + "0"
            memPrint = es.timings["MapHeticV2"]["npc"][npcId]["speechMem"]
            try:
                print("no errors ",ss.speechList[gs.npcId][memPrint])
            except KeyError: #stop incrementing and goes back to earlier value if you reached end of dialogs dict
                es.timings["MapHeticV2"]["npc"][npcId]["speechMem"] = indexMem
                memPrint = es.timings["MapHeticV2"]["npc"][npcId]["speechMem"]
                print("error back:", ss.speechList[gs.npcId][memPrint])

        if npcId != "npc2": #everytime you talk to a NPC (except the first lady who gives you coffee (and heals you!!)
            if gs.base_hp >= 4: #if you have more than 4 HP (you can't die from cafeine deficiency so ...)
                gs.base_hp -= 0.7 #makes you lose HP
            else:
                pass

        if not gs.speech:
            gs.talk = False
            gs.music.set_volume(0.5) #music volume back to normal after every end of dialog)
        gs.talk = False
        gs.clock.tick(gs.FPS)
        pg.display.update()


def interface():
    #Displays health bar and help counter

    title = text_format("Energie", gs.menuFont, 15, gs.GREEN)
    help = text_format("Personnes aidées : " + str(gs.help_count), gs.menuFont, 15, gs.GREEN)
    title_rect = title.get_rect()
    title_rect.x = gs.WIDTH / 2 - (title_rect[2] / 2)
    pg.draw.rect(gs.win, (gs.RED), pg.Rect(20, 20, gs.base_hp * 5, 10))
    gs.win.blit(title, (20, 18))
    gs.win.blit(help, (20, 36))
    if gs.base_hp <= 5:
        title = text_format("Besoin urgent de café !", gs.menuFont, 30, gs.RED)
        gs.win.blit(title, (20, 54))


def handle_npc():
    for npc in gs.entities_list:
        npc.deplacement()
        npc.display()


def game_loop():
    if gs.change_char:
        gs.change_char = False
        randomPlayer = playerList[compteur]
        gs.playerSelect = randomPlayer
        gs.char = player.Player(randomPlayer, gs.base_hp)

    # Game Loop
    while gs.run:
        gs.win.fill((gs.DARKGREY))
        gs.char.player_controls() #links function to char variable
        gs.map.afficher_arriere_plan()
        handle_npc()
        gs.char.update()
        gs.map.afficher_premier_plan()
        interface()




     # Events (displays pause menu if you press ESC; leaves game when you close the window)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pause_menu()
                elif event.key == pg.K_i:
                    inventory_menu()
            elif event.type == pg.QUIT:
                pg.quit()
                quit()

    #####TODO: create teleportation function (manages the change of maps)
    ##### Hopefully we'll add another map sometimes in the future :)

        #   runs game at FPS defined in gs (game_settings)
        gs.clock.tick(gs.FPS)
        # updates screen
        pg.display.update()


def reset_display(): #resets a few functions for a correct display (so we don't have previous frames still blit on the screen)
    gs.map.afficher_arriere_plan()
    handle_npc()
    gs.char.update()
    gs.map.afficher_premier_plan()
    interface()

    gs.clock.tick(gs.FPS)
    pg.display.update()