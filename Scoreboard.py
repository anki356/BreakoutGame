from turtle import Turtle


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.score=0
        self.writeScore()
    def writeScore(self):
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Courier",24,"normal"))
    def increaseScore(self):
        self.score+=1
        self.writeScore()
    def printGameOver(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Courier", 40, "normal"))
