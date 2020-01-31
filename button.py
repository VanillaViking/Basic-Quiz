import pygame
import textwrap
import time
pygame.font.init()


class button():
  """class for simplifying the use of buttons"""
  def __init__(self, real_col, change_col, x, y, w, h, text, text_col=(0,0,0), font_size=(25), wrapping=0, center=True, animate=True):
    arial = pygame.font.SysFont('Arial', font_size)
    self.real_col = real_col
    self.change_col = change_col
    self.colour = real_col
    self.rect = pygame.Rect(x,y,w,h)
    self.center = center
    self.plain_text = text
    self.pressed = False
    self.size_change = False
    self.animate = animate
    self.font_size = font_size

    #text wrapping inside the button
    if wrapping:
      self.text = []
      wrapped = textwrap.wrap(text, wrapping)
      for n in wrapped:
          self.text.append(arial.render(n, True, text_col))
    else:
        self.text = [arial.render(text, True, text_col)]


  def draw(self, DISPLAY):
    pygame.draw.rect(DISPLAY, self.colour, self.rect)

    #centering the text in the middle of the button
    if self.center:
        ypos = self.rect.center[1] - (self.text[0].get_height()/2)
    else:
        ypos = self.rect.y + 15
    
    #printing the text in
    for line in self.text:
      DISPLAY.blit(line, (self.rect.center[0] - (line.get_width()/2), ypos))
      ypos += self.font_size + 1
  

  def isOver(self, mouse_pos):
    if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
      return True

    return False 
  

  def update(self, event, DISPLAY):

    if event.type == pygame.MOUSEMOTION:
        if self.isOver(pygame.mouse.get_pos()):
            self.colour = self.change_col
            if self.animate:
              if not self.size_change:
                for n in range(5):
                  time.sleep(0.02)
                  self.rect.x -= 1
                  self.rect.y -= 1
                  self.rect.width += 2
                  self.rect.height += 2
                  self.draw(DISPLAY)
                  pygame.display.update()
                self.size_change = True
        else:
          if self.animate:
            if self.size_change:
              self.size_change = False
              '''for n in range(5):
                self.rect.width -= 2
                self.rect.height -= 2
                self.rect.y += 1
                self.rect.x += 1
                self.draw(DISPLAY)
                pygame.display.update()'''
              self.rect.width -= 10
              self.rect.height -= 10
              self.rect.y += 5
              self.rect.x += 5
          self.colour = self.real_col
    if event.type == pygame.MOUSEBUTTONDOWN:
        if self.isOver(pygame.mouse.get_pos()):
            self.pressed = True
    