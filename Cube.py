import pygame
import random

class Cube(object):

    def __init__(self, start, dirX=1, dirY=0, color=(255,0,0)):
        self.pos = start
        self.dirX = dirX
        self.dirY = dirY
        self.color = color

    def move(self, dirX, dirY):
        self.dirX = dirX
        self.dirY = dirY
        self.pos = (self.pos[0] + self.dirX, self.pos[1] + self.dirY)

    def draw(self, surface, dist):
        
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i * dist +1, j * dist +1, dist -2, dist -2))

 