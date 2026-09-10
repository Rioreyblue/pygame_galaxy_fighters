import pygame
pygame.font.init()

WIDTH, HEIGHT = 1080, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Fighters")
BG = pygame.transform.scale(pygame.image.load("Assets/space.png"), (WIDTH, HEIGHT))
SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT = 60, 40
#color theme
RED = (255,0,0)
BLUE =(0,255,0)
GREEN =(0,0,255)
BLACK = (0,0,0)
#game border
BORDER = pygame.Rect(WIDTH//2 - 12, 0, 5, HEIGHT)
#game fps
FPS = 60
#player variables
PLAYER_VEL = 5
RED_SPACESHIP_IMAGE = pygame.image.load("Assets/spaceship_red.png")
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)), 90)

YELLOW_SPACESHIP_IMAGE = pygame.image.load("Assets/spaceship_yellow.png")
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)), 270)

RED_HIT = pygame.USEREVENT+1
YELLOW_HIT = pygame.USEREVENT+2

#BULLETS 
BULLETS_VEL = 7
MAX_BULLETS = 3

HEALTH_FONT = pygame.font.SysFont('sans-serif', 40)
WINNER_FONT = pygame.font.SysFont('poppins', 100)