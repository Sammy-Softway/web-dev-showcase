from turtle import Turtle


BALL_START_X = 0
BALL_START_Y = -220
X_MOVE = 10
Y_MOVE = 10
INITIAL_SPEED = 0.05
MIN_SPEED = 0.015


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.goto(BALL_START_X, BALL_START_Y)
        self.x_move = X_MOVE
        self.y_move = Y_MOVE
        self.base_speed = INITIAL_SPEED
        self.move_speed = self.base_speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x,new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(BALL_START_X, BALL_START_Y)
        self.x_move *= -1
        self.y_move = abs(self.y_move)
        self.move_speed = self.base_speed

    def speed_up(self):
        self.move_speed = max(MIN_SPEED, self.move_speed * 0.95)
