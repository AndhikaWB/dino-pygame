import pygame

class Enemy:
    def __init__(self, road_y):
        self.pos_x = None
        self.pos_y = 0
        self.road_y = road_y
        self.exist = False
        self.anim = None

    def show(self, display, frame):
        if self.pos_x == None:
            self.pos_x = display.get_width()
        elif self.pos_x - self.anim[0].get_width() > 0:
            self.pos_x -= 10
        else:
            self.exist = False

        frame %= len(self.anim)
        display.blit(self.anim[frame], (self.pos_x, display.get_height() - self.road_y - self.anim[0].get_height() - self.pos_y))

class Snail(Enemy):
    def __init__(self, road_y):
        super().__init__(road_y)
        self.exist = True
        self.anim = [
            pygame.image.load("assets/snail_move_01.png").convert_alpha(),
            pygame.image.load("assets/snail_move_02.png").convert_alpha()
        ]

class Spike(Enemy):
    def __init__(self, road_y):
        super().__init__(road_y)
        self.exist = True
        self.anim = [
            pygame.image.load("assets/spike_move_01.png").convert_alpha(),
            pygame.image.load("assets/spike_move_02.png").convert_alpha()
        ]

class Fly(Enemy):
    def __init__(self, road_y):
        super().__init__(road_y)
        self.exist = True
        self.pos_y = 60
        self.anim = [
            pygame.image.load("assets/fly_move_01.png").convert_alpha(),
            pygame.image.load("assets/fly_move_02.png").convert_alpha()
        ]