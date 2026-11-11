from turtle import Screen
from paddle import Paddle, PADDLE_HEIGHT, PADDLE_WIDTH, START_Y
from ball import Ball
from time import sleep
from brick_manager import BrickManager

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 10
RIGHT_WALL = (SCREEN_WIDTH // 2) - BALL_RADIUS
LEFT_WALL = -RIGHT_WALL
TOP_WALL = (SCREEN_HEIGHT // 2) - BALL_RADIUS
PADDLE_WALL = START_Y + BALL_RADIUS + (PADDLE_HEIGHT // 2)


class GameManager:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Breakout Game")
        self.screen.tracer(0)
        self.is_game_on = True

        self.paddle = Paddle()
        self.screen.listen()
        self.screen.onkeypress(self.paddle.move_left, "Left")
        self.screen.onkeypress(self.paddle.move_right, "Right")
        self.screen.getcanvas().bind("<Motion>", self.on_mouse_move)

        self.ball = Ball()

        self.bricks = BrickManager()

    def on_mouse_move(self, event):
        turtle_x = event.x - (SCREEN_WIDTH // 2)
        self.paddle.move_to_x(turtle_x)


    def collision_check(self):
        if self.ball.xcor() >= RIGHT_WALL or self.ball.xcor() <= LEFT_WALL:
            self.ball.bounce_x()

        if self.ball.ycor() >= TOP_WALL:
            self.ball.bounce_y()

        if (START_Y <= self.ball.ycor() <= PADDLE_WALL
                and abs(self.ball.xcor() - self.paddle.xcor()) <= (PADDLE_WIDTH // 2) + BALL_RADIUS
                and self.ball.y_move < 0):
            self.ball.bounce_y()

    def run(self):
        while self.is_game_on:
            self.ball.move()

            self.collision_check()

            self.screen.update()
            sleep(0.05)

        self.screen.exitonclick()