import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()

    for car in car_manager.hitbox():
        if car[0][0] >= 0 >= car[0][1] and (car[1][0] >= player.y()[0] >= car[1][1] or car[1][0] >= player.y()[1] >= car[1][1]):
            game_is_on = False
            scoreboard.game_over()

    if player.y()[0] >= player.finish_line:
        player.refresh()
        car_manager.refresh()
        scoreboard.increase_level()


screen.exitonclick()
