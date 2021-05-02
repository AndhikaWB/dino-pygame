import pygame

class Dino:
    def __init__(self, road_y):
        # Posisi dino
        self.pos_x = 70
        self.pos_y = 0
        # Ketinggian jalan
        self.road_y = road_y
        # Status dino
        self.state = "IDLE"

        self.anim = self.idle_anim = [
            pygame.image.load("assets/dino_idle_01.png").convert_alpha()
        ]

        self.walk_anim = [
            pygame.image.load("assets/dino_move_01.png").convert_alpha(),
            pygame.image.load("assets/dino_move_02.png").convert_alpha(),
            pygame.image.load("assets/dino_move_03.png").convert_alpha(),
            pygame.image.load("assets/dino_move_04.png").convert_alpha(),
            pygame.image.load("assets/dino_move_05.png").convert_alpha(),
            pygame.image.load("assets/dino_move_06.png").convert_alpha(),
            pygame.image.load("assets/dino_move_07.png").convert_alpha(),
            pygame.image.load("assets/dino_move_08.png").convert_alpha(),
            pygame.image.load("assets/dino_move_09.png").convert_alpha(),
            pygame.image.load("assets/dino_move_10.png").convert_alpha(),
            pygame.image.load("assets/dino_move_11.png").convert_alpha()
        ]

        self.jump_anim = [
            pygame.image.load("assets/dino_jump_01.png").convert_alpha()
        ]

        self.duck_anim = [
            pygame.image.load("assets/dino_duck_01.png").convert_alpha()
        ]

        self.hurt_anim = [
            pygame.image.load("assets/dino_hurt_01.png").convert_alpha()
        ]

    def show(self, display, frame):
        if self.state == "JUMP":
            if self.pos_y < 120:
                self.pos_y += 5
            else:
                self.state = "WALK"
        elif self.state == "WALK":
            if self.pos_y > 0:
                self.pos_y -= 5
            else:
                self.anim = self.walk_anim

        frame %= len(self.anim)
        display.blit(self.anim[frame], (self.pos_x, display.get_height() - self.road_y - self.anim[0].get_height() - self.pos_y))

    def walk(self):
        # Cegah jalan saat melompat
        if self.pos_y <= 0:
            self.pos_y = 0
            self.state = "WALK"
            self.anim = self.walk_anim

    def jump(self):
        # Cegah lompat berkali-kali
        if self.pos_y == 0:
            self.state = "JUMP"
            self.anim = self.jump_anim

    def duck(self):
        # Cegah jongkok saat melompat
        if self.pos_y == 0:
            self.pos_y -= 20
            self.state = "DUCK"
            self.anim = self.duck_anim