from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("Black")
user_level = screen.textinput("Difficulty", "Choose a difficulty: 'easy', 'hard' or 'normal'").lower()

screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()
snake.create_snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

new_score = 0
game_is_on = True
if user_level:
    game_is_on = True
while game_is_on:
    screen.update()
    if user_level == "hard":
        time.sleep(0.08)
    elif user_level == "easy":
        time.sleep(0.13)
    else:
        time.sleep(0.1)

    snake.move()
    # Detect food collisions
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collisions with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collisions with tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
