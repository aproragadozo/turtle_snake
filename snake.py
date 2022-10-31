from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


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
        self.segments.append(new)
        self.head = self.segments[0]

    def restart(self):
        # trim snake to first three segments
        # this is supposed to hide the segments over 3
        # what it does is something else completely
        # for bit in self.segments[3:]:
        #     bit.hideturtle()
        # perhaps a completely new snake then?
        # resetting the screen, and re-drawing the whole thing?
        # self.reset()
        # ez azért nem jó, mert maga a snek nem turtle, csak az egyes darabjai
        # egyenként adarabjaira ha meghívjuk a resetet?
        for bit in self.segments:
            bit.reset()
        self.__init__()

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def report(self):
        return self.segments[0].position()

    def move(self):
        for idx in range(len(self.segments) - 1, 0, -1):
            # for idx, bit in enumerate(segments):
            # if idx == 0:
            # bit.left(90)
            # bit.forward(20)
            # else:
            # bit.goto(segments[idx-1].xcor(), segments[idx-1].ycor())
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

# def left():
#     screen.tracer(0)
#     for bit in segments:
#         bit.setx(bit.xcor() - 20)
#     screen.update()
#
#
# def right():
#     screen.tracer(0)
#     for bit in segments:
#         bit.setx(bit.xcor() + 20)
#     screen.update()
#
#
# def up():
#     screen.tracer(0)
#     for idx in range(len(segments)-1, 0, -1):
#     # for idx, bit in enumerate(segments):
#         #if idx == 0:
#             #bit.left(90)
#             #bit.forward(20)
#         #else:
#             #bit.goto(segments[idx-1].xcor(), segments[idx-1].ycor())
#         segments[idx].goto(segments[idx - 1].xcor(), segments[idx - 1].ycor())
#     segments[0].left(90)
#     segments[0].forward(20)
#     screen.update()
#
#
# def down():
#     screen.tracer(0)
#     for bit in segments:
#         bit.sety(bit.ycor() - 20)
#     screen.update()
#
#
# screen.onkeypress(key="Left", fun=left)
# screen.onkeypress(key="Right", fun=right)
# screen.onkeypress(key="Up", fun=up)
# screen.onkeypress(key="Down", fun=down)
# screen.exitonclick()