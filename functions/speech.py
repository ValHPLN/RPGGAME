import pygame
from constants import game_settings as gs
from constants import speech_settings as ss
import textwrap

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

class TypeText():
    def __init__(self, x, y, text1):
        self.x = x
        self.y = y
        self.textA = "\n".join(textwrap.wrap(text1, 8))
        self.size = 12
        self.wrap = 25
        self.line = 0
        self.delay = 60
        self.color = (000, 000, 000)
        self.font_type = 'img/Minecraftia-Regular.ttf'
        self.bubbleImg()
        self.display_text_animation(self.textA)
        self.quit()

    def bubbleImg(self):
        bubblePng = pygame.image.load("img/SpeechBubble.png")
        bubblePng = pygame.transform.scale(bubblePng, (210, 140))  # 42 28
        gs.win.blit(bubblePng, (self.x - 10, self.y - 10))

    def display_text_animation(self, string):
        Wrap = "\n".join(textwrap.wrap(string, self.wrap))
        count = string.count("\n")

        for i in range(count):
            try:
                Index = Wrap.index("\n")
            except ValueError:
                Index = len(Wrap)
            text = ''
            for i in range(Index):
                text += Wrap[i]
                font = pygame.font.Font(self.font_type, self.size)
                text_surface = font.render(text, True, self.color)
                textSize = text_surface.get_size()
                bubbleSurf = pygame.Surface((textSize[0] + 10, textSize[1]))
                bubbleRect = bubbleSurf.get_rect()
                bubbleSurf.fill(WHITE)
                bubbleSurf.blit(text_surface, text_surface.get_rect(topleft=bubbleRect.topleft))
                bubbleRect.topleft = (self.x, self.y + (self.line * self.size * 1.5))
                gs.win.blit(bubbleSurf, bubbleRect)
                pygame.display.update()
                pygame.time.wait(self.delay)
            self.line = self.line + 1
            Wrap = Wrap[Index+1:]

    def quit(self):
        gs.speech = True
        while gs.speech:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        gs.speech = False
