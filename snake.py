from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = ((0, 0), (-20, 0), (-40, 0))


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):

        # Creating first three snake starting parts
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Method that creates one snake segment"""
        snake_part = Turtle()
        snake_part.penup()
        snake_part.shape("square")
        snake_part.color("white")
        snake_part.goto(position)
        self.snake_parts.append(snake_part)

    def extend(self):
        """Method that adds new segment to the snake, after eating food"""
        self.add_segment(self.snake_parts[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        """Method that allows snake to move itself"""
        snake = self.snake_parts
        for segment_num in range(len(snake) - 1, 0, -1):
            new_x = snake[segment_num - 1].xcor()
            new_y = snake[segment_num - 1].ycor()
            snake[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
