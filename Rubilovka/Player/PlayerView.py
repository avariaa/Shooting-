import time
import tkinter
import tkinter as tk
from math import *

from Player.Bullet import Bullet
from View import *

class PlayerView:
    center_x, center_y = 450, 250

    def __init__(self, root: tk.Tk, canvas: tk.Canvas):
        self.root = root
        self.canvas = canvas
        self.h = 25
        self.player = self.CreatePlayer(self.center_x, self.center_y, pi)

        self.bullets_view = []
        self.bullets_copy: list[Bullet] = []


    def create_bullet(self):
        return self.canvas.create_oval(0, 0, 0, 0,fill = 'red', outline='#000000')


    def show_bullets(self, bullets_data):
        self.bullets_copy = bullets_data
        while len(self.bullets_copy) > len(self.bullets_view):
            self.bullets_view.append(self.create_bullet())

        i = 0
        for bullet in self.bullets_copy:
            x = bullet.position.x + self.center_x
            y = bullet.position.y + self.center_y
            self.canvas.coords(self.bullets_view[i],
                               x + bullet.radius, y + bullet.radius,
                               x - bullet.radius, y - bullet.radius)
            i += 1

        # while len(self.bullets_view) > i:
        #      self.canvas.delete(self.bullets_view[i])




    def CreatePlayer(self, x, y, angle):
        return self.canvas.create_polygon(x + self.h * cos(angle), y + self.h * sin(angle),
                                            x + 2 * self.h * cos(angle+2*pi/3), y + 2 * self.h * sin(angle+2*pi/3),
                                            x + 2 * self.h * cos(angle-2*pi/3), y + 2 * self.h * sin(angle-2*pi/3), fill = '#50026E', outline='#000000')

    def ShowPos(self, position, angle):
        x = position.x + self.center_x
        y = position.y + self.center_y
        pos = [x + self.h * cos(angle), y + self.h * sin(angle),
        x + 2 * self.h * cos(angle+2*pi/3), y + 2 * self.h * sin(angle+2*pi/3),
        x + 2 * self.h * cos(angle-2*pi/3), y + 2 * self.h * sin(angle-2*pi/3)]
        self.canvas.coords(self.player, *pos)

