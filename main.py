from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# configuration of game rules
WALL_COLLISION = True

# configuration of screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# create snake, food and scoreboard instances
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# snake directioning with arrows
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

# starts the game
game_on = True

# snake movement
while game_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  # detect when snake eats food
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.grow()
    scoreboard.increase()

  # detect collision with wall
  if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
    if WALL_COLLISION:
      game_on = False
      scoreboard.gameover()
    else:
      snake.transport()

  # detect collision with tail
  for seg in snake.segments[1:]:
    if snake.head.distance(seg) < 10:
      game_on = False
      scoreboard.gameover()

# for keeping screen on
screen.exitonclick()
