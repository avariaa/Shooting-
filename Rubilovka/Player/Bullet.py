from math import *

from Player.Position import Position


class Bullet:
    def __init__(self, angle=pi, x=0, y=0, speed=200, radius=2, x_bound=-510):
        self.radius = radius
        self.angle = angle
        self.position = Position(x, y)
        self.x_bound = x_bound
        self.speed = speed


    def check_bounds(self):
        if self.position.x <= self.x_bound:
            self.destroy_bullet()


    def Move(self, delta_time):
        self.position.x += self.speed * delta_time * cos(self.angle)
        self.position.y += self.speed * delta_time * sin(self.angle)
        self.check_bounds()


    def destroy_bullet(self):
        self.position.x = 500
        self.speed = 0