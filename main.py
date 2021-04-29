import pygame
from dino import Dino

def dino_game():
    # Frame mula-mula
    frame = 0

    # Inisialisasi objek
    dino = Dino(50)

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

        dino.show(display, frame)
        pygame.display.update()

        # Atur framerate
        fps.tick(max_fps)
        frame = (frame + 1) % max_fps

if __name__ == "__main__":
    # Inisialisasi modul pygame
    pygame.init()
    pygame.mixer.init()

    # Inisialisasi dino game
    pygame.display.set_caption("Bellatrix's Dino Game")
    background = pygame.image.load("assets/background_01.png")
    display = pygame.display.set_mode((800, 600))
    fps = pygame.time.Clock()
    max_fps = 30

    # Panggil dino game
    dino_game()
    pygame.quit()