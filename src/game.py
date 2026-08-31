import pygame

WIDTH, HEIGHT = 1080, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Fighters")
BG = pygame.transform.scale(pygame.image.load("Assets/space.png"), (WIDTH, HEIGHT))
RED = (255,0,0)
BLUE =(0,255,0)
GREEN =(0,0,255)
FPS = 60

def draw():
    WIN.blit(BG,(0,0))
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