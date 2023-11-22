from turtle import Turtle
FONTS =('Arial', 12, 'bold')
ALIGNMENTS = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.color("white")
        self.penup()
        self.goto(-20, 280)
        self.hideturtle()


    def update_scoreboard(self):
        self.write(f"Score: {self.scores}", move=False, align= ALIGNMENTS, font=FONTS)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGNMENTS, font=FONTS)

    def increase_scores(self):
        self.scores += 1
        self.clear()
        self.update_scoreboard()