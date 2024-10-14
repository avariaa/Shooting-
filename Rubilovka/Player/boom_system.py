from Player.Position import Position

class Boom:
    def __init__(self, x, y, destruction_time):
        self.position = Position(x, y)
        self.life_time = 0
        self.destruction_time = destruction_time
        self.is_exist = True



    def update(self, delta_time):
        self.life_time += delta_time
        if self.life_time >= self.destruction_time:
            self.is_exist = False

class BoomSystem:
    def __init__(self):
        self.booms_list: list[Boom] = []

    def update(self, delta_time):
        for boom in self.booms_list:
            boom.update(delta_time)


    def create_boom(self, x, y, destruction_time = 0.7):
        self.booms_list.append(Boom(x, y, destruction_time))