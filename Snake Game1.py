import turtle
import random
import time

delay = 0.1
sc = 0
hs = 0

bodies = []
# creating a screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("pink")
s.setup(height=600, width=600)

# creating Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("White")
head.fillcolor("yellow")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.shape("circle")
food.color("black")
food.penup()
food.ht()  # hide turtle
food.goto(150, -200)
food.st()

# ScoreBoard
sb = turtle.Turtle()
sb.ht()
sb.penup()
sb.goto(-250, 250)
sb.write("Score: 0 | highest score: 0", font=('Arial', 15, 'bold'))  # to print ScoreBoard


def moveup():
    if head.direction != "down":
        head.direction = "up"
     
def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Event handling - Key Mapping
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")

# mainloop
while True:
    s.update()  # to update the screen

    # Check collision with border
    if head.xcor() > 290:
        head.setx(-290)

    if head.xcor() < -290:
        head.setx(290)

    if head.ycor() > 290:
        head.sety(-290)

    if head.ycor() < -290:
        head.sety(290)

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # increase the body of snake
        body = turtle.Turtle()
        body.speed()
        body.penup()
        body.shape("square")
        body.color("black")
        body.fillcolor("red")
        bodies.append(body)  # append new body in list
        sc += 10
        delay -= 0.001  # increase the speed

        if sc > hs:
            hs = sc  # update the highest score
        sb.clear()
        sb.write("Score: {} | highest score: {}".format(sc, hs), font=('Arial', 15, 'bold'))

    # Move snake bodies
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            sc = 0
            delay = 0.1
            sb.clear()
            sb.write("Score: {} | highest score: {}".format(sc, hs), font=('Arial', 15, 'bold'))
            time.sleep(delay)

    time.sleep(delay)

s.mainloop()
