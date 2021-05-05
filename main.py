import pygame
import random

from menu import Menu
from dino import Dino
from enemy import Enemy

display_width = 800
display_height = 600
font_size = 28
road_height = 50

def dino_game():
    # Instansiasi objek
    menu = Menu()
    dino = Dino(road_height)
    enemy = Enemy(road_height)

    # Inisiasi frame
    frame = 0

    while True:
        # Tampilkan background game
        display.blit(background, (0, 0))

        # Dapatkan informasi event saat ini
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif menu.state == "RUN":
                if event.type == pygame.KEYDOWN:
                    # Tekan UP untuk melompat
                    if event.key == pygame.K_UP:
                        dino.jump()
                    # Tekan DOWN untuk menunduk
                    elif event.key == pygame.K_DOWN:
                        dino.duck()
                    # Tekan ESC untuk berhenti sejenak
                    elif event.key == pygame.K_ESCAPE:
                        menu.game_pause()
                # Kembali berjalan sesudah menekan tombol
                elif event.type == pygame.KEYUP:
                    dino.walk()
            elif menu.state != "RUN":
                if event.type == pygame.KEYDOWN:
                    if menu.state == "PAUSE":
                        # Tekan R untuk memulai kembali
                        if event.key == pygame.K_r:
                            menu.reset(display, dino, enemy)
                        # Tekan ESC untuk melanjutkan
                        elif event.key == pygame.K_ESCAPE:
                            menu.game_run()
                    elif menu.state == "DIED":
                        # Tekan APA SAJA untuk memulai kembali
                        menu.reset(display, dino, enemy)

        # Update pergerakan dino dan musuh
        dino.update(display, frame, menu)
        enemy.update(display, frame, menu, dino)

        # Update status menu dan display
        menu.update(display, font)
        pygame.display.update()

        # Atur frame untuk loop selanjutnya
        frame = (frame + 1) % menu.speed
        fps.tick(menu.speed)

if __name__ == "__main__":
    # Inisialisasi modul
    pygame.init()
    # Inisialisasi game
    pygame.display.set_caption("Bellatrix's Dino Game")
    background = pygame.image.load("assets/background_01.png")
    display = pygame.display.set_mode((display_width, display_height))
    font = pygame.font.Font("assets/VT323-Regular.ttf", font_size)
    fps = pygame.time.Clock()
    # Panggil game
    dino_game()
    pygame.quit()