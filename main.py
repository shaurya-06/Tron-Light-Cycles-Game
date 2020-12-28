from turtle import Turtle, Screen
from players import Players
from display_winner import DisplayWinner
import time

screen = Screen()
screen.title("TRON - Light Cycles")
screen.bgcolor("black")
screen.setup(width=900, height=900)
screen.tracer(0)

heading = Turtle()
heading.hideturtle()
heading.color("white")
heading.penup()
heading.goto(x=-60, y=390)
heading.write("TRON", font=("Arial", 40, "bold"))

blue_player = Players(color="aquamarine", heading=0, pos_x=-420, pos_y=0)
orange_player = Players(color="orange", heading=180, pos_x=420, pos_y=0)
game_is_on = True

screen.listen()
screen.onkey(orange_player.up, "Up")
screen.onkey(orange_player.down, "Down")
screen.onkey(orange_player.left, "Left")
screen.onkey(orange_player.right, "Right")
screen.onkey(blue_player.up, "w")
screen.onkey(blue_player.down, "s")
screen.onkey(blue_player.left, "a")
screen.onkey(blue_player.right, "d")

while game_is_on:
    blue_player.pos.append(blue_player.position())
    orange_player.pos.append(orange_player.position())
    screen.update()
    time.sleep(0.1)
    orange_player.forward(10)
    blue_player.forward(10)

    for orange_pos in orange_player.pos:
        if blue_player.distance(orange_pos) <= 1:
            display_winner = DisplayWinner("Orange")
            game_is_on = False
            break
        if not game_is_on:
            break

    for blue_pos in blue_player.pos:
        if orange_player.distance(blue_pos) <= 1:
            display_winner = DisplayWinner("Blue")
            game_is_on = False
            break
        if not game_is_on:
            break

    if blue_player.xcor() >= 445 or blue_player.ycor() >= 445 or blue_player.xcor() <= -445 or blue_player.ycor() <= -445:
        game_is_on = False
        display_winner = DisplayWinner("Orange")
        break

    if orange_player.xcor() >= 445 or orange_player.ycor() >= 445 or orange_player.xcor() <= -445 or orange_player.ycor() <= -445:
        game_is_on = False
        display_winner = DisplayWinner("Blue")
        break

screen.exitonclick()
