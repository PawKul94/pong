from turtle import Turtle
FONT = ("Courier", 48, "bold")
ALIGNMENT = "center"


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("grey")
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.clear()
        self.penup()
        self.setpos(-100, 200)
        self.pendown()
        self.write(arg=f"{self.p1_score}", align=ALIGNMENT, font=FONT)
        self.penup()
        self.setpos(100, 200)
        self.pendown()
        self.write(arg=f"{self.p2_score}", align="center", font=FONT)

    def increase_score(self, player):
        if player == "p1":
            self.p1_score += 1
            self.create_scoreboard()
        elif player == "p2":
            self.p2_score += 1
            self.create_scoreboard()
