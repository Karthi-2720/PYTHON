import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard

NUM_R = 0
NUM_L = 0
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("green")
screen.title("Pong")
screen.tracer(0)


# # --- NEW BORDER CODE ---
# border_pen = Turtle()
# border_pen.hideturtle()
# border_pen.color("white")
# border_pen.pensize(3)
# border_pen.penup()

# # Move to top-left corner
# border_pen.goto(-400, 300)
# border_pen.pendown()
#
# # Draw the rectangle
# for _ in range(2):
#     border_pen.forward(780)  # Width
#     border_pen.right(90)
#     border_pen.forward(580)  # Height
#     border_pen.right(90)
# # -----------------------

screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score_r = Scoreboard((100, 220))
score_l = Scoreboard((-100, 220))

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up_l, "w")
screen.onkey(l_paddle.down_l, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.02)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
            (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        NUM_L += 1
        score_l.l_score(num=NUM_L)

    if ball.xcor() < -380:
        ball.reset_ball()
        NUM_R += 1
        score_r.l_score(num=NUM_R)

    if NUM_R == 10:
        is_game_on = False
        print("Left player loose")

    elif NUM_L == 10:
        is_game_on = False
        print("Right player loose")


screen.exitonclick()