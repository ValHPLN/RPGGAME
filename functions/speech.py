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
        self.bubbleWidth = width #210
        self.bubbleHeight = 140
        self.bubblePadding = 10
        self.line = 0
        self.delay = 5
        self.color = (64, 64, 100)
        self.fontSize = 12
        self.fontWidth = self.fontSize * 4.5 / 7 #largeur moyenne haute d'une lettre
        self.fontWrap = int((self.bubbleWidth - (2 * self.bubblePadding)) / self.fontWidth) #combien de lettres avant le retour à la ligne
        print(self.fontWidth, self.fontWrap)
        self.fontInter = self.fontSize + self.fontSize * 8 / 12 #interligne
        self.fontType = 'img/Minecraftia-Regular.ttf'
        self.dico = {}
        self.hoverRect = {}
        self.megaDico = text1
        self.dictionary = False
        if type(text1) == dict:
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
        else:
            self.textA = "\n".join(textwrap.wrap(text1, self.fontWrap))
            self.textA = self.textA + "\n"
            self.bubbleImg()
            self.splitText(self.textA)
        #self.display_text_animation(self.textA)
        #self.quit()

    def drawDico(self):
        count = self.textAbis.count("\n")

        for i in range(count): #boucle pour chaque ligne
            try:
                Index = self.textAbis.index("\n")
            except ValueError:
                Index = len(self.textAbis)
            text = ''
            for i in range(Index): #boucle pour chaque lettre de chaque ligne
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
                #pg.time.wait(self.delay)
            self.line = self.line + 1
            self.textAbis = self.textAbis[Index+1:]
        #self.arrowImg()

        #self.bubbleImg()
        count = (count + 1) * self.fontInter
        for x in range(len(self.dico)): #boucle pour chaque ligne
            text = ''
            for i in range(len(self.dico["rep" + str(x)])): #boucle pour chaque lettre de chaque ligne
                text += self.dico["rep" + str(x)][i]
                font = pg.font.Font(self.fontType, self.fontSize)
                text_surface = font.render(text, True, self.color)
                textSize = text_surface.get_size()
                #bubbleSurf = pg.Surface((textSize[0] + 10, textSize[1]))
                #bubbleRect = bubbleSurf.get_rect()
                #bubbleSurf.fill(CREAM)
                #bubbleSurf.blit(text_surface, text_surface.get_rect(topleft=bubbleRect.topleft))
                #bubbleRect.topleft = (self.x, self.y + (self.line * self.fontInter))
                #gs.win.blit(bubbleSurf, bubbleRect)
                gs.win.blit(text_surface, (self.x, self.y + count))
                gs.clock.tick(gs.FPS)
                pg.display.update()
                #pg.time.wait(self.delay)
            count = count + self.fontInter

        self.arrowImg()
        self.hover()
        #self.enter()
        #self.bubbleImg()

    def hover(self):
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
                for x in range(len(self.dico)): #boucle pour chaque ligne
                    self.hoverRect[x] = {}
                    text = ''
                    for i in range(len(self.dico["rep" + str(x)])): #boucle pour chaque lettre de chaque ligne
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
                        #gs.win.blit(text_surface, (self.x, self.y + count))
                        gs.clock.tick(gs.FPS)
                        pg.display.update()
                        #pg.time.wait(self.delay)
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

                if event.type == pg.KEYDOWN:
                    if printSelected != None:
                        if event.key == pg.K_RETURN:
                            print(self.megaDico["answer" + str(printSelected + 1)])
                            es.timings["MapHeticV2"]["npc"][npcId]["answer"] = printSelected + 1
                            noHover = False

            if memSelected == selected:
                change = False
            else:
                change = True
            memSelected = selected

            if selected is not None:
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





    def bubbleImg(self): #importe et affiche la bulle
        bubblePng = pg.image.load("img/SpeechBubble.png")
        #bubblePng = pg.transform.scale(bubblePng, (self.bubbleWidth, self.bubbleHeight))  # 42 28
        gs.win.blit(bubblePng, (self.x - self.bubblePadding, self.y - self.bubblePadding))

    def arrowImg(self): #importe et affiche la touche entrer
        arrowPng = pg.image.load("img/arrow.png")
        #arrowPng = pg.transform.scale(arrowPng, (18, 15))  # 23 19
        gs.win.blit(arrowPng, (self.x + self.bubbleWidth - 55, self.y + self.bubbleHeight - 45))
        gs.clock.tick(gs.FPS)
        pg.display.update()

    def splitText(self, Wrap): #détermine en combien de pages le texte sera découpé, en fonction de la hauteur de la bulle
        x = 1
        while x * self.fontInter < self.bubbleHeight: #compte combien de lignes rentrent dans une bulle
            x = x + 1
        limiteHeight = x - 1 #nombre maximal de lignes pour tenir dans une seule bulle
        count = Wrap.count("\n")
        super = True
        while super:
            if count > limiteHeight: #si le texte depasse de cette longeur maximale
                i = 0
                Index = 1
                add = 0
                while i < limiteHeight - 1:  # trouve l'endroit ou couper la str
                    i = i + 1
                    add = Wrap.index("\n", Index)
                    Index = add + 3
                wrap1 = Wrap[:add]
                self.display_text_animation(wrap1) #envoie un bout de str a la fontion pour l'afficher
                Wrap = Wrap[add:] #supprime de la str le bout qui a été envoyé
                count = Wrap.count("\n") #recompte le nombre de lignes restantes

            else:
                wrap1 = Wrap
                self.display_text_animation(wrap1) #envoie le dernier bout de str à la fonction pour l'afficher
                super = False

    def display_text_animation(self, Wrap):

        if Wrap.find("\n", 0, 2) == 0: #supprime le retour à la ligne si il y en a un au début
            Wrap = Wrap[1:]

        count = Wrap.count("\n")

        for i in range(count): #boucle pour chaque ligne
            try:
                Index = Wrap.index("\n")
            except ValueError:
                Index = len(Wrap)
            text = ''
            for i in range(Index): #boucle pour chaque lettre de chaque ligne
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
                #pg.time.wait(self.delay)
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
                    if event.key == pg.K_RETURN:
                        gs.speech = False


