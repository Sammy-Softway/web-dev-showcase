from turtle import Turtle

BASE_SIZE = 20
STRETCH_WID = 1
STRETCH_LEN = 3
X_SPACING = 65       #(60px brick + 5px gap)
Y_SPACING = 25       #(20px brick + 5px gap)
START_X = -325
START_Y = 220
ROW_NUMS = 5
COLUMN_NUMS = 11
ROW_COLORS = ["red", "orange", "yellow", "green", "blue"]
BRICK_HEIGHT = BASE_SIZE * STRETCH_WID
BRICK_WIDTH = BASE_SIZE * STRETCH_LEN

class Brick(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)
        self.color(color)
        self.goto(position)

class BrickManager:
    def __init__(self):
        self.all_bricks = []
        self.create_wall()

    def create_wall(self):
        for row in range(ROW_NUMS):
            color = ROW_COLORS[row]
            y = START_Y - (row * Y_SPACING)
            for col in range(COLUMN_NUMS):
                x = START_X + (col * X_SPACING)

                new_brick = Brick(color, (x,y))
                self.all_bricks.append(new_brick)
