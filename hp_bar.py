import pygame
import time

class hp():
    def __init__(self, DISPLAY, x,y,l,h):
        self.display = DISPLAY
        self.const_rect = pygame.Rect(x,y,l,h)
        self.rect = pygame.Rect(x,y,l,h)
        self.dead = False
    
    def draw(self):
        pygame.draw.rect(self.display, (255,255,255), self.const_rect)
        pygame.draw.rect(self.display, (0,200,0),self.rect)
    
    def reduce(self, reduction_amount):
    
        for n in range(30):
            if self.rect.width > 0:
                self.rect.width -= int(reduction_amount/30)
                time.sleep(0.02)
                self.draw()
                pygame.display.update()
        if self.rect.width <= 0:
            self.dead = True
