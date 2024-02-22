from turtle import Turtle, Screen
ALIGN =   "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    self.goto(0, 270)
    self.update_score()
    self.hideturtle()

  def update_score(self):
    self.clear()
    self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

  def gameover(self):
    self.goto(0, 0)
    self.write("GAME OVER", align=ALIGN, font=FONT)

  def increase(self):
    self.score += 1
    self.update_score()
