import pygame, sys
from constants import game_settings as gs

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
DISPLAYSURF = pygame.display.set_mode((0, 0))

class TypeText():
    def __init__(self, x, y, text1, text2, text3):
        self.x = x
        self.y = y
        self.size = 20
        self.line = 0
        self.color = (000, 000, 000)
        self.font_type = 'img/Minecraftia-Regular.ttf'
        self.bubbleImg()
        self.display_text_animation(text1)
        self.display_text_animation(text2)
        self.display_text_animation(text3)
        self.quit()

    def bubbleImg(self):
        bubblePng = pygame.image.load("img/SpeechBubble.png")
        bubblePng = pygame.transform.scale(bubblePng, (210, 140))  # 42 28
        gs.win.blit(bubblePng, (self.x - 10, self.y - 10))

    def display_text_animation(self, string):
        text = ''
        for i in range(len(string)):
            # DISPLAYSURF.fill(WHITE)
            text += string[i]
            font = pygame.font.Font(self.font_type, self.size)
            text_surface = font.render(text, True, self.color)
            textSize = text_surface.get_size()
            bubbleSurf = pygame.Surface((textSize[0] + 10, textSize[1]))
            bubbleRect = bubbleSurf.get_rect()
            bubbleSurf.fill(WHITE)
            bubbleSurf.blit(text_surface, text_surface.get_rect(topleft=bubbleRect.topleft))
            bubbleRect.topleft = (self.x, self.y + (self.line * 30))
            gs.win.blit(bubbleSurf, bubbleRect)
            pygame.display.update()
            pygame.time.wait(100)
        self.line = self.line + 1

    def quit(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        transparent = (0, 0, 0, 0)
                        #bubblePng = pygame.image.fill(bubblePng, transparent)
                        # DISPLAYSURF.quit()
                        # pygame.time.wait(300)
                        pygame.quit()
                        sys.exit()

