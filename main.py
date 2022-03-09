import turtle
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-390, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # detect collision with paddle
    if (ball.distance(r_paddle) < 55 and ball.xcor() >= 360) or (ball.distance(l_paddle) < 55 and ball.xcor() <= -370):
        ball.bounce_x()

    # detect when R paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.new_round()

    # detect when L paddle misses
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.new_round()

    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_is_on = False

screen.exitonclick()
