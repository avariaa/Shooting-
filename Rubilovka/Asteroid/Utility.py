from Player.Position import *

HEIGHT = 500
WIDTH = 500

def Distance(pos1: Position, pos2: Position):
    return ((pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2)**(1/2)
