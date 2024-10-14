import time
import tkinter as tk
from tkinter import ttk

from Asteroid.AsteroidView import CENTER_X, CENTER_Y
from Player.boom_system import Boom
from boom_view import BoomView


class View:
    center_x, center_y = 450, 250
    def __init__(self, views):
        self.views = views
        self.root = tk.Tk()

        self.game_canvas = tk.Canvas(height=500, width=500, background='#7CD0A0', highlightbackground="black")
        self.game_canvas.grid(row=0, column=0)
        self.cosmos_of_game_canvas_png = tk.PhotoImage(file='cosmos.png')
        #self.game_canvas.create_image(0, 0, anchor="nw", image=self.cosmos_of_game_canvas_png)

        self.cosmos_of_ui_canvas_png = tk.PhotoImage(file='cosmos2.png')
        self.ui_canvas = tk.Canvas(height=100, width=500, background='black', highlightbackground="black")

        self.ui_cosmos_background = self.ui_canvas.create_image(0, 0, image=self.cosmos_of_ui_canvas_png)

        self.cosmos_background_1_x = 250
        self.cosmos_background_1 = self.game_canvas.create_image(self.cosmos_background_1_x, 250, image=self.cosmos_of_game_canvas_png)
        self.cosmos_background_2_x = -250
        self.cosmos_background_2 = self.game_canvas.create_image(self.cosmos_background_2_x, 250, image=self.cosmos_of_game_canvas_png)


        self.create_health_bar(0)
        self.ui_canvas.grid(row=1, column=0)
        self.hearts_png = tk.PhotoImage(file="hearts_boarder.png")
        self.hp_border = self.create_hearts_border()

        self.restart_btn = ttk.Button(text='restart level', command=self.restart)
        self.restart_text = ttk.Label(text="Игрок мертв:(", font=("Arial", 30))

        self.boom_list: list[BoomView] = []


    def show_booms(self, boom_data_list: list[Boom]):
        while len(boom_data_list) > len(self.boom_list):
            self.create_boom(-100, -100)

        i = 0
        for boom_data in boom_data_list:
            if boom_data.is_exist:
                self.boom_list[i].show_pos(boom_data.position.x, boom_data.position.y)
            else:
                self.boom_list[i].show_pos(-1000, -1000)
            print(boom_data.position.x, boom_data.position.y, i, "ffffff")
            i += 1


    def show_restart_menu(self):
        self.restart_btn.grid(row=0, column=0)
        self.restart_text.grid(row=0, column=0, pady=30, sticky="S")


    def delete_restart_menu(self):
        self.restart_btn.destroy()
        self.restart_text.destroy()

        self.restart_btn = ttk.Button(text='restart level', command=self.restart)
        self.restart_text = ttk.Label(text="Игрок мертв:(", font=("Arial", 30))


    def on_restart(self, restart_function):
        self.restart_function = restart_function

    def restart(self):
        self.restart_function()




    def create_health_bar(self, x):
        self.health_bar = self.ui_canvas.create_rectangle(0, 0, 380 + x, 150, fill='red')


    def create_hearts_border(self):
        return self.ui_canvas.create_image(0, 0, anchor="nw", image=self.hearts_png)


    def create_boom(self, x, y):
        self.boom_list.append(BoomView(x, y, self.game_canvas))



    def get_view(self, view_class):
        return self.views[view_class]

    def OnKeyPressed(self, function):
        self.root.bind('<KeyPress>', function)

    def OnKeyRelease(self, function):
        self.root.bind('<KeyRelease>', function)

    def OnUpdate(self, update_function):
        self.update_function = update_function

    def Update(self, delta_time):
        self.update_function(delta_time)
        self.root.update()

    def Start(self):
        delta_time = 0.02
        while True:
            time.sleep(delta_time)
            self.Update(delta_time)


    def move_backgrounds(self):
        self.cosmos_background_1_x += 1
        self.cosmos_background_2_x += 1
        if self.cosmos_background_1_x >= 750:
            self.cosmos_background_1_x = -250
        if self.cosmos_background_2_x >= 750:
            self.cosmos_background_2_x = -250
        print(self.cosmos_background_1_x, self.cosmos_background_2_x)
        self.game_canvas.coords(self.cosmos_background_1, self.cosmos_background_1_x, 250)
        self.game_canvas.coords(self.cosmos_background_2, self.cosmos_background_2_x, 250)
