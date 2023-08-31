from turtle import Turtle, Screen
from ball import ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

#screen setup
Screen = Screen()
Screen.setup(800, 600)
Screen.bgcolor("black")
Screen.title("PONG")
Screen.tracer(0)

#Initialize paddles and ball
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = ball((0,0))
scoreboard = Scoreboard()


#key binding
Screen.listen()
Screen.onkey(r_paddle.goUp, "Up")
Screen.onkey(r_paddle.goDown, "Down")
Screen.onkey(l_paddle.goUp, "w")
Screen.onkey(l_paddle.goDown, "s")


game_on = True

while game_on:
    time.sleep(ball.move_speed)
    Screen.update()
    ball.move()
#check for collision with top and bottom wall then reverse direction
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
       


 #check for collision with right paddle   
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()
        
        
# check to see if ball misses paddles
    if ball.xcor() > 390 :
        scoreboard.l_point()
        ball.reset()


    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset()


Screen.exitonclick()