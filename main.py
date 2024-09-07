import sys

import pygame
from pygame.locals import QUIT
from pygame.sprite import _Group

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
paddle_width = 54
paddle_height = 20
all_sprites_group= pygame.sprite.Group()

class Brick(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    self.image = pygame.Surface([width, height])
    super().__init__()
    pygame.draw.rect(self.image, color, [0, 0, width, height])
    self.rect = self.image.get_rect()
    
class Paddle(pygame.sprite.Sprite):
  def __init__(self,color, width, height):
    self.image = pygame.Surface([width, height])
    pygame.draw.rect(self.image, color, [0, 0, width, height])
    self.rect = self.image.get_rect()
  def move_right(self, pixels):
    self.rect.x += pixels
    if self.rect.x > WIDTH - wall_width - paddle_width:
      self.rect.x = WIDTH - wall_width - paddle_width
  def move_right(self, pixels):
    self.rect.x -= pixels
    if self.rect.x < wall_width:
      self.rect.x = wall_width

wall_width = 16  
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    pygame.display.update()
    clock.tick(FPS)
