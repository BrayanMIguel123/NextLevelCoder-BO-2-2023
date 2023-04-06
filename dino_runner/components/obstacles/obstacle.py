from pygame.Sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
   def __init__(self, image, animated = False):
       self.image = image
       self.rect = self.image.get_rect()
       self.rect.x = SCREEN_WIDTH
       self.animated = animated

   def update(self, game_speed, obstacles):
       self.rect_x -= game_speed
       if self.rect.x < 0:
           obstacles.pop()

       if self.animated:
           self.animate()

   def draw(self, screen):
       screen.blit(self.image, self.rect)

   def animate(self):
       pass

    



