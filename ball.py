from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.just_hit = False

    def bounce_x(self):
        if not self.just_hit:
            self.x_move *= -1
            self.move_speed *= 0.9
        self.just_hit = True

    def bounce_y(self):
        self.y_move *= -1

    def move(self):
        self.setpos(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def reset_just_hit(self):
        self.just_hit = False

    def reset_position(self):
        self.setpos(0, 0)
        self.bounce_x()
