# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import turtle
import math
import time
from random import randint
# game_screen_setup
game_screen=turtle.Screen()
game_screen.setup(width=800,height=500)
game_screen.title("Snake Game")
game_screen.bgcolor("black")
game_screen.tracer(0)
# snake_setup
snake=turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("orange")
snake.goto(0,0)
snake.penup()
snake.direction=""
snake.pensize(50)

# keyfunction

def move_up():
    if snake.direction!="down":
        snake.direction="up"
def move_down():
    if snake.direction!="up":
        snake.direction="down"
def move_right():
    if snake.direction!="left":
        snake.direction="right"
def move_left():
    if snake.direction != "right":
        snake.direction="left"
# key assign
game_screen.listen()
game_screen.onkeypress(move_up,"")
game_screen.onkeypress(move_down,"s")
game_screen.onkeypress(move_right,"d")
game_screen.onkeypress(move_left,"a")

# direction_setup
def move():
    if snake.direction=="right":
        x=snake.xcor()
        snake.setx(x+10)
    if snake.direction=="left":
        x = snake.xcor()
        snake.setx(x-10)
    if snake.direction=="up":
        y = snake.ycor()
        snake.sety(y+10)
    if snake.direction=="down":
        y = snake.ycor()
        snake.sety(y-10)
# food
food=turtle.Turtle()
food.penup()
food.shape("circle")
food.color("blue")
food.goto(randint(-400,400),randint(-230,230))

# stop game
def stop_game():
    time.sleep(1)
    snake.goto(0, 0)
    for index in range(0, len(segments)):
        segments[index].goto(1000, 1000)
    segments.clear()
    snake.direction = "stop"

# food position
def food_position():
    food_x = randint(-80, 80)
    food_y = randint(-80, 80)
    food.goto(food_x,food_y)

segments=[]

score=0

# game loop

while True:

     game_screen.update()

     if snake.distance(food)<20:
         food_position()
         body=turtle.Turtle()
         body.shape("square")
         body.speed(0)
         body.penup()
         body.color("gray")
         segments.append(body)
         score=score+10
     for index in range(len(segments)-1,0,-1):
         x=segments[index-1].xcor()
         y=segments[index-1].ycor()
         segments[index].goto(x,y)
     if len(segments)>0:
         x=snake.xcor()
         y=snake.ycor()
         segments[0].goto(x,y)

     move()
     for segment in segments:
         if segment.distance(snake)<5:
             stop_game()
     if snake.xcor()>400 or snake.xcor()<-400 or snake.ycor()>250 or snake.ycor()<-250:
         stop_game()
     time.sleep(.03)



game_screen.mainloop()

