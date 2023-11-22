from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT_SCORE = 'left'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.color("black")
        self.penup()
        self.goto(-280, 270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Level: {self.scores}", move=False, align= ALIGNMENT_SCORE, font=FONT)

    
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=FONT)

    def increase_scores(self):
        self.scores += 1
        self.clear()
        self.update_scoreboard()