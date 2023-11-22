from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.pair = ()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.dx = 10
        self.dy = 10
        self.move_speed = 0.1


    def bounce_off_walls(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        self.move_speed *= 0.9

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

