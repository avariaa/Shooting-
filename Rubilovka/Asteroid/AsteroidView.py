import random
import tkinter as tk
from PIL import Image, ImageTk

import Asteroid.AsteroidModel

CENTER_X, CENTER_Y = 450, 250

def create_tk_image(size):
    angle = random.randint(0,20)
    if size == 'small':
        image_path = 'C:/Users/1/PycharmProjects/pythonProject18/Asteroid/asteroid3.png'
        reduce_factor = 2
    elif size == 'medium':
        image_path = 'C:/Users/1/PycharmProjects/pythonProject18/Asteroid/asteroid2.png'
        reduce_factor = 10
    elif size == 'big':
        image_path = 'C:/Users/1/PycharmProjects/pythonProject18/Asteroid/asteroid_1.png'
        reduce_factor = 10

    image_pil = Image.open(image_path)
    return ImageTk.PhotoImage(Image.open(image_path))


class AsteroidView:
    def __init__(self, root: tk.Tk, canvas: tk.Canvas):
        self.root = root
        self.canvas = canvas

        self.small_asteroid = create_tk_image('small')

        #self.canvas.create_image(100, 100, image=self.asteroid_tk_small)


    def Start(self, number_of_asteroids, asteroids_data: list[Asteroid.AsteroidModel.Asteroid]):
        self.number_of_asteroids = number_of_asteroids
        self.image_list = [create_tk_image(asteroids_data[i].size) for i in range(number_of_asteroids)]
        self.asteroids = [self.CreateAsteroid(-300, -300, self.image_list[i]) for i in range(number_of_asteroids)]


    def CreateAsteroid(self, x, y, image, radius=30):
        return self.canvas.create_image(x + radius, y + radius, image=image)


    def ShowPos(self, asteroids_data: list[Asteroid.AsteroidModel.Asteroid]):
        for i in range(self.number_of_asteroids):
            radius = asteroids_data[i].radius
            x = asteroids_data[i].position.x + CENTER_X
            y = asteroids_data[i].position.y + CENTER_Y
            ''' Раньше было вот так, а мы X и Y не меняли
            x = asteroids_data[i].x
            y = asteroids_data[i].y
            '''
            self.canvas.coords(self.asteroids[i], x, y)

