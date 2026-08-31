import pygame

WIDTH, HEIGHT = 1080, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Fighters")
BG = pygame.transform.scale(pygame.image.load("Assets/space.png"), (WIDTH, HEIGHT))
SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT = 60, 40
#color theme
RED = (255,0,0)
BLUE =(0,255,0)
GREEN =(0,0,255)
#game fps
FPS = 60
#player variables
RED_SPACESHIP_IMAGE = pygame.image.load("Assets/spaceship_red.png")
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT))
YELLOW_SPACESHIP_IMAGE = pygame.image.load("Assets/spaceship_yellow.png")
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT))

def draw():
    WIN.blit(BG,(0,0))
    WIN.blit(RED_SPACESHIP,(0,HEIGHT/2))
    WIN.blit(YELLOW_SPACESHIP,(1020, HEIGHT/2))
    pygame.display.update()

def run_game():
    fps_clock = pygame.time.Clock()
    run = True
    while run:
        fps_clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            draw()
                
                
    pygame.quit()