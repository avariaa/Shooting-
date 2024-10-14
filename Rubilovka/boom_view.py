import tkinter

from Asteroid.AsteroidView import CENTER_X, CENTER_Y


class BoomView:
    center_x, center_y = 450, 250
    def __init__(self, x,  y, canvas):
        self.canvas: tkinter.Canvas = canvas
        self.boom_png = tkinter.PhotoImage(file='boom.png')
        #self.boom = self.canvas.create_oval(x + self.center_x - 25, y + self.center_y-25, x + self.center_x + 25, y + self.center_y+25)
        self.boom = self.canvas.create_image(x + self.center_x - 25, y + self.center_y, image=self.boom_png)


    def show_pos(self, x, y):
        self.canvas.coords(self.boom, x + CENTER_X, y + CENTER_Y)


    def delete_boom(self):
        self.canvas.delete(self.boom)