from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):

    def __init__(self, image_list):
        super().__init__(image_list[0], animated=True)
        self.rect.y = 250
        self.flight_index = 0

    def aniate(self):
        super().animate()
        if self.flight_index < 5:
            self.image = BIRD[0]
        else:
            self.image = Bird[1]
        self.flight_index = (self.flight_index + 1)

        if self.flight_index >= 10:
            self.flight_index = 0
