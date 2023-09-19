import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 25, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.color("white")
        self.penup()
        self.goto(0, 265)
        file=open("data.txt",mode="r")
        contents=file.read()
        print(contents)
        content=int(contents)
        self.highscore=content
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            file = open("data.txt", mode="w")
            new_h_score=str(self.score)
            contents = file.write(new_h_score)

        self.score=0
        self.update_scoreboard()
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
