import pygame
from button import *
pygame.font.init()
arial = pygame.font.SysFont('Arial', 40)
class text_screens():
    def __init__(self, bg_col, text_col):
        self.button_pressed = False
        self.text_col = text_col
        self.bg_col = bg_col
    def draw(self, DISPLAY, text):
        self.button_pressed = False
        player_text = arial.render(text, True, self.text_col)
        cont_button = button([200,200,200], (190,0, 230), (DISPLAY.get_width() /2) - 100, ((3 * DISPLAY.get_height())/4), 200, 75, "continue")      #(255, 255, 255), 200, 75, ((DISPLAY.get_width() /2) - 100, 800), "continue"

        while not cont_button.pressed:
            pygame.display.update()
            DISPLAY.fill(self.bg_col)
            DISPLAY.blit(player_text, ((DISPLAY.get_width() / 2) - (player_text.get_width() / 2),(DISPLAY.get_height()/4) - (player_text.get_height() / 2)))
            cont_button.draw(DISPLAY)

            for event in pygame.event.get():
                cont_button.update(event, DISPLAY)
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()