from Player.PlayerModel import *
from Player.PlayerController import *
from OldController import *
from Model import *
from Asteroid.AsteroidModel import *
from Asteroid.AsteroidView import *
from Asteroid.AsteroidContoller import *

models = {}
views = {}
controllers = {}

model = Model(models)
view = View(views)

def creat_model(model_class):
    global models
    models[model_class] = model_class()
    return models[model_class]


def creat_view(view_class):
    global views
    views[view_class] = view_class(view.root, view.game_canvas)
    return views[view_class]


def creat_MVC(model_class, view_class, controller_class):
    global controllers
    controllers[controller_class] = controller_class(creat_model(model_class),
                                                     creat_view(view_class))
    print(controllers[controller_class].view)
    return controllers[controller_class]

number_of_asteroids = 20

player_controller = creat_MVC(PlayerModel, PlayerView, PlayerController)
asteroid_controller = creat_MVC(AsteroidModel, AsteroidView, AsteroidController)

print(models, views, controllers, sep='\n')
controller = OldController(model, view, controllers)


