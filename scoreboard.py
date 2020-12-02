from turtle import Turtle

FONT = ("Arial", 14, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.score = 0
        self.hit()
        self.color("white")
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT)

    def hit(self):
        self.clear()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score : {self.score} ", align=ALIGNMENT, font=FONT)
        self.score += 1

