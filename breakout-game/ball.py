from turtle import Turtle

START_X = 0
START_Y = -220
X_MOVE = 10
Y_MOVE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.goto(START_X, START_Y)
        self.x_move = X_MOVE
        self.y_move = Y_MOVE

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x,new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1