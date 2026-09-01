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
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)), 90)
PLAYER_VEL = 5

YELLOW_SPACESHIP_IMAGE = pygame.image.load("Assets/spaceship_yellow.png")
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)), 270)

def draw(yellow_player, red_player):
    WIN.blit(BG,(0,0))
    WIN.blit(RED_SPACESHIP,(red_player.x, red_player.y))
    WIN.blit(YELLOW_SPACESHIP,(yellow_player.x, yellow_player.y))
    pygame.display.update()

def run_game():
    red_player = pygame.Rect(10, HEIGHT/2, SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)
    yellow_player = pygame.Rect(1020, HEIGHT/2, SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)
    
    fps_clock = pygame.time.Clock()
    run = True
    while run:
        fps_clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_presed = pygame.key.get_pressed()
        if keys_presed[pygame.K_a] and red_player.x - PLAYER_VEL >=0:
            red_player.x -= PLAYER_VEL
        if keys_presed[pygame.K_d] and red_player.x + PLAYER_VEL + SPACE_SHIP_WIDTH <= WIDTH/2:
            red_player.x += PLAYER_VEL
        if keys_presed[pygame.K_w] and red_player.y - PLAYER_VEL >=0:
            red_player.y -= PLAYER_VEL
        if keys_presed[pygame.K_s] and red_player.y + PLAYER_VEL + SPACE_SHIP_HEIGHT <= HEIGHT-20:
            red_player.y += PLAYER_VEL
        
                
        draw(yellow_player, red_player)
                
                
    pygame.quit()