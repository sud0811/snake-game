from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")

game_is_on = True
screen.update()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
   
   #detech collision w food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()


    #detech collision w wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset ()
        snake.reset()

    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()
        


screen.exitonclick() 