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
BULLETS_VEL = 10
MAX_BULLETS = 3

def draw(yellow_player, red_player, red_bullets, yellow_bullets):
    WIN.blit(BG,(0,0))
    WIN.blit(RED_SPACESHIP,(red_player.x, red_player.y))
    WIN.blit(YELLOW_SPACESHIP,(yellow_player.x, yellow_player.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, "red", bullet)
        
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, "yellow", bullet)
        
    #border
    pygame.draw.rect(WIN, BLACK, BORDER)
    pygame.display.update()
    
def red_handle_movements(keys_presed, red_player):
        if keys_presed[pygame.K_a] and red_player.x - PLAYER_VEL >=0:
            red_player.x -= PLAYER_VEL
        if keys_presed[pygame.K_d] and red_player.x + PLAYER_VEL + SPACE_SHIP_WIDTH <= WIDTH/2:
            red_player.x += PLAYER_VEL
        if keys_presed[pygame.K_w] and red_player.y - PLAYER_VEL >=0:
            red_player.y -= PLAYER_VEL
        if keys_presed[pygame.K_s] and red_player.y + PLAYER_VEL + SPACE_SHIP_HEIGHT <= HEIGHT-20:
            red_player.y += PLAYER_VEL
            
def yellow_handle_movements(keys_presed, yellow_player):
        if keys_presed[pygame.K_LEFT] and yellow_player.x - PLAYER_VEL >= WIDTH/2:
            yellow_player.x -= PLAYER_VEL
        if keys_presed[pygame.K_RIGHT] and yellow_player.x + PLAYER_VEL + SPACE_SHIP_WIDTH <= WIDTH:
            yellow_player.x += PLAYER_VEL
        if keys_presed[pygame.K_UP] and yellow_player.y - PLAYER_VEL >=0:
            yellow_player.y -= PLAYER_VEL
        if keys_presed[pygame.K_DOWN] and yellow_player.y + PLAYER_VEL + SPACE_SHIP_HEIGHT <= HEIGHT-20:
            yellow_player.y += PLAYER_VEL

def handle_bullets(red_player, yellow_player, red_bullets, yellow_bullets):
    for bullet in red_bullets:
        bullet.x += BULLETS_VEL
        if yellow_player.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
            
    for bullet in yellow_bullets:
        bullet.x -= BULLETS_VEL
        if red_player.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
    

def run_game():
    red_player = pygame.Rect(10, HEIGHT/2, SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)
    yellow_player = pygame.Rect(1020, HEIGHT/2, SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []
    
    fps_clock = pygame.time.Clock()
    run = True
    while run:
        fps_clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red_player.x + red_player.width, red_player.y + red_player.height//2 -2, 10, 5)
                    red_bullets.append(bullet)
                    
                if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow_player.x - yellow_player.width, yellow_player.y - yellow_player.height//2 -2, 10, 5)
                    yellow_bullets.append(bullet)
                    
        # print(red_bullets)
        keys_presed = pygame.key.get_pressed()
        red_handle_movements(keys_presed, red_player)
        yellow_handle_movements(keys_presed, yellow_player)
              
        draw(yellow_player, red_player)
                
                
    pygame.quit()