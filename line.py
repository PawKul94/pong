from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("grey")
        self.pensize(3)
        self.setpos(0, 300)
        self.setheading(270)

        for _ in range(19):
            self.forward(15)
            self.pendown()
            self.forward(15)
            self.penup()
