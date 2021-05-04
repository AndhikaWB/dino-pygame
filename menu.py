class Menu:
    def __init__(self):
        self.score = 0
        self.state = "DIED"

    def add_score(self, cur_fps):
        self.score += 1
        # Bonus skor tiap 5 rintangan
        if self.score % 5 == 0:
            print("Game score +10")
            self.score += 10
        # Tambah kecepatan tiap 10 rintangan
        if self.score % 30 == 0:
            print("Game speed +3")
            return cur_fps + 3
        return cur_fps

    def change_state(self, state):
        self.state = state

    def reset(self, min_fps):
        # Reset menu
        self.score = 0
        self.state = "RUN"
        # Reset frame
        return min_fps

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