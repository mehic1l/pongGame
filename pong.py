

import turtle
win = turtle.Screen()
win.title("Game by @mehic_l")
win.bgcolor("#F49FBC")
win.setup(width=800, height=600)
win.tracer(0)

#Score
score_a=0
score_b=0

#Player A
player_a=turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("black")
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.penup()
player_a.goto(-350,0)

#Player B
player_b=turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.color("black")
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.penup()
player_b.goto(+350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=-0.2

#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B:  0", align="center", font=("Courier", 20, "bold"))

#Functions
def player_aUp():
    y=player_a.ycor()
    y+=20
    player_a.sety(y)

def player_aDown():
    y=player_a.ycor()
    y-=20
    player_a.sety(y)

def player_bUp():
    y=player_b.ycor()
    y+=20
    player_b.sety(y)

def player_bDown():
    y=player_b.ycor()
    y-=20
    player_b.sety(y)

#Keyboard binding
win.listen()
win.onkeypress(player_aUp, "w")
win.onkeypress(player_aDown, "s")
win.onkeypress(player_bUp, "Up")
win.onkeypress(player_bDown, "Down")


#Game loop
while True:
    win.update()

    #Ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Setting borders
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}  Player B:  {}".format(score_a,score_b), align="center", font=("Courier", 20, "bold"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B:  {}".format(score_a,score_b), align="center", font=("Courier", 20, "bold"))

    #Paddle x ball
    if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<player_b.ycor()+40 and ball.ycor()>player_b.ycor()-50):
        ball.setx(340)
        ball.dx*=-1

    if ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<player_a.ycor()+40 and ball.ycor()>player_a.ycor()-50):
        ball.setx(-340)
        ball.dx*=-1
