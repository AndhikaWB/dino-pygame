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
    min_gap = 450
    max_gap = 650
    # Instansiasi objek
    menu = Menu()
    dino = Dino(road_y)
    enemies = [ Snail(road_y, display.get_width()) ]

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
                            cur_fps = menu.reset(min_fps)
                            dino.reset()
                            enemies = [ Snail(road_y, display.get_width()) ]
                        # Tekan ESC untuk melanjutkan game
                        elif event.key == pygame.K_ESCAPE:
                            menu.change_state("RUN")
                    elif menu.state == "DIED":
                        # Tekan APA SAJA untuk mengulang game
                        cur_fps = menu.reset(min_fps)
                        dino.reset()
                        enemies = [ Snail(road_y, display.get_width()) ]

        # Jika baru ada satu musuh
        if len(enemies) == 1:
            # Acak tipe dan jarak musuh kedua
            enemy_type = random.randint(0,2)
            enemy_range = random.randrange(enemies[0].pos_x + min_gap, enemies[0].pos_x + max_gap, 25)
            # Tambahkan musuh kedua
            if enemy_type == 0:
                enemies.append(Snail(road_y, enemy_range))
            elif enemy_type == 1:
                enemies.append(Spike(road_y, enemy_range))
            elif enemy_type == 2:
                enemies.append(Fly(road_y, enemy_range))

        # Jika game sedang kondisi main
        if menu.state == "RUN":
            # Update pergerakan dino
            dino.update(display, cur_frame)
            # Cek pergerakan musuh
            for enemy in enemies:
                enemy.update(display, cur_frame)
                if dino.rect.colliderect(enemy.rect):
                    dino.hurt()
                    menu.change_state("DIED")
                elif enemy.state == "NOT_EXIST":
                    cur_fps = menu.add_score(cur_fps)
                    enemies.remove(enemy)

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