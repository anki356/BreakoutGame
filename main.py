import time
import turtle
import random
from turtle import Turtle,Screen

from Scoreboard import scoreboard
from ball import Ball
from brick import Brick
from paddle import Paddle

screen=Screen()
screen.title("Breakout Game")
screen.setup(width=1314,height=600)
screen.bgcolor("black")
screen.tracer(0)
colors=["yellow","red","orange","green"]
bricks=[]
ball=Ball()
pd=Paddle()
sc=scoreboard()
for index in range(4):
    b = 0
    for num in range(0,20):
        brick=Brick(colors[index],(-627+num*60+b,150+20*index))
        bricks.append(brick)
        b+=6
game_is_on=True
screen.listen()
screen.onkeypress(pd.move_right,"Up")
screen.onkeypress(pd.move_left,"Down")

while game_is_on:
    time.sleep(0.1)


#detect collision
    for brick in bricks:
        if ball.distance(brick)<40:
            brick.hideturtle()
            bricks.remove(brick)
            ball.bounce_y_back()
#detect boundary
    if ball.xcor()>637 or ball.xcor()<-637:
       ball.bounce_x_back()
#detect collision with paddle
    if ball.distance(pd)<150 and ball.ycor()<-255:
       sc.increaseScore()
       ball.bounce_y_back()
#detect with floor
    if ball.ycor()<-280:
       game_is_on=False
       sc.printGameOver()
    ball.move()
    screen.update()
screen.exitonclick()




