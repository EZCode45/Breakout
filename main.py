import sys

import pygame
from pygame.locals import QUIT
from pygame.sprite import Group

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
velocity = 1
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
    super().__init__()
    self.image = pygame.Surface([width, height])
    pygame.draw.rect(self.image, color, [0, 0, width, height])
    self.rect = self.image.get_rect()
  def move_left(self, pixels):
    self.rect.x += pixels
    if self.rect.x > WIDTH - wall_width - paddle_width:
      self.rect.x = WIDTH - wall_width - paddle_width
  def move_right(self, pixels):
    self.rect.x -= pixels
    if self.rect.x < wall_width:
      self.rect.x = wall_width

class Ball(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()
    self.image = pygame.Surface([width, height])
    pygame.draw.rect(self.image, color, [0, 0, width, height])
    self.rect = self.image.get_rect()
    self.velocity = [velocity, velocity]
  def update(self, *args, **kwargs):
    self.rect.x += self.velocity[0]
    self.rect.y += self.velocity[1]
  def bounce(self):
    self.velocity[0] = self.velocity[0]
    self.velocity[1] = -self.velocity[1]

paddle = Paddle(BLUE,paddle_width, paddle_height)
paddle.rect.x = WIDTH//2 - paddle_width//2
paddle.rect.y = HEIGHT - 65

ball = Ball(WHITE, 10, 10)
ball.rect.x = WIDTH//2 - 5
ball.rect.y = HEIGHT// 2 - 5
all_sprites_group.add(ball)
all_sprites_group.add(paddle)
wall_width = 16  
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    all_sprites_group.update()  
    SCREEN.fill(BLACK)
    all_sprites_group.draw(SCREEN)
    pygame.display.update()
    clock.tick(FPS)