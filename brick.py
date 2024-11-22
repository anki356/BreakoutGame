from turtle import Turtle


class Brick(Turtle):
    def __init__(self,color,position):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=3)
        self.goto(position)

