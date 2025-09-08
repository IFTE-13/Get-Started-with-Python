# Ping Pong Game with Turtle

# Create a two-player Ping Pong game using Python's turtle module.

# Requirements:
# 1. Two paddles (left and right) controlled by players (w/s for left, Up/Down for right).
# 2. A ball that moves continuously and bounces off the top/bottom walls.
# 3. The ball should bounce off paddles and reset when it passes the left or right edges.
# 4. A score system: each player starts with 3 lives. When the ball passes a paddle, the opponent loses a life.
# 5. Display “Game Over” when either player runs out of lives.

import turtle as t

# -----------------------------
# Variables
# -----------------------------
playerA = 3
playerB = 3
ball_speed_x = 0.2
ball_speed_y = 0.2

# -----------------------------
# Window setup
# -----------------------------
window = t.Screen()
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# -----------------------------
# Left paddle
# -----------------------------
leftPaddle = t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

# -----------------------------
# Right paddle
# -----------------------------
rightPaddle = t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(350, 0)

# -----------------------------
# Ball
# -----------------------------
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)

# -----------------------------
# Score Display
# -----------------------------
pen = t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {playerA}   Player B: {playerB}", align="center", font=("Arial", 24, "normal"))

# -----------------------------
# Paddle movement functions
# -----------------------------
def left_paddle_up():
    y = leftPaddle.ycor()
    y += 15
    leftPaddle.sety(y)

def left_paddle_down():
    y = leftPaddle.ycor()
    y -= 15
    leftPaddle.sety(y)

def right_paddle_up():
    y = rightPaddle.ycor()
    y += 15
    rightPaddle.sety(y)

def right_paddle_down():
    y = rightPaddle.ycor()
    y -= 15
    rightPaddle.sety(y)

# -----------------------------
# Keyboard bindings
# -----------------------------
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

# -----------------------------
# Main game loop
# -----------------------------
while True:
    if playerA > 0 and playerB > 0:
        window.update()

        # Move the ball
        ball.setx(ball.xcor() + ball_speed_x)
        ball.sety(ball.ycor() + ball_speed_y)

        # Top and bottom border collision
        if ball.ycor() > 290:
            ball.sety(290)
            ball_speed_y *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball_speed_y *= -1

        # Right border - Player A scores
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball_speed_x *= -1
            playerA -= 1
            pen.clear()
            pen.write(f"Player A: {playerA}   Player B: {playerB}", align="center", font=("Arial", 24, "normal"))

        # Left border - Player B scores
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball_speed_x *= -1
            playerB -= 1
            pen.clear()
            pen.write(f"Player A: {playerA}   Player B: {playerB}", align="center", font=("Arial", 24, "normal"))

        # Paddle collisions
        if (340 < ball.xcor() < 350) and (rightPaddle.ycor() - 50 < ball.ycor() < rightPaddle.ycor() + 50):
            ball.setx(340)
            ball_speed_x *= -1

        if (-350 < ball.xcor() < -340) and (leftPaddle.ycor() - 50 < ball.ycor() < leftPaddle.ycor() + 50):
            ball.setx(-340)
            ball_speed_x *= -1

    else:
        # Game Over
        window.clearscreen()
        t.Turtle().write("GAME OVER", align="center", font=("Arial", 36, "bold"))
        break
