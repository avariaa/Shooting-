from math import *

from Player.Bullet import *
from Player.Position import *

HEIGHT = 500
WIDTH = 500


class PlayerModel:
    move_direction = 0
    turn_direction = 'stop'

    def __init__(self, angle=pi, x=0, y=0, speed=200, hit_point=3, speed_turning=2, radius=25, y_bound=250):
        self.radius = radius
        self.angle = angle
        self.position = Position(x, y)
        self.y_bound = y_bound
        self.speed = speed
        self.hit_point = hit_point
        self.speed_turning = speed_turning

        self.bullets: list[Bullet] = []




    def Shoot(self):
        self.bullets.append(Bullet(angle=self.angle, x=self.position.x, y=self.position.y))
        print('Пиу пиу пиу')

    def Turn(self, delta_time):
        if self.turn_direction == 'right':
            self.angle = self.angle + self.speed_turning * delta_time
        elif self.turn_direction == 'left':
            self.angle = self.angle - self.speed_turning * delta_time

    def TurnRight(self, delta_time):
        self.Turn(delta_time, 'right')

    def TurnLeft(self, delta_time):
        self.Turn(delta_time, 'left')

    def Move(self, delta_time):
        if self.move_direction == 1:
            self.position.y -= self.speed * delta_time
        if self.move_direction == -1:
            self.position.y += self.speed * delta_time
        self.CheckBounds()

        for bullet in self.bullets:
            bullet.Move(delta_time)




    def IsOutOfBoundTop(self):
        return self.position.y < -290


    def IsOutOfBoundBottom(self):
        return self.position.y > 290


    def ToBottom(self):
        self.position.y = self.y_bound + self.radius


    def ToTop(self):
        self.position.y = -(self.y_bound + self.radius)


    def CheckBounds(self):
        if self.IsOutOfBoundTop():
            self.ToBottom()
        elif self.IsOutOfBoundBottom():
            self.ToTop()


    def IsAlive(self):
        if self.hit_point <= 0:
            return False
        else:
            return True

    def destroy_bullet(self, bullet: Bullet):
        bullet.destroy_bullet()
