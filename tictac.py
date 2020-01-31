import pygame

class square():
    def __init__(self, DISPLAY,col, change_col, x,y,l,h):
        self.col = col
        self.real_col = col
        self.change_col = change_col
        self.display = DISPLAY
        self.rect = pygame.Rect(x,y,l,h)
        self.xo = None
    
    def draw(self):
        pygame.draw.rect(self.display, self.col, self.rect)
    
    def update(self, event):
        if self.xo == None:
            if event.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    self.col = self.change_col
                else:
                    self.col = self.real_col
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    if self.xo == None:
                        self.xo = "X"


