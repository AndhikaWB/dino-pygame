import pygame
import random

from menu import Menu
from dino import Dino
from enemy import Enemy, Snail, Spike, Fly

def dino_game():
    # Batasan frame
    min_fps = 30
    max_fps = 60
    # Frame mula-mula
    cur_fps = min_fps
    cur_frame = 0
    # Ketinggian jalan
    road_y = 50
    # Jarak antar musuh
    min_gap = 500
    max_gap = 600
    # Instansiasi objek
    menu = Menu()
    dino = Dino(road_y)
    enemy = Enemy(road_y)

    while True:
        # Tampilkan background game
        display.blit(background, (0, 0))

        # Dapatkan info event saat ini
        for event in pygame.event.get():
            # Jika pengguna menutup game
            if event.type == pygame.QUIT:
                return
            # Jika game sedang kondisi main
            elif menu.state == "RUN":
                if event.type == pygame.KEYDOWN:
                    # Tekan panah atas untuk melompat
                    if event.key == pygame.K_UP:
                        dino.jump()
                    # Tekan panah bawah untuk jongkok
                    elif event.key == pygame.K_DOWN:
                        dino.duck()
                    # Tekan ESC untuk pause game
                    elif event.key == pygame.K_ESCAPE:
                        menu.change_state("PAUSE")
                elif event.type == pygame.KEYUP:
                    dino.walk()
            # Jika game sedang kondisi diam/mati
            elif menu.state != "RUN":
                if event.type == pygame.KEYDOWN:
                    if menu.state == "PAUSE":
                        # Tekan R untuk mengulang game
                        if event.key == pygame.K_r:
                            cur_fps = menu.reset(dino, enemy, min_fps)
                        # Tekan ESC untuk melanjutkan game
                        elif event.key == pygame.K_ESCAPE:
                            menu.change_state("RUN")
                    elif menu.state == "DIED":
                        # Tekan APA SAJA untuk mengulang game
                        cur_fps = menu.reset(dino, enemy, min_fps)

        # Jika sedang tidak ada musuh
        if enemy.state == "NOT_EXIST":
            # Tambahkan skor saat ini
            cur_fps = menu.add_score(cur_fps)
            # Tambahkan musuh secara acak
            enemy_type = random.randint(0, 2)
            if enemy_type == 0:
                enemy = Snail(road_y)
            elif enemy_type == 1:
                enemy = Spike(road_y)
            elif enemy_type == 2:
                enemy = Fly(road_y)

        # Jika game sedang kondisi main
        if menu.state == "RUN":
            # Update gerakan dino dan musuh
            dino.update(display, cur_frame)
            enemy.update(display, cur_frame)
            # Cek apakah dino menabrak musuh
            if dino.rect.colliderect(enemy.rect):
                menu.change_state("DIED")

        # Update menu dan display
        menu.update(display, font)
        pygame.display.update()

        # Cegah game berjalan terlalu cepat
        if cur_fps > max_fps: cur_fps = max_fps
        # Atur frame untuk loop selanjutnya
        cur_frame = (cur_frame + 1) % cur_fps
        fps.tick(cur_fps)

if __name__ == "__main__":
    # Inisialisasi display
    pygame.init()
    # Inisialisasi game
    pygame.display.set_caption("Bellatrix's Dino Game")
    background = pygame.image.load("assets/background_01.png")
    display = pygame.display.set_mode((800, 600))
    font = pygame.font.Font("assets/VT323-Regular.ttf", 28)
    fps = pygame.time.Clock()
    # Panggil game
    dino_game()
    pygame.quit()