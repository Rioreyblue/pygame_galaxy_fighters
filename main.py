import pygame

WIDTH, HEIGHT = 1080, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Fighters")
BG = pygame.image.load("Assets/space.png",)
RED = (255,0,0)
BLUE =(0,255,0)
GREEN =(0,0,255)
FPS = 60

def draw():
    WIN.fill(GREEN)
    pygame.display.update()

def main():
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            draw()
                
                
    pygame.quit()

if __name__ == "__main__":
    main()