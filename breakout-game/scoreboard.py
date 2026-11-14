from turtle import Turtle
import json


SCORE_START_X = 0
SCORE_START_Y = 260
NORMAL_FONT = ("Courier", 20, "bold")
LARGE_FONT = ("Courier", 30, "bold")
ALIGNMENT = "center"
STARTING_LIVES = 3
STARTING_LEVEL = 1
MAX_LEVEL = 3
DATA_FILE = "scores.json"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.top_scores = self.load_scores()
        self.high_score = self.top_scores[0]["score"] if self.top_scores else 0
        self.lives = STARTING_LIVES
        self.level = STARTING_LEVEL
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(SCORE_START_X, SCORE_START_Y)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score} | Lives: {self.lives} | Level: {self.level}",
                   align=ALIGNMENT, font=NORMAL_FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            # self.save_high_score()
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self, message):
        self.goto(0, 80)
        self.write(message, align=ALIGNMENT, font=LARGE_FONT)
        self.goto(0, 35)
        self.write("TOP 5 SCORES", align=ALIGNMENT, font=NORMAL_FONT)
        for index, entry in enumerate(self.top_scores, start=1):
            self.goto(0, 35 - (index * 30))
            self.write(f"{index}. {entry['name']} - {entry['score']}", align=ALIGNMENT, font=NORMAL_FONT)

    # @staticmethod
    # def load_high_score():
    #     try:
    #         with open(DATA_FILE, "r") as file:
    #             data = json.load(file)
    #             return data.get("high_score", 0)
    #     except (FileNotFoundError, json.JSONDecodeError):
    #         return 0
    #
    # def save_high_score(self):
    #     with open(DATA_FILE, "w") as file:
    #         data = {"high_score": self.high_score}
    #         json.dump(data, file, indent=4)

    @staticmethod
    def load_scores():
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                scores = data.get("top_scores", [])
                return scores if isinstance(scores, list) else []
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_scores(self):
        with open(DATA_FILE, "w") as file:
            data = {"top_scores": self.top_scores}
            json.dump(data, file, indent=4)

    def is_top_score(self):
        if self.score <= 0:
            return False
        return len(self.top_scores) < 5 or self.score > self.top_scores[-1]["score"]

    def add_top_score(self, name):
        clean_name = (name or "AAA").strip()[:3].upper() or "AAA"
        self.top_scores.append({"name": clean_name, "score": self.score})
        self.top_scores.sort(key=lambda item: item["score"], reverse=True)
        self.top_scores = self.top_scores[:5]
        self.high_score = self.top_scores[0]["score"]
        self.save_scores()
