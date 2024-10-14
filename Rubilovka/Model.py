from Asteroid.AsteroidModel import *
from Player.PlayerModel import *
from Player.Position import *
from View import *

def Distance(pos1: Position, pos2: Position):
    return ((pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2)**(1/2)


class Model:
    def __init__(self, models, x=0, y=0, x_difference=-100):
        self.models = models
        self.position = Position(x, y)
        self.x_difference = x_difference

    def get_model(self, model_class):
        return self.models[model_class]


    def MoveRectangle(self):
        self.position.x = self.x_difference















