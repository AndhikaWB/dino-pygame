import pygame
import random

from menu import Menu
from dino import Dino
from enemy import Enemy, Snail, Spike, Fly

min_fps = 30
max_fps = 60
road_height = 50
enemy_gap = (450, 650)
display_size = (800, 600)

def dino_game():
    # Inisiasi frame
    cur_fps = min_fps
    cur_frame = 0

    # Instansiasi objek
    menu = Menu()
    dino = Dino(road_height)
    enemies = [ Snail(road_height, display_size[0]) ]

    while True:
        # Tampilkan background game
        display.blit(background, (0, 0))

        # Dapatkan informasi event saat ini
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
                        menu.game_pause()
                elif event.type == pygame.KEYUP:
                    dino.walk()
            elif menu.state != "RUN":
                if event.type == pygame.KEYDOWN:
                    if menu.state == "PAUSE":
                        if event.key == pygame.K_r:
                            cur_fps = menu.reset(min_fps)
                            enemies = enemies[0].reset(display)
                            dino.reset()
                        elif event.key == pygame.K_ESCAPE:
                            menu.game_run()
                    elif menu.state == "DIED":
                        cur_fps = menu.reset(min_fps)
                        enemies = enemies[0].reset(display)
                        dino.reset()

        # Jika baru ada satu musuh
        if len(enemies) == 1:
            # Acak tipe dan jarak musuh kedua
            enemy_type = random.randint(0,2)
            enemy_range = random.randrange(enemies[0].pos_x + enemy_gap[0], enemies[0].pos_x + enemy_gap[1], 25)
            # Tambahkan musuh kedua
            if enemy_type == 0:
                enemies.append(Snail(road_height, enemy_range))
            elif enemy_type == 1:
                enemies.append(Spike(road_height, enemy_range))
            elif enemy_type == 2:
                enemies.append(Fly(road_height, enemy_range))

        dino.update(display, cur_frame, menu.state)
        [ enemy.update(display, cur_frame, menu.state) for enemy in enemies ]

        # Jika game sedang kondisi main
        if menu.state == "RUN":
            # Cek pergerakan musuh
            for enemy in enemies:
                if dino.rect.colliderect(enemy.rect):
                    menu.game_end()
                    dino.hurt()
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
    display = pygame.display.set_mode((display_size[0], display_size[1]))
    font = pygame.font.Font("assets/VT323-Regular.ttf", 28)
    fps = pygame.time.Clock()
    # Panggil game
    dino_game()
    pygame.quit()