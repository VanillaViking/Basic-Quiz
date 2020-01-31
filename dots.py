import pygame
from brain import *
import math
#from obstacles import *

class dot():
    def __init__(self, x,y):
        self.dead = False
        self.goal_reached = False
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.acc_x = 0
        self.acc_y = 0
        self.brain_step = 0
        self.fitness = 0
        self.col = (0,0,0)
        self.brain = brain(500)
        self.rect = pygame.Rect(self.x,self.y, 15,15)
    def draw(self, display):
        pygame.draw.rect(display, (0,0,0), (self.x,self.y, 30,30))
    
    def move(self, DISPLAY):
        self.rect = pygame.Rect(self.x,self.y, 30,30)
        if not self.dead and not self.goal_reached:
            if self.brain_step < len(self.brain):
                self.acc_x = self.brain[self.brain_step][0]
                self.acc_y = self.brain[self.brain_step][1]
                self.brain_step += 1
            else:
                self.goal_reached = True
            
            self.vel_x += self.acc_x
            self.vel_y += self.acc_y
            self.x += self.vel_x
            self.y += self.vel_y
            
            if self.vel_x > 10:         #VELOCITY LIMITS
                self.vel_x = 10
            if self.vel_x < -10:
                self.vel_x = -10
            
            if self.vel_y > 10:
                self.vel_y = 10
            if self.vel_y < -10:
                self.vel_y = -10
        
        else:
            self.acc_x = self.acc_y = self.vel_x = self.vel_y = 0
        
        if (self.x <= 0 or self.y <= 0 or self.x >= DISPLAY.get_width() or self.y >= DISPLAY.get_height()):
            self.goal_reached = True

    def check(self, event):
        if self.rect.collidepoint(event.pos):
            self.col = (0,255,0)
            self.dead = True

