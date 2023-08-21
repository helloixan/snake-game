from turtle import Turtle
FONT = ("courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data :
            self.high_score= int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write_score()

    def update_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align="center", font=FONT)


    def reset(self):
        if self.score > self.high_score :
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.write_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER.", align="center", font=FONT)