class Menu:
    def __init__(self):
        self.score = 0
        self.state = "PAUSE"

    def pause(self, font, state = "PAUSE"):
        self.state = state

    def unpause(self):
        self.state = "NOT_PAUSE"

    def update(self, display, font):
        self.score += 1
        # Bonus skor tiap melewati 5 rintangan
        if self.score % 5 == 0:
            self.score += 9

        score_text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        display.blit(score_text, (10, 10))