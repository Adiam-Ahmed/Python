
from turtle import Screen
import turtle as t
import random


adiam = t.Turtle()
t.colormode(255)

heading = [0,90,180,270]
adiam.speed("fastest")

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colors = (r,g,b)
    return colors

def draw_spirography(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        adiam.color(random_color())
        adiam.circle(100)
        adiam.setheading(adiam.heading()+size_of_gap)

draw_spirography(5)


# for _ in range(1000):
#     adiam.color(random_color())
#     adiam.setheading(random.choice(heading))  
#     adiam.forward(30)






    



# n = 3
# while n < 10:
#     adiam.color(random.choice(colors))
#     for i in range(n):
        
#         adiam.forward(100)
#         adiam.right(360/n)
#     n+=1

























screen = Screen()
screen.exitonclick()