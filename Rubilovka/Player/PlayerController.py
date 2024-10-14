import tkinter

from Player.PlayerModel import *
from Player.PlayerView import *

class PlayerController:
    def __init__(self, model: PlayerModel, view: PlayerView):
        self.model = model
        self.view = view

    def Move(self, delta_time):
        self.model.Move(delta_time)
        self.view.ShowPos(self.model.position, 0)

    def Shoot(self, event: tkinter.Event):
        self.model.Shoot()

    def Update(self, delta_time):
        self.view.ShowPos(self.model.position, self.model.angle)
        self.Move(delta_time)
        self.model.Turn(delta_time)

    def Accelerate(self):
        self.model.Accelerate(1)
