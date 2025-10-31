import pygame
import utils

Grid = utils.Grid
Point = utils.Point

SCREEN_HEIGHT:int = 500
SCREEN_WIDTH:int = 500
GRID_HEIGHT:int = 50
GRID_WIDTH:int = 50
FPS = 10

pygame.init()
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
grid_screen = pygame.Surface(size=(GRID_WIDTH, GRID_HEIGHT))
clock = pygame.time.Clock()

size_point = Point(x=GRID_WIDTH, y=GRID_HEIGHT)
grid = Grid(size=size_point)
running = True
pixel_input_pos: Point = Point(25, 25)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pixel_input_pos.y=pixel_input_pos.y-1
    if keys[pygame.K_DOWN]:
        pixel_input_pos.y=pixel_input_pos.y+1
    pixel_input_pos.clamp_point(Point(1,1), Point(grid.size.x -2, grid.size.y -2))
    if keys[pygame.K_LEFT]:
        pixel_input_pos.x=pixel_input_pos.x-1
    if keys[pygame.K_RIGHT]:
        pixel_input_pos.x=pixel_input_pos.x+1
    pixel_input_pos.clamp_point(Point(1,1), Point(grid.size.x -2, grid.size.y -2))
    
    grid.set_cell(pixel_input_pos, True)
    grid.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()