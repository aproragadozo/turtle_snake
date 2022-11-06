from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

    def generate(self):
        self.color(random.choice(["blue", "red"]))
        if str(self.color() [0])== "red":
            self.shape("arrow")
        else:
            self.shape("circle")
        print(str(self.color()))
        random_x = random.randrange(-280, 280, 20)
        random_y = random.randrange(-280, 280, 20)
        self.goto(random_x, random_y)

    def drop(self):
        self.reset()
