import time

import pygame as pg
from constants import game_settings as gs
from constants import entity_settings as es
from constants import speech_settings as ss
import textwrap

from constants.game_settings import npcId
from functions import game

BLACK = (  0,   0,   0)
BLUE = (64, 64, 100)
WHITE = (255, 255, 255)
CREAM = (235, 225, 246)

class TypeText():
    def __init__(self, x, y, text1, width):
        self.x = x + 40
        self.y = y - 10
        self.bubbleWidth = width    # Normally the rest of the code should adapt to this width. It's responsive
        self.bubbleHeight = 140
        self.bubblePadding = 10
        self.line = 0
        self.delay = 5
        self.color = (64, 64, 100)
        self.fontSize = 12
        self.fontWidth = self.fontSize * 4.5 / 7    # medium high letter width
        self.fontWrap = int((self.bubbleWidth - (2 * self.bubblePadding)) / self.fontWidth) #how many letters before the newline
        print(self.fontWidth, self.fontWrap)
        self.fontInter = self.fontSize + self.fontSize * 8 / 12 # line spacing
        self.fontType = 'img/Minecraftia-Regular.ttf'
        self.dico = {}
        self.hoverRect = {}
        self.megaDico = text1
        self.dictionary = False
        if type(text1) == dict:     # if the sentence is a question
            self.dictionary = True
            textDict = text1
            text1 = text1["question"]
            for i in range(1, len(textDict)):
                self.dico["rep{0}".format(i-1)] = textDict["answer" + str(i)]
            self.textA = "\n".join(textwrap.wrap(text1, self.fontWrap))
            self.textA = self.textA + "\n"
            self.textAbis = self.textA
            self.bubbleImg()
            self.drawDico()
        else:      # if the sentence is information
            print("text1: ", text1)
            self.textA = "\n".join(textwrap.wrap(text1, self.fontWrap))
            self.textA = self.textA + "\n"
            self.bubbleImg()
            self.splitText(self.textA)
        #self.display_text_animation(self.textA)
        #self.quit()

    def drawDico(self): # prepare text for display if that's a question
        count = self.textAbis.count("\n")

        for i in range(count):  # loop for each row of the question
            try:
                Index = self.textAbis.index("\n")
            except ValueError:
                Index = len(self.textAbis)
            text = ''
            for i in range(Index):      # loop for each letter in each row
                text += self.textAbis[i]
                font = pg.font.Font(self.fontType, self.fontSize)
                text_surface = font.render(text, True, self.color)
                textSize = text_surface.get_size()
                bubbleSurf = pg.Surface((textSize[0] + 10, textSize[1]))
                bubbleRect = bubbleSurf.get_rect()
                bubbleSurf.fill(CREAM)
                bubbleSurf.blit(text_surface, text_surface.get_rect(topleft=bubbleRect.topleft))
                bubbleRect.topleft = (self.x, self.y + (self.line * self.fontInter))
                gs.win.blit(bubbleSurf, bubbleRect)
                gs.clock.tick(gs.FPS)
                pg.display.update()
            self.line = self.line + 1
            self.textAbis = self.textAbis[Index+1:]

        count = (count + 1) * self.fontInter
        for x in range(len(self.dico)):     # loop for each row of the answer
            text = ''
            for i in range(len(self.dico["rep" + str(x)])):     # loop for each letter in each row
                text += self.dico["rep" + str(x)][i]
                font = pg.font.Font(self.fontType, self.fontSize)
                text_surface = font.render(text, True, self.color)
                gs.win.blit(text_surface, (self.x, self.y + count))
                gs.clock.tick(gs.FPS)
                pg.display.update()
            count = count + self.fontInter

        self.arrowImg()
        self.hover()
        #self.enter()
        #self.bubbleImg()

    def hover(self):  # response selection by the player
        noHover = True
        drawText = True
        selected = None
        change = False
        arrow = " <-"
        space = "       "
        memSelected = None
        printSelected = None
        hoverDico = self.dico
        while noHover:
            while drawText:
                count = self.textAbis.count("\n")
                count = (count + 1) * self.fontInter
                for x in range(len(self.dico)):     # loop for each row
                    self.hoverRect[x] = {}
                    text = ''
                    for i in range(len(self.dico["rep" + str(x)])):     # loop for each letter of each row
                        text += hoverDico["rep" + str(x)][i]
                        font = pg.font.Font(self.fontType, self.fontSize)
                        text_surface = font.render(text, True, self.color)
                        textSize = text_surface.get_size()
                        bubbleSurf = pg.Surface((textSize[0] + 10, textSize[1]))
                        bubbleRect = bubbleSurf.get_rect()
                        self.hoverRect[x][i] = bubbleRect
                        bubbleSurf.fill(CREAM)
                        bubbleSurf.blit(text_surface, text_surface.get_rect(topleft=bubbleRect.topleft))
                        bubbleRect.topleft = (self.x, self.y + (self.line * self.fontInter) + count)
                        gs.win.blit(bubbleSurf, bubbleRect)
                        gs.clock.tick(gs.FPS)
                        pg.display.update()
                    count = count + self.fontInter
                drawText = False

            mx, my = pg.mouse.get_pos()
            for event in pg.event.get():
                # print(mx, my)
                selected = None
                for x in range(len(self.hoverRect)):
                    for i in range(len(self.hoverRect[x])):
                        rect = self.hoverRect[x][i]
                        if rect.collidepoint((mx, my)):
                            selected = x
                            drawText = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    if printSelected != None:
                        if event.button == 1:
                            print(gs.npcId, str(printSelected + 1))
                            es.timings["MapHeticV2"]["npc"][gs.npcId]["speechMem"] = es.timings["MapHeticV2"]["npc"][gs.npcId]["speechMem"] + str(printSelected + 1)
                            noHover = False

                if event.type == pg.KEYDOWN:
                    if printSelected != None:
                        if event.key == pg.K_e:
                            print(gs.npcId, str(printSelected + 1))
                            es.timings["MapHeticV2"]["npc"][gs.npcId]["speechMem"] = es.timings["MapHeticV2"]["npc"][gs.npcId]["speechMem"] + str(printSelected + 1)
                            noHover = False

            if memSelected == selected:
                change = False
            else:
                change = True
            memSelected = selected

            if selected is not None:       # display of the arrow next to the selection hovered
                printSelected = selected
                while change:
                    for x in range(len(self.hoverRect)):
                        if selected == x:
                            hoverDico.update({"rep" + str(x): self.megaDico["answer" + str(x+1)] + arrow})
                            drawText = True
                        else:
                            hoverDico.update({"rep" + str(x): self.megaDico["answer" + str(x+1)] + space})
                            drawText = True
                    change = False


    def bubbleImg(self):    # import and display the bubble
        bubblePng = pg.image.load("img/SpeechBubble.png")
        #bubblePng = pg.transform.scale(bubblePng, (self.bubbleWidth, self.bubbleHeight))  # 42 28
        gs.win.blit(bubblePng, (self.x - self.bubblePadding, self.y - self.bubblePadding))

    def arrowImg(self): # import and display the enter key
        arrowPng = pg.image.load("img/arrow.png")
        #arrowPng = pg.transform.scale(arrowPng, (18, 15))  # 23 19
        gs.win.blit(arrowPng, (self.x + self.bubbleWidth - 55, self.y + self.bubbleHeight - 45))
        gs.clock.tick(gs.FPS)
        pg.display.update()

    def splitText(self, Wrap): # determines how many pages the text will be split into, based on the height of the bubble
        x = 1
        while x * self.fontInter < self.bubbleHeight: # count how many lines fit in a bubble
            x = x + 1
        limiteHeight = x - 1  # maximum number of lines to fit in a single bubble
        count = Wrap.count("\n")
        super = True
        while super:
            if count > limiteHeight: # if the text exceeds this maximum length
                i = 0
                Index = 1
                add = 0
                while i < limiteHeight - 1:  # find the place to cut the str
                    i = i + 1
                    add = Wrap.index("\n", Index)
                    Index = add + 3
                wrap1 = Wrap[:add]
                self.display_text_animation(wrap1) # send a piece of str to the function to display it
                Wrap = Wrap[add:] # delete from str the end that was sent
                count = Wrap.count("\n") # recount the number of lines remaining

            else:
                wrap1 = Wrap
                self.display_text_animation(wrap1) # send the last bit of str to the function to display it
                super = False

    def display_text_animation(self, Wrap):

        if Wrap.find("\n", 0, 2) == 0: # suppress the newline if there is one at the beginning
            Wrap = Wrap[1:]

        count = Wrap.count("\n")

        for i in range(count): # loop for each row
            try:
                Index = Wrap.index("\n")
            except ValueError:
                Index = len(Wrap)
            text = ''
            for i in range(Index): # loop for each letter of each row
                text += Wrap[i]
                font = pg.font.Font(self.fontType, self.fontSize)
                text_surface = font.render(text, True, self.color)
                textSize = text_surface.get_size()
                bubbleSurf = pg.Surface((textSize[0] + 10, textSize[1]))
                bubbleRect = bubbleSurf.get_rect()
                bubbleSurf.fill(CREAM)
                bubbleSurf.blit(text_surface, text_surface.get_rect(topleft=bubbleRect.topleft))
                bubbleRect.topleft = (self.x, self.y + (self.line * self.fontInter))
                gs.win.blit(bubbleSurf, bubbleRect)
                gs.clock.tick(gs.FPS)
                pg.display.update()
            self.line = self.line + 1
            Wrap = Wrap[Index+1:]
        self.arrowImg()
        self.line = 0
        self.enter()
        self.bubbleImg()

    def enter(self):
        gs.speech = True
        while gs.speech:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_e:
                        gs.speech = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        gs.speech = False


