import pygame
import random
from dino import Dino
from enemy import *

def dino_game():
    # Frame mula-mula
    max_fps = 30
    frame = 0

    # Tinggi jalan
    road_y = 50

    # Inisialisasi objek
    dino = Dino(road_y)
    enemy = Enemy(road_y)

    while True:
        # Tampilkan latar belakang
        display.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dino.jump()
                elif event.key == pygame.K_DOWN:
                    dino.duck()
            elif event.type == pygame.KEYUP:
                dino.walk()

        if enemy.exist == False:
            enemy_type = random.randrange(0, 2)
            if enemy_type == 0:
                enemy = Snail(road_y)
            elif enemy_type == 1:
                enemy = Spike(road_y)
            elif enemy_type == 2:
                enemy = Fly(road_y)

        dino.show(display, frame)
        enemy.show(display, frame)
        pygame.display.update()

        # Atur framerate
        fps.tick(max_fps)
        frame = (frame + 1) % max_fps

if __name__ == "__main__":
    # Inisialisasi pygame
    pygame.init()
    pygame.mixer.init()

    # Inisialisasi dino game
    pygame.display.set_caption("Bellatrix's Dino Game")
    background = pygame.image.load("assets/background_01.png")
    display = pygame.display.set_mode((800, 600))
    fps = pygame.time.Clock()

    # Panggil dino game
    dino_game()
    pygame.quit()