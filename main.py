import pygame
import updates
import screen

SCREEN_SIZE=720
CLOCK_SPEED=60

pygame.init()
screen.init(SCREEN_SIZE)
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