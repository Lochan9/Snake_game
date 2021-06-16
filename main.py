import pygame
import random
x=pygame.init()

#colors
white = (255,255,255)
red = (255,0,0)
black=(0,0,0)

#create window
Game_window = pygame.display.set_mode((800,500))
pygame.display.set_caption("MY First Game")

#game specific variable
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0
snake_size = 10
fps =45
score = 0
clock = pygame.time.Clock()
food_size = 20
food_x = random.randint(0,800/2)
food_y = random.randint(0,500/2)
snake_velocity = 5
font = pygame.font.SysFont(None,55)
snk_List =[]
snk_length = 1

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    Game_window.blit(screen_text,[x,y])

def plot_snake(Game_window,color,snk_List,snake_size):
    for x,y in snk_List:
        pygame.draw.rect(Game_window,color,[x,y,snake_size,snake_size])
#loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game =True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = snake_velocity
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -snake_velocity
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = -snake_velocity
                velocity_x =0
            
            if event.key == pygame.K_DOWN:
                velocity_y = snake_velocity
                velocity_x = 0

           
    snake_x += velocity_x
    snake_y += velocity_y
            
    if abs(snake_x -food_x)<15 and abs(snake_y - food_y)<15:
        score += 1     
        food_x = random.randint(0,800/2)
        food_y = random.randint(0,500/2)
        snk_length +=5
    Game_window.fill(white)
    text_screen("Pts:- "+str(score),red,5,5)
    x=pygame.draw.rect(Game_window,red,[food_x,food_y,food_size,food_size])
    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snk_List.append(head)
    #y=pygame.draw.rect(Game_window,black,[snake_x,snake_y,snake_size,snake_size])
    plot_snake(Game_window,black,snk_List,snake_size)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
