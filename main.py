import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
SPACESHIP_WIDHT, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, 
                                                                (SPACESHIP_WIDHT, SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, 
                                                                (SPACESHIP_WIDHT, SPACESHIP_HEIGHT)), 270)
pygame.display.set_caption("Spaceship Morning")

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (300, 100))
    WIN.blit(RED_SPACESHIP, (700, 100))
    pygame.display.update()

def main():
    run = True
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()