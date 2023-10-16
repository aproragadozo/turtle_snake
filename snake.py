from turtle import Turtle, ontimer
import inspect


STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.head = None
        self.create_snake()
        # define the delay for the game loop here
        # since this is where it will be manipulated
        # to avoid circular import and undefined value errors
        self.delay = 0.1
        # the default is 1 food at a time
        self.multi = False

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
        for bit in self.segments:
            bit.reset()
        self.__init__()

    def grow(self):
        self.add_segment(self.segments[-1].position())
    

# different kinds of food shouldn't just look different, but also trigger events
    def handle_fud(self, fud):
        # from main import screen
        # the arrow food speeds up the game by reducing the delay
        if fud.shape() == "arrow":
            # reset the screen background
            # screen.bgcolor("black")
            # reset the food generation scheme
            self.multi = False
            if self.delay > 0.02:
                self.delay -= 0.02
        # the square food blinks the screen randomly
        if fud.shape() == "square":
            # reset the delay
            self.delay = 0.1
            # reset the food generation scheme
            self.multi = False
            """ def screen_to_white():
                screen.bgcolor("white")
            def screen_to_black():
                screen.bgcolor("black")
            for i in range(len(self.segments)):
                ontimer(screen_to_white, 10)
                ontimer(screen_to_black, 10) """
        # the circle food generates a lot of food
        if fud.shape() == "circle":
             # reset the delay
            self.delay = 0.1
            # reset the screen background
            # screen.bgcolor("black")
            self.multi = True


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
