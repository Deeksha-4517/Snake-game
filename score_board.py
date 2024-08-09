from turtle import Turtle
hs = open("highscore.txt", mode="r+")

class ScoreBoard(Turtle):

# Initialise
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.high_score = int(hs.read())
        self.write(arg= f'Score = {self.score}, HighScore = {self.high_score}', move=False, align='center', font=("arial", 24, 'normal'))


    def refresh_score(self):
        self.clear()
        self.write(arg=f'Score = {self.score}, HighScore = {self.high_score}', move=False, align='center', font=("arial", 24, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            hs.write(str(self.high_score))
        self.score = 0
        self.refresh_score()

    def inc_score(self):
        self.score += 1
        self.refresh_score()

