import pygame
import random
from Cube import Cube

class Snake(object):
    body = []
    turns = {}

    def __init__(self, pos, color, rows):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirX = 1
        self.dirY = 0
        self.rows = rows
    
    def draw(self, surface, dist):
        for i, c in enumerate(self.body):
            c.draw(surface, dist)
    
    def addCube(self):
        tail = self.body[-1]
        dx = tail.dirX
        dy = tail.dirY

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dirX = dx
        self.body[-1].dirY = dy

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys = pygame.key.get_pressed()
           
            if keys[pygame.K_LEFT]:
                self.dirX, self.dirY = -1, 0
            if keys[pygame.K_RIGHT]:
                self.dirX, self.dirY = 1, 0
            if keys[pygame.K_UP]:
                self.dirX, self.dirY = 0, -1
            if keys[pygame.K_DOWN]:
                self.dirX, self.dirY = 0, 1
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                
            self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

        for i, c in enumerate(self.body):
            pos = c.pos[:]
            if pos in self.turns:
                turn = self.turns[pos]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(pos)
            else:
                if c.dirX == -1 and c.pos[0] <= 0:
                     c.pos = (self.rows-1, c.pos[1])
                elif c.dirX == 1 and c.pos[0] >= self.rows-1:
                     c.pos = (0,c.pos[1])
                elif c.dirY == 1 and c.pos[1] >= self.rows-1:
                     c.pos = (c.pos[0], 0)
                elif c.dirY == -1 and c.pos[1] <= 0: 
                    c.pos = (c.pos[0],self.rows-1)
                else: 
                    c.move(c.dirX,c.dirY)
    
    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

