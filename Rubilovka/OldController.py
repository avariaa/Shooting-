from Player.boom_system import *
from Player.PlayerController import *
from Model import *


class OldController:

    def __init__(self, model, view, controllers):
        self.count_of_dead = 0
        self.model = model
        self.player_model: PlayerModel = self.model.get_model(PlayerModel)
        self.asteroid_model: AsteroidModel= self.model.get_model(AsteroidModel)
        self.view = view
        self.controllers = controllers
        self.player_controller = self.controllers[PlayerController]

        self.view.OnKeyPressed(self.PressListener)
        self.view.OnKeyRelease(self.ReleaseListener)
        self.view.OnUpdate(self.Update)
        self.view.on_restart(self.restart)

        self.view.get_view(PlayerView).h = self.model.get_model(PlayerModel).radius

        self.boom_system = BoomSystem()

        self.view.Start()

    def restart(self):
        self.player_model.hit_point = 3
        self.update_health_bar()
        self.view.delete_restart_menu()
        self.player_model.__init__()
        self.asteroid_model.__init__()


    def CheckCollition(self):
        player = self.model.get_model(PlayerModel)
        for asteroid in self.asteroid_model.asteroids:
            if Distance(player.position, asteroid.position) <= (asteroid.radius + player.radius):
                player.hit_point -= 1
                self.asteroid_to_start(asteroid)
                self.update_health_bar()
                self.boom_system.create_boom(player.position.x, player.position.y)

            if player.hit_point == 0:
                self.view.show_restart_menu()
                print('он мертв')
            for bullet in self.player_model.bullets:
                if Distance(bullet.position, asteroid.position) <= (asteroid.radius + bullet.radius):
                    self.asteroid_to_start(asteroid)
                    self.boom_system.create_boom(bullet.position.x, bullet.position.y)
                    #self.view.create_boom(bullet.position.x, bullet.position.y)
                    self.destroy_bullet(bullet)



    def delete_health_bar(self):
        return self.view.ui_canvas.delete(self.view.health_bar)

    def update_health_bar(self):
        self.delete_health_bar()
        self.view.create_health_bar(-127 * (3 - self.player_model.hit_point))
        self.view.create_hearts_border()

    def asteroid_to_start(self, asteroid: Asteroid):
        asteroid.to_start()

    def Update(self, delta_time):
        #print(self.player_model.hit_point)
        if self.player_model.IsAlive():
            self.view.move_backgrounds()
        else:
            delta_time = 0
        for controller in self.controllers:
            self.controllers[controller].Update(delta_time)
        self.CheckCollition()
        self.boom_system.update(delta_time)

        self.view.show_booms(self.boom_system.booms_list)
        player_view: PlayerView = self.view.get_view(PlayerView)
        player_view.show_bullets(self.player_model.bullets)
        player_view.ShowPos(self.model.get_model(PlayerModel).position,
                                               self.model.get_model(PlayerModel).angle)

    def PressListener(self, event: tkinter.Event):
        print(event)
        delta_time = 0.1
        print(event.keysym, event.x_root, event.y_root, event.x, event.y)
        if event.keysym == 'Up':
            self.player_model.move_direction = 1
        if event.keysym == 's':
            self.model.get_model(PlayerModel).Shoot()
        if event.keysym == 'Down':
            self.player_model.move_direction = -1
        if event.keysym == 'Left':
            self.player_model.turn_direction = 'left'
        if event.keysym == 'Right':
            self.player_model.turn_direction = 'right'

    def ReleaseListener(self, event: tkinter.Event):
        delta_time = 0.1
        if event.keysym == 'Up':
            self.player_model.move_direction = 0
        if event.keysym == 'Down':
            self.player_model.move_direction = 0
        if event.keysym == 'Left':
            self.player_model.turn_direction = 'stop'
        if event.keysym == 'Right':
            self.player_model.turn_direction = 'stop'

    def destroy_bullet(self, bullet: Bullet):
        self.player_model.destroy_bullet(bullet)
