import pygame
from constants import game_settings as gs
from constants import speech_settings as ss
import textwrap

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

class TypeText():
    def __init__(self, x, y, text1, width):
        self.x = x
        self.y = y
        self.bubbleWidth = width #210
        self.bubbleHeight = 140
        self.bubblePadding = 10
        self.line = 0
        self.delay = 20
        self.color = (000, 000, 000)
        self.fontSize = 12
        self.fontWidth = self.fontSize * 4.5 / 7 #largeur moyenne haute d'une lettre
        self.fontWrap = int((self.bubbleWidth - (2 * self.bubblePadding)) / self.fontWidth) #combien de lettres avant le retour à la ligne
        print(self.fontWidth, self.fontWrap)
        self.fontInter = self.fontSize + self.fontSize * 8 / 12 #interligne
        self.textA = "\n".join(textwrap.wrap(text1, self.fontWrap))
        self.fontType = 'img/Minecraftia-Regular.ttf'
        self.bubbleImg()
        self.splitText(self.textA)
        #self.display_text_animation(self.textA)
        #self.quit()

    def bubbleImg(self): #importe et affiche la bulle
        bubblePng = pygame.image.load("img/SpeechBubble.png")
        bubblePng = pygame.transform.scale(bubblePng, (self.bubbleWidth, self.bubbleHeight))  # 42 28
        gs.win.blit(bubblePng, (self.x - self.bubblePadding, self.y - self.bubblePadding))

    def arrowImg(self): #importe et affiche la touche entrer
        arrowPng = pygame.image.load("img/arrow.png")
        #arrowPng = pygame.transform.scale(arrowPng, (18, 15))  # 23 19
        gs.win.blit(arrowPng, (self.x + self.bubbleWidth - 48, self.y + self.bubbleHeight - 58))
        pygame.display.update()

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
                font = pygame.font.Font(self.fontType, self.fontSize)
                text_surface = font.render(text, True, self.color)
                textSize = text_surface.get_size()
                bubbleSurf = pygame.Surface((textSize[0] + 10, textSize[1]))
                bubbleRect = bubbleSurf.get_rect()
                bubbleSurf.fill(WHITE)
                bubbleSurf.blit(text_surface, text_surface.get_rect(topleft=bubbleRect.topleft))
                bubbleRect.topleft = (self.x, self.y + (self.line * self.fontInter))
                gs.win.blit(bubbleSurf, bubbleRect)
                pygame.display.update()
                pygame.time.wait(self.delay)
            self.line = self.line + 1
            Wrap = Wrap[Index+1:]
        self.arrowImg()
        self.line = 0
        self.enter()
        self.bubbleImg()

    def enter(self):
        gs.speech = True
        while gs.speech:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gs.speech = False
