import time
from ball import Ball
from board import Board
from line import Line
from paddle import Paddle
from turtle import Screen

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

ball = Ball()
board = Board()
line = Line()
p1 = Paddle((-350, 0))
p2 = Paddle((350, 0))

screen.onkeypress(fun=p1.move_up, key="w")
screen.onkeypress(fun=p1.move_down, key="s")
screen.onkeypress(fun=p2.move_up, key="Up")
screen.onkeypress(fun=p2.move_down, key="Down")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() in range(320, 341) and ball.distance(p2) < 50:
        ball.bounce_x()
    elif ball.xcor() in range(-341, -320) and ball.distance(p1) < 50:
        ball.bounce_x()

    if ball.xcor() in range(-100, 100):
        ball.reset_just_hit()

    if ball.xcor() > 380:
        board.increase_score("p1")
        ball.reset_position()
        ball.move_speed = 0.1
    elif ball.xcor() < -380:
        board.increase_score("p2")
        ball.reset_position()
        ball.move_speed = 0.1

screen.exitonclick()
