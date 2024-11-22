from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.goto(0,-250)
        self.x_move=10
        self.y_move=10
    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)
    def bounce_y_back(self):
        self.y_move*=-1

    def bounce_x_back(self):
            self.x_move *= -1
