import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 5
        self.y_move = 5
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move = -1 * self.y_move

    def bounce_x(self):
        self.x_move = -1 * self.x_move
        self.ball_speed = self.ball_speed*0.9

    def new_round(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()

