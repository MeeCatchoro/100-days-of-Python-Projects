from turtle import Screen
from paddle import Player, Computer
from ball import Ball
from scoreboard import PlayerScore, ComputerScore, Division
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 800)
screen.title("Pong")
screen.tracer(0)

player = Player()
computer = Computer()
player_score = PlayerScore()
computer_score = ComputerScore()
ball = Ball()
division = Division()

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    ballx = ball.xcor()
    bally = ball.ycor()

    # Computer brain
    if bally > computer.y()[0]-20:
        computer.up()
    elif bally < computer.y()[1]+20:
        computer.down()

    # Detects collision with walls
    if bally > 385 or bally < (-385):
        ball.wall_collision()

    # Detects collision with paddles
    if player.x()[0] >= ballx >= player.x()[1] and player.y()[0] >= bally >= player.y()[1]:
        ball.paddle_collision()
    elif computer.x()[0] >= ballx >= computer.x()[1] and computer.y()[0] >= bally >= computer.y()[1]:
        ball.paddle_collision()

    # Score points
    if ballx >= 385:
        ball.refresh("right")
        player_score.increase_score()
    elif ballx <= -385:
        ball.refresh("left")
        computer_score.increase_score()

    if player_score.score == 11:
        player_score.player_wins()
        game_is_on = False
    elif computer_score.score == 11:
        computer_score.computer_wins()
        game_is_on = False

screen.exitonclick()
