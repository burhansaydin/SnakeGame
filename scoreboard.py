from turtle import Turtle

FONT = ("Arial", 14, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as f:
            current_score = int(f.read())
        self.high_score = current_score
        self.pu()
        self.score = 0
        self.update_score()
        self.color("white")
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def hit(self):
        self.clear()
        self.score += 1
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align=ALIGNMENT, font=FONT)


