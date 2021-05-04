import pygame
import random

from menu import Menu
from dino import Dino
from enemy import Enemy, Snail, Spike, Fly

def dino_game():
    # Frame mula-mula
    min_fps = 30
    max_fps = 30
    frame = 0

    # Ketinggian jalan
    road_y = 50

    # Instansiasi objek
    menu = Menu()
    dino = Dino(road_y)
    enemy = Enemy(road_y)

    while True:
        # Tampilkan latar belakang
        display.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif menu.state == "RUN":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        dino.jump()
                    elif event.key == pygame.K_DOWN:
                        dino.duck()
                    elif event.key == pygame.K_ESCAPE:
                        menu.change_state("PAUSE")
                elif event.type == pygame.KEYUP:
                    dino.walk()
            elif menu.state == "PAUSE" or menu.state == "DIED":
                if event.type == pygame.KEYDOWN:
                    if menu.state == "PAUSE":
                        if event.key == pygame.K_r:
                            max_fps = menu.reset(dino, enemy, min_fps)
                        elif event.key == pygame.K_ESCAPE:
                            menu.change_state("RUN")
                    elif menu.state == "DIED":
                        max_fps = menu.reset(dino, enemy, min_fps)

        if enemy.state == "NOT_EXIST":
            max_fps = menu.add_score(max_fps)
            enemy_type = random.randint(0, 2)
            if enemy_type == 0:
                enemy = Snail(road_y)
            elif enemy_type == 1:
                enemy = Spike(road_y)
            elif enemy_type == 2:
                enemy = Fly(road_y)

        if menu.state == "RUN":
            dino.update(display, frame)
            enemy.update(display, frame)
            if dino.rect.colliderect(enemy.rect):
                menu.change_state("DIED")
                print("Noob")
        menu.update(display, font)
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
    font = pygame.font.Font("assets/VT323-Regular.ttf", 28)
    fps = pygame.time.Clock()

    # Panggil dino game
    dino_game()
    pygame.quit()