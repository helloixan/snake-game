from turtle import Turtle
from random import randint

class Food(Turtle) :

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.penup()
        self.update()
    
    def update(self):
        random_position = randint(-280, 280)
        self.goto(x=random_position, y=random_position)

