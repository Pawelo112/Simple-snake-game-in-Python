from turtle import Turtle
import random

FOOD_TYPES = ["blue", "red", "orange", "green"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Method that puts food in a new random position"""
        self.color(random.choice(FOOD_TYPES))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
