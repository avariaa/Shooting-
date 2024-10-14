import random
import time
from Player.Position import *
from math import *

seed_a = time.time()
print(seed_a)

HEIGHT = 500
WIDTH = 500


def Distance(pos1: Position, pos2: Position):
    return ((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2) ** (1 / 2)


class Asteroid:
    a = ['small', 'medium', 'big']

    def __str__(self):
        return f"{self.position.x} {self.position.y}"

    def __init__(self, speed=100,
                 x_start=-510,
                 y_start=-250, radius=0, damage=0):
        self.x_start = x_start
        self.y_start = y_start
        global seed_a
        random.seed(seed_a)
        self.size = self.a[random.randint(0, len(self.a) - 1)]
        if self.size == self.a[0]:
            self.radius = radius + 10
            self.speed = speed
            self.damage = damage + 10
        elif self.size == self.a[1]:
            self.radius = radius + 25
            self.speed = speed + 20
            self.damage = damage + 15
        else:
            self.radius = radius + 40
            self.speed = speed + 40
            self.damage = damage + 25
        seed_a += 1000
        self.position = self.random_position()

    def is_out_of_bounds(self):
        return self.position.x >= 110

    def random_position(self):
        return Position(random.randint(self.x_start - WIDTH, self.x_start),
                        random.randint(self.y_start, -self.y_start))

    def to_start(self):
        self.position = self.random_position()
        self.position.x = self.x_start
        self.position.y = random.randint(self.y_start, -self.y_start)

    def CheckBounds(self):
        if self.is_out_of_bounds():
            self.to_start()

    def move(self, delta_time):
        self.position.x += self.speed * delta_time
        self.CheckBounds()


class AsteroidModel:
    def __init__(self, number_of_asteroids=15):
        self.number_of_asteroids = number_of_asteroids
        self.asteroids = [Asteroid() for i in range(number_of_asteroids)]

    def check_collision(self):
        for asteroid1 in self.asteroids:
            for asteroid2 in self.asteroids:
                if asteroid1 == asteroid2:
                    pass
                else:
                    while Distance(asteroid1.position, asteroid2.position) <= (asteroid1.radius + asteroid2.radius):
                        if asteroid1.position.y > asteroid2.position.y:
                            asteroid1.position.y += 1
                            asteroid2.position.y -= 1
                        else:
                            asteroid1.position.y -= 1
                            asteroid2.position.y += 1

    def move(self, delta_time):
        for asteroid in self.asteroids:
            if asteroid.position.x < asteroid.x_start:
                self.check_collision()
            asteroid.move(delta_time)
