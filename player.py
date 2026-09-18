from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED,PLAYER_SHOOT_SPEED
import pygame
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self,x: int,y: int) ->None:
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0.0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen,"white",self.triangle(),LINE_WIDTH)

    def rotate(self,dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0,1)
        rotate_vector = unit_vector.rotate(self.rotation)
        rotate_speed_vector = rotate_vector * PLAYER_SPEED * dt
        self.position += rotate_speed_vector

    def shoot(self):
        shot = Shot(self.position[0],self.position[1])
        unit_vector = pygame.Vector2(0,1)
        rotate_vector = unit_vector.rotate(self.rotation)
        shot_speed = rotate_vector * PLAYER_SHOOT_SPEED
        #print(shot_speed)
        shot.velocity = shot_speed
       