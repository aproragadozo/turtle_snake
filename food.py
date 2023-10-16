from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")

    def generate(self):
        switch = {
            1: {"color": "red", "shape": "arrow"},
            2: {"color": "blue", "shape": "circle"},
            3: {"color": "green", "shape": "square"}
        }
        new_choice = random.choice([1, 2, 3])
        self.color(switch.get(new_choice)["color"])
        self.shape(switch.get(new_choice)["shape"])
        random_x = random.randrange(-280, 280, 20)
        random_y = random.randrange(-280, 280, 20)
        self.goto(random_x, random_y)

    def drop(self):
        self.reset()
