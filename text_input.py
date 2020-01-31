import pygame

pygame.font.init()
FONT = pygame.font.SysFont('Arial', 32)
SFONT = pygame.font.SysFont('Arial', 20)

class text_input():
    """text input class"""
    def __init__(self, DISPLAY,x, y, w, h, text =''):
        self.display = DISPLAY
        self.rect = pygame.Rect(x, y, w, h)
        self.active = False
        self.colour = (200,200,200)
        self.text = text
        self.text_surface = FONT.render(text,True, (0,0,0) )
    
    def activate(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.colour = (100,100,100)
            else:
                self.active = False
                self.colour = (200,200,200)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_RETURN:
                    self.active = False
                    self.colour = (200,200,200)
                elif event.key == pygame.K_TAB:
                    self.active = False
                    self.colour = (200,200,200)
                else:
                    self.text += event.unicode
                self.text_surface = FONT.render(self.text, True, (0,0,0))

    def draw(self):
        self.display.blit(self.text_surface, (self.rect.x+5,self.rect.y+5))
        pygame.draw.rect(self.display, (self.colour), self.rect, 2)
