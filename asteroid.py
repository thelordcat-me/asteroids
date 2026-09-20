from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            value = random.uniform(20.0, 30.0)
            new_astorid_vector1 = self.velocity.rotate(value)
            new_astorid_vector2 = self.velocity.rotate(-value)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_astorid1 = Asteroid(self.position[0],self.position[1],new_radius)
            new_astorid2 = Asteroid(self.position[0],self.position[1],new_radius)
            new_astorid1.velocity = new_astorid_vector1 * 1.2
            new_astorid2.velocity = new_astorid_vector2 * 1.2