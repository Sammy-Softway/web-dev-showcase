from turtle import Turtle


SCORE_START_X = 0
SCORE_START_Y = 260
NORMAL_FONT = ("Courier", 20, "bold")
LARGE_FONT = ("Courier", 30, "bold")
ALIGNMENT = "center"
STARTING_LIVES = 3
STARTING_LEVEL = 1
MAX_LEVEL = 3


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = STARTING_LIVES
        self.level = STARTING_LEVEL
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(SCORE_START_X, SCORE_START_Y)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | Lives: {self.lives} | Level: {self.level}",
                   align=ALIGNMENT, font=NORMAL_FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self, message):
        self.goto(0, 0)
        self.write(message, align=ALIGNMENT, font=LARGE_FONT)