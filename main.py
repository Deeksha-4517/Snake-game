from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard

# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Nokia snake game')

# Setup game objects
snake = Snake()
screen.tracer(0)
screen.listen()
food = Food()
scoreboard = ScoreBoard()

game_on = True
while game_on:
    screen.update()
    snake.move()

# Move snake
    screen.onkey(fun=snake.up, key='w')
    screen.onkey(fun=snake.down, key='s')
    screen.onkey(fun=snake.left, key='a')
    screen.onkey(fun=snake.right, key='d')

# Extend Snake
    if snake.head.distance(food) < 15:
        food.generate()
        scoreboard.inc_score()
        snake.extend()

# Conditions for game over
    if snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()


    for segment in snake.SegList:
        if segment != snake.head:
            if snake.head.distance(segment) < 5:
                scoreboard.reset()
                snake.reset()


screen.exitonclick()
