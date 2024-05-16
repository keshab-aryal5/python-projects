from turtle import Turtle,Screen
from setup import Screen_height,Screen_width,Sleep_time
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor("black")
# screen.bgpic("me.jpg")
screen.setup(width=Screen_width,height=Screen_height)
screen.title("Snake Game")
screen.tracer(0)

# creating a snake body
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkeypress(fun=snake.move_up, key="Up")
screen.onkeypress(fun=snake.move_down, key="Down")
screen.onkeypress(fun=snake.move_left, key="Left")
screen.onkeypress(fun=snake.move_right, key="Right")                                                                    
is_game_on = True
food.new_food()
scoreboard.update_score()
while is_game_on:
    screen.update()
    snake.move()
    if snake.collides():
        is_game_on = False
        scoreboard.game_over()
    if snake.head.distance(food.get_position()) < 15:
        scoreboard.update_score()
        food.new_food()
        snake.add_segment()
        if Sleep_time > 0.0625:
            Sleep_time *= 0.5
    time.sleep(Sleep_time)


screen.exitonclick()

# There may be many bugs in this program, but the main bug is: 
# suppose the snake is moving one one direction towards right
# now if we want to change the direction to left, first we press
# up key(down also works) and then left key. But is you press these
# two key quickly. The sanke head directly move backward without moving
# upward (or downward) and the game ends. 