from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNEK!")

screen.tracer(0)


game = True
snek = Snake()
# this starts out as regular food, and then should either change to fancy food or not
# every time a bit of food is eaten
fud = Food()
scoreboard = Scoreboard(-20, (screen.window_height()//2) - 20)
score = scoreboard.score
screen.listen()

screen.onkey(key="Up", fun=snek.up)
screen.onkey(key="Left", fun=snek.left)
screen.onkey(key="Right", fun=snek.right)
screen.onkey(key="Down", fun=snek.down)

while game:
    screen.update()
    time.sleep(snek.delay)
    snek.move()
    # this bit will need to be rewritten if the new default is that collision with the walls kill
    if abs(snek.report()[0]) >= screen.window_width()//2:
        if snek.report()[0] < -(screen.window_width()//2):
            snek.head.goto((screen.window_width()//2), snek.head.ycor())
        else:
            snek.head.goto(-(screen.window_width() // 2), snek.head.ycor())
    if abs(snek.report()[1]) >= screen.window_height()//2:
        if snek.report()[1] < -(screen.window_height()//2):
            snek.head.goto(snek.head.xcor(), (screen.window_height()//2))
        else:
            snek.head.goto(snek.head.xcor(), -(screen.window_height() // 2))

    # detect collision with food
    if snek.head.distance(fud) < 15:
        snek.handle_fud(fud)
        snek.grow()
        # if the last food type eaten was a circle
        # generate an additional food for each segment in the snake
        if snek.multi:
            for i in range(5):
                fud.generate()
        else:
            fud.generate()
        scoreboard.increment()
        print(snek.multi)

    # detect collision with tail
    for bit in snek.segments[1:]:
        if snek.head.distance(bit) < 10:
            #game = False
            scoreboard.game_over()
            snek.restart()
    
screen.mainloop()
# screen.exitonclick()