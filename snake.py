from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color(f"light green")

    def create_snake(self):
        for position in STARTING_POSITION:
            self.make_segment(position)

    def make_segment(self, position):
        new_segment = Turtle(shape="circle")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    

    def add_segment(self):
        self.make_segment(self.segments[-1].position())


    def reset(self):
        for seg in self.segments:
            seg.goto(-1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.color(f"light green")

    def move(self):
        for num_seg in range(len(self.segments)-1, 0, -1):
            front_seg = num_seg - 1
            new_x = self.segments[front_seg].xcor()
            new_y = self.segments[front_seg].ycor()
            self.segments[num_seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def Up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)
        
    def Down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)

    def Right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)

    def Left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)