import pygame
import time

pygame.font.init()
FONT = pygame.font.SysFont('Arial', 32)

class tf():
    '''class for true/false buttons'''
    def __init__(self, DISPLAY, x, y, radius, text):
        self.x = x
        self.y = y
        self.display = DISPLAY
        self.active = False
        self.col = (100,100,100)
        self.real_col = (100,100,100)
        self.change_col = (190,0, 230)
        self.text = text = FONT.render(text, True, (0,0,0))
        self.radius = radius
        self.coloured = False

    def draw(self, anim_check):
        self.display.blit(self.text, (self.x + self.text.get_width()+5,self.y))
        if self.active:
            if anim_check:
                if not self.coloured:
                    for f in range(self.radius + 1):
                        pygame.draw.circle(self.display, (190,0, 230), (int(self.x),int(self.y)), f)
                        pygame.display.update()
                        time.sleep(0.02)
                    self.coloured = True
                
                pygame.draw.circle(self.display, (190,0,230), (int(self.x),int(self.y)), self.radius)
        else:
            pygame.draw.circle(self.display, (self.col), (int(self.x),int(self.y)), self.radius, 1)
            self.coloured = False
  
    def activate(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (int(event.pos[0] - self.x))**2 + (int(event.pos[1] - self.y))**2 <= self.radius**2:
                self.active = True
            elif not pygame.Rect((self.display.get_width() /2) - 100, ((3 * self.display.get_height())/4), 200, 75).collidepoint(event.pos):
                self.active = False

        