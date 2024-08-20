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
        self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Method that updates current scores displayed at the scoreboard"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 19, "normal"))

    def reset(self):
        """Updates the scoreboard and high score if needed after dying with snake."""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def update_score(self):
        """Method that updates the score after snake hits the food"""
        self.score += 1
        self.update_scoreboard()