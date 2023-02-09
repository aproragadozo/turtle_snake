from turtle import Turtle
import inspect

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10


class Snake:
    def __init__(self):
        self.segments = []
        self.head = None
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        new = Turtle(shape="square")
        new.penup()
        new.color("white")
        new.setx(position[0])
        new.sety(position[1])
        # trying to define speed here already, perhaps that helps
        new.speed("slowest")
        self.segments.append(new)
        self.head = self.segments[0]

    def restart(self):
        # trim snake to first three segments
        for bit in self.segments:
            bit.reset()
        self.__init__()

    def grow(self):
        self.add_segment(self.segments[-1].position())

# different kinds of food shouldn't just look different, but also trigger events
    def handle_fud(self, fud):
        # I think manipulating MOVE_DISTANCE might be the way forward
        global MOVE_DISTANCE
        if fud.shape() == "arrow":
            # if this is higher than 20, the snake develops gaps
            MOVE_DISTANCE = 20


    def report(self):
        return self.segments[0].position()

    def move(self):
        for idx in range(len(self.segments) - 1, 0, -1):
            self.segments[idx].goto(self.segments[idx - 1].xcor(), self.segments[idx - 1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if int(self.segments[0].heading()) == 0:
            self.segments[0].left(90)
        elif int(self.segments[0].heading()) == 180:
            self.segments[0].right(90)
        elif int(self.segments[0].heading()) == 90:
            pass

    def left(self):
        if self.head.heading() != 0:
            if int(self.segments[0].heading()) == 270:
                self.segments[0].right(90)
            elif int(self.segments[0].heading()) != 180:
                self.segments[0].left(90)

    def right(self):
        if self.head.heading() != 180:
            if int(self.segments[0].heading()) == 270:
                self.segments[0].left(90)
            elif int(self.segments[0].heading()) != 0:
                self.segments[0].right(90)

    def down(self):
        if int(self.segments[0].heading()) == 0:
            self.segments[0].right(90)
        elif int(self.segments[0].heading()) == 180:
            self.segments[0].left(90)
