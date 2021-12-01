import sys, pygame
import numpy as np
import random
pygame.init()
class Snake():
    def __init__(self,snake_x,snake_y):
        self.pos = [[snake_y, snake_x],
                    [snake_y, snake_x-1],
                    [snake_y, snake_x-2]]
        self.snake_image = pygame.image.load("Snake_Piece.png")
        self.rects = []

    def update_snake(self):
        self.rects = []
        for x in range(len(self.pos)):
            snake_coords = coord_func(self.pos[x])
            self.rects.append(pygame.Rect(self.snake_image.get_rect(center=(snake_coords[0], snake_coords[1]))))
        for x in range(len(self.rects)):

            screen.blit(snake.snake_image, self.rects[x])

def coord_func(par):
    x = par[0]
    y = par[1]
    return [30+y*60,30+x*60]

def game_over(score):
    print("Game Over\nFinal Score: " + str(score))

def score_update(score):

    text_string = "Score: " + str(score)
    text = font.render(text_string, True, green, )
    textRect = text.get_rect()
    textRect.center = (coord_func([1,1]))
    screen.blit(text, textRect)

def move(snake,food,key,score):
    new_head = [snake.pos[0][0] , snake.pos[0][1]]
    if key == "DOWN":
        new_head[0] += 1
    if key == "UP":
        new_head[0] -= 1
    if key == "LEFT":
        new_head[1] -= 1
    if key == "RIGHT":
        new_head[1] += 1
    snake.pos.insert(0,new_head)
    if snake.pos[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, grid_size - 1),
                random.randint(1, grid_size - 1)
            ]
            food = nf if nf not in snake.pos else None
            score += 100
    else:
        snake.pos.pop()
    return snake , food ,score





grid_size = 15
black = 0, 0, 0
green = (0, 255, 0)
font = pygame.font.Font('freesansbold.ttf', 36)
board = np.zeros(shape=(grid_size,grid_size))
size = width, height = 60 * grid_size , 60 * grid_size
screen = pygame.display.set_mode(size)

score = 0
snake_x = 4
snake_y = 4

food = [random.randint(1,grid_size-1),random.randint(1,grid_size-1)]
snake = Snake(snake_x,snake_y)

food_image = pygame.image.load("Food_Piece.png")
key = "RIGHT"
while 1:
    if snake.pos[0][0] in [0, grid_size] or snake.pos[0][1] in [0, grid_size] or snake.pos[0] in snake.pos[1:]:
        game_over(score)
        quit()
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key = "UP"
            if event.key == pygame.K_DOWN:
                key = "DOWN"

            if event.key == pygame.K_RIGHT:
                key = "RIGHT"
            if event.key == pygame.K_LEFT:
                key = "LEFT"
    snake , food , score =  move(snake,food,key,score)
    snake.update_snake()
    food_coords = coord_func(food)
    screen.blit(food_image,pygame.Rect(food_image.get_rect(center=(food_coords[0],food_coords[1]))))
    score_update(score)

    pygame.time.wait(100)
    pygame.display.flip()