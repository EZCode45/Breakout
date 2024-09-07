import sys

import pygame
from pygame.locals import QUIT

pygame.init()
#-------------------------
WIDTH = 893
HEIGHT = 1000
screen_size = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(screen_size)
pygame.display.set_caption('breakout')
clock = pygame.time.Clock()
FPS = 120
#-------------------------
#color constants
WHITE = ('#ffffff')
GREY = ('#a8a8a8')
BLACK = ('#000000')
BLUE = ('#000a73')
RED = ('#820000')
ORANGE = ('#ff3c00')
GREEN = ('#00ba09')
YELLOW = ('#fffb00')
#-------------------------

score = 0
balls = 1
velocity = 4

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    pygame.display.update()
    clock.tick(FPS)
