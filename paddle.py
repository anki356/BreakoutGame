from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=15)
        self.goto(0,-275)
    def move_right(self):
        self.penup()
        if self.xcor()<477:
           self.goto(self.xcor()+20,self.ycor())

    def move_left(self):
        self.penup()
        if self.xcor()>-477:
           self.goto(self.xcor() - 20, self.ycor())