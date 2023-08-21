from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")


game_on = True
while game_on :
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15 :
        food.update()
        scoreboard.update_score()
        snake.add_segment()
    
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280 :
        scoreboard.reset()
        snake.reset()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15 :
            scoreboard.reset()
            snake.reset()

screen.exitonclick()