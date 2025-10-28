import pygame
import updates

SCREEN_SIZE=500
CLOCK_SPEED=60

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock=pygame.time.Clock()
running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill("purple")
    pygame.display.flip()
    updates.update()
    clock.tick(CLOCK_SPEED)
    
pygame.quit()