import pygame
import random
from Snake import Snake
from Cube import Cube

       
def redrawWindow(window, dist):
    global snake, food
    window.fill((0,0,0))  
    snake.draw(window, dist)
    food.draw(window, dist)
    pygame.display.update()  

def randomFood(rows, item):
    positions = item.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len( list( filter(lambda z : z.pos ==(x,y), positions))) > 0:
            continue
        else:
            break
    
    return (x,y)

def main(w, rows):
    global snake, food
    flag = True
    window = pygame.display.set_mode((w, w))    
    snake = Snake((10,10),(255,0,0), rows)
    clock = pygame.time.Clock()

    food = Cube(randomFood(rows, snake), color=(0,255,0))

    while flag:
        pygame.time.delay(10)
        clock.tick(10)
        snake.move()

        if snake.body[0].pos == food.pos:
            snake.addCube()
            food = Cube(randomFood(rows, snake), color=(0,255,0))

        for x in range(len(snake.body)):
            if snake.body[x].pos in list(map(lambda z:z.pos,snake.body[x+1:])): 
                print('Score: ', len(snake.body))
                snake.reset((10,10))
                break
        redrawWindow(window, w//rows)
    
    


main(500, 20)