from turtle import Turtle


class DisplayWinner(Turtle):

    def __init__(self, winner):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=-200, y=0)
        self.write(winner + " is the winner!", font=("Arial", 40, "normal"))
