from turtle import Turtle, Screen
import time


class Snake:

# Initialise
    def __init__(self):
        self.SegList = []
        screen = Screen()
        screen.tracer(0)
        self.create_snake()
        screen.update()
        self.head = self.SegList[0]


    def create_snake(self):
        xcord = 0
        ycord = 0
        for _ in range(3):
            self.SegList.append(self.snake_part(xcord=xcord, ycord=ycord))
            xcord -= 20
        self.head = self.SegList[0]


    def reset(self):
        for seg in self.SegList:
            seg.goto(1000, 1000)
        self.SegList.clear()
        self.create_snake()


    def move(self):
        time.sleep(0.15)
        for segment in range(len(self.SegList) - 1, 0, -1):
            Xval = self.SegList[segment - 1].xcor()
            Yval = self.SegList[segment - 1].ycor()
            self.SegList[segment].goto(Xval, Yval)
        self.head.forward(20)


    def snake_part(self, xcord, ycord):
        t = Turtle()
        t.shape('square')
        t.color('white')
        t.penup()
        t.goto(x = xcord, y= ycord)
        return t


    def extend(self):
        x = self.SegList[-1].xcor()
        y = self.SegList[-1].ycor()

        self.SegList.append(self.snake_part(x, y))


# Motion
    def up(self):
        if not self.SegList[0].heading() == 270:
            self.SegList[0].setheading(90)
        else:
            return


    def down(self):
        if not self.SegList[0].heading() == 90:
            self.SegList[0].setheading(270)
        else:
            return


    def right(self):
        if not self.SegList[0].heading() == 180:
            self.SegList[0].setheading(0)
        else:
            return


    def left(self):
        if not self.SegList[0].heading() == 0:
            self.SegList[0].setheading(180)
        else:
            return
