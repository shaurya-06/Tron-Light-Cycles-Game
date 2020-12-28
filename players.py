from turtle import Turtle


class Players(Turtle):

    def __init__(self, color, heading, pos_x, pos_y):
        super().__init__()
        self.penup()
        self.color(color)
        self.setheading(heading)
        self.goto(x=pos_x, y=pos_y)
        self.speed("fast")
        self.pendown()
        self.pos = []

    def up(self):
        if self.heading() != 270:
            self.setheading(90)

    def down(self):
        if self.heading() != 90:
            self.setheading(270)

    def left(self):
        if self.heading() != 0:
            self.setheading(180)

    def right(self):
        if self.heading() != 180:
            self.setheading(0)
            self.forward(10)
