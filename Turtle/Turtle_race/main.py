import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manger = CarManager()
scoreboard  = Scoreboard()

screen.listen()

screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manger.create_random_car()
    car_manger.move_car()
     
    for car in car_manger.car_list:
        if player.distance(car) < 15:
         scoreboard.game_over()
         game_is_on= False
         

        if player.reach_finish_line():
            player.go_to_position()
            car_manger.level_up()
            scoreboard.increase_scores()
    

screen.exitonclick()
