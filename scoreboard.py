from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x, y):
        self.title = "Score: "
        self.score = 0
        # itt kéne olvasni a filéből
        # self.high_score = 0
        with open('hi-score.txt') as file:
            self.high_score = int(file.read())
        super().__init__()
        self.penup()
        self.color("white")
        self.x = x
        self.y = y
        self.setpos(self.x, self.y)
        self.hideturtle()
        self.display()

    def display(self):
        self.clear()
        self.write(f"{self.title} {str(self.score)} High Score {self.high_score}",
                   move=False, align="left", font=("Courier New", 12, "normal"))

    def increment(self):
        self.score += 1
        self.display()

    def game_over(self):
        if self.score > self.high_score:
            # erre továbbra is szükség van, mert az új high score csak a reinitnél olvasódik majd ki
            self.high_score = self.score
            # itt kéne írni a filébe
            with open('hi-score.txt', mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.display()
        # self.goto(0, 0)
        # self.write("GAME OVER", move=False, align="left", font=("Courier New", 12, "normal"))
