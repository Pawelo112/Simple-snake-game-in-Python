from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Courier", 19, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 19, "normal"))

    def update_score(self):
        """Method that updates the score after snake hits the food"""
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 19, "normal"))
