import pygame

class Menu:
    def __init__(self):
        self.score = 0
        self.state = "DIED"

    def add_score(self, cur_fps):
        self.score += 1
        # Bonus skor tiap 5 rintangan
        if self.score % 5 == 0:
            print(f"Game score +10 ({self.score})")
            self.score += 10
        # Tambah kecepatan tiap 10 rintangan
        if self.score % 30 == 0:
            print(f"Game speed +3 ({cur_fps + 3})")
            return cur_fps + 3
        return cur_fps

    def game_run(self):
        self.state = "RUN"

    def game_pause(self):
        self.state = "PAUSE"

    def game_end(self):
        print(f"Game over ({self.score})")
        self.state = "DIED"

    def reset(self, min_fps):
        self.score = 0
        self.state = "RUN"
        return min_fps

    """
    def check(self, event, min_fps):
        if event.type == pygame.KEYDOWN:
            if self.state == "RUN":
                if event.key == pygame.K_p:
                    self.game_pause()
            elif self.state == "PAUSE":
                if event.key == pygame.K_p:
                    self.game_run()
                elif event.key == pygame.k_r:
                    self.reset(min_fps)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
            elif self.state == "DIED":
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                else: self.reset(min_fps)
    """

    def update(self, display, font):
        score_text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        display.blit(score_text, (10, 10))

        if self.state == "PAUSE":
            help_text = font.render("Press R to reset or ESC to continue", True, (255, 255, 255))
            help_text_rect = help_text.get_rect()
            help_text_rect.center = (display.get_width() // 2, 70)
            display.blit(help_text, help_text_rect)
        elif self.state == "DIED":
            help_text = font.render("Press ANY KEY to (re)start", True, (255, 255, 255))
            help_text_rect = help_text.get_rect()
            help_text_rect.center = (display.get_width() // 2, 70)
            display.blit(help_text, help_text_rect)