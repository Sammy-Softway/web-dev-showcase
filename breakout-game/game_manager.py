from turtle import Screen
from paddle import Paddle, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_START_Y
from ball import Ball
from time import sleep
from brick_manager import BrickManager, BRICK_HEIGHT, BRICK_WIDTH
from scoreboard import Scoreboard, MAX_LEVEL


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 10
RIGHT_WALL = (SCREEN_WIDTH // 2) - BALL_RADIUS
LEFT_WALL = -RIGHT_WALL
TOP_WALL = (SCREEN_HEIGHT // 2) - BALL_RADIUS
PADDLE_Y_WALL = PADDLE_START_Y + BALL_RADIUS + (PADDLE_HEIGHT // 2)
PADDLE_X_WALL = (PADDLE_WIDTH // 2) + BALL_RADIUS
BRICK_X_WALL = (BRICK_WIDTH // 2) + BALL_RADIUS
BRICK_Y_WALL = (BRICK_HEIGHT // 2) + BALL_RADIUS
BOTTOM_WALL = -(SCREEN_HEIGHT // 2) + BALL_RADIUS
LEVEL_SPEEDS = {1: 0.05, 2: 0.038, 3: 0.028}
RESET_DELAY = 0.5


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

        self.scoreboard = Scoreboard()

    def on_mouse_move(self, event):
        turtle_x = event.x - (SCREEN_WIDTH // 2)
        self.paddle.move_to_x(turtle_x)

    def collision_check(self):
        if self.ball.xcor() >= RIGHT_WALL or self.ball.xcor() <= LEFT_WALL:
            self.ball.bounce_x()

        if self.ball.ycor() >= TOP_WALL:
            self.ball.bounce_y()

        if (PADDLE_START_Y <= self.ball.ycor() <= PADDLE_Y_WALL
                and abs(self.ball.xcor() - self.paddle.xcor()) <= PADDLE_X_WALL
                and self.ball.y_move < 0):
            self.ball.bounce_y()

        if self.ball.ycor() <= BOTTOM_WALL:
            self.scoreboard.lose_life()
            self.ball.reset_position()
            sleep(0.5)

            if self.scoreboard.lives <= 0:
                self.is_game_on = False
                self.scoreboard.game_over("GAME OVER")

        self.check_brick_collisions()

    def check_brick_collisions(self):
        all_bricks = self.bricks.all_bricks[:]
        for brick in all_bricks:
            if (abs(self.ball.xcor() - brick.xcor()) <= BRICK_X_WALL
                    and abs(self.ball.ycor() - brick.ycor()) <= BRICK_Y_WALL):

                overlap_x = BRICK_X_WALL - abs(self.ball.xcor() - brick.xcor())
                overlap_y = BRICK_Y_WALL - abs(self.ball.ycor() - brick.ycor())

                if overlap_x < overlap_y:
                    self.ball.bounce_x()
                else:
                    self.ball.bounce_y()

                self.bricks.remove_brick(brick)
                self.scoreboard.increase_score()

                if self.scoreboard.score % 5 == 0:
                    self.ball.speed_up()

                if len(self.bricks.all_bricks) == 0:
                    if self.scoreboard.level < MAX_LEVEL:
                        self.scoreboard.increase_level()
                        self.ball.base_speed = LEVEL_SPEEDS[self.scoreboard.level]
                        self.ball.reset_position()
                        self.bricks.create_wall(rows=5 + self.scoreboard.level - 1)
                        self.screen.update()
                        sleep(RESET_DELAY)
                    else:
                        self.is_game_on = False
                        self.scoreboard.game_over("YOU WIN!")

                break

    def run(self):
        while self.is_game_on:
            self.ball.move()

            self.collision_check()

            self.screen.update()
            sleep(self.ball.move_speed)

        self.screen.exitonclick()