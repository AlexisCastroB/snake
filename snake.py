from turtle import Turtle
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for pos in START_POSITION:
      self.add(pos)

  def add(self, pos):
      seg = Turtle('square')
      seg.color('white')
      seg.penup()
      seg.goto(pos)
      self.segments.append(seg)

  def grow(self):
    self.add(self.segments[-1].position())

  def move(self):
    for seg in range(len(self.segments) - 1, 0, -1):
      [x, y] = self.segments[seg - 1].pos()
      self.segments[seg].goto(x, y)
    self.head.forward(DISTANCE)

  def transport(self):
    for seg in range(len(self.segments) - 1, 0, -1):
      [x, y] = self.segments[seg - 1].pos()
      self.segments[seg].goto(x, y)
    [portal_x, portal_y] = self.head.pos()
    if abs(portal_x) > 280:
      portal_x *= -1
    if abs(portal_y) > 280:
      portal_y *= -1
    self.head.goto(portal_x, portal_y)

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
