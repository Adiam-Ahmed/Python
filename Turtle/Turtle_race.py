import random
from turtle import Turtle, Screen 


is_race_on = False
my_screen = Screen()
my_screen.setup(width=500,height=400)
user_bet = my_screen.textinput(title="Bet time",prompt="Which turtle will win the race? Enter a color?")
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_pos = [-100,-50,0,50,100,150]
all_turtles=[]

for position in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(rainbow_colors[position])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=turtle_pos[position])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on= True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False 
            winning_color = turtle.pencolor()
            if winning_color== user_bet:
                print (f"You've won! The {winning_color} turtle is the winner")
            else:
                print (f"You've lost! The {winning_color} turtle is the winner")
        forward_random = random.randint(0,10)
        turtle.forward(forward_random)
    

  


my_screen.exitonclick()


