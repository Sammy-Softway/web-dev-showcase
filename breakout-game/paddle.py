from turtle import Turtle

START_X = 0
START_Y = -250
X_LIMIT = 350
MOVE_DISTANCE = 20
BASE_SIZE = 20
STRETCH_WID = 1
STRETCH_LEN = 5
PADDLE_HEIGHT = BASE_SIZE * STRETCH_WID
PADDLE_WIDTH = BASE_SIZE * STRETCH_LEN

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)
        self.penup()
        self.goto(START_X, START_Y)

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        if new_x >= -X_LIMIT:
            self.goto(new_x,self.ycor())

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        if new_x <= X_LIMIT:
            self.goto(new_x,self.ycor())

    def move_to_x(self, target_x):
        clamped_x = max(-X_LIMIT, min(X_LIMIT, target_x))
        self.goto(clamped_x, self.ycor())
