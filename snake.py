import turtle
from object_class import Create_Object
import time
import random

wn = turtle.Screen()
wn.setup(700, 700)
wn.bgcolor('black')
wn.title('SNAKE GAME')
wn.tracer(0)

flag = False
segments = []
block = 1
score = 0

head = Create_Object('head', 'dark green', 'square')
head = head.Create()

snake_food = Create_Object('snake_food', 'dark red', 'square')
snake_food = snake_food.Create()
snake_food_x = random.randint(-280, 280)
snake_food_y = random.randint(-280, 280)
snake_food.setposition(snake_food_x, snake_food_y)

border = Create_Object('border', 'blue')
border = border.Create()
border.hideturtle()
border.setposition(-300, -300)
border.pensize(4)
border.pendown()
for i in range(4):
    border.fd(600)
    border.lt(90)

pen = Create_Object('pen', 'green')
pen = pen.Create()
pen.hideturtle()

def flag_quit():
    global flag
    flag = True

def left():
    if head.heading() != 0:
        head.setheading(180)
    else:
        if len(segments) < 2:
            head.setheading(180)
        else:
            flag_quit()

def right():
    if head.heading() != 180:
        head.setheading(0)
    else:
        if len(segments) < 2:
            head.setheading(0)
        else:
            flag_quit()

def up():
    if head.heading() != 270:
        head.setheading(90)
    else:
        if len(segments) < 2:
            head.setheading(90)
        else:
            flag_quit()

def down():
    if head.heading() != 90:
        head.setheading(270)
    else:
        if len(segments) < 2:
            head.setheading(270)
        else:
            flag_quit()

def move():
    x = head.xcor()
    y = head.ycor()
    if head.heading() == 0:
        x += 20 + block
        if x > 295:
            x = -285
        head.setx(x + block)
    elif head.heading() == 180:
        x -= (20 + block)
        if x < -290:
            x = 285
        head.setx(x - block)

    elif head.heading() == 90:
        y += 20 + block
        if y > 290:
            y = -285
        head.sety(y + block)
    elif head.heading() == 270:
        y -= (20 + block)
        if y < -290:
            y = 285
        head.sety(y - block)

def food():
    snake_food_x = random.randint(-280, 280)
    snake_food_y = random.randint(-280, 280)
    snake_food.setposition(snake_food_x, snake_food_y)

def high_score_write():
    global line
    f = open('high_score.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        try:
            line = int(line)
            break
        except:
            pass
    pen.color('green')
    pen.setposition(290, 310)
    pen.write('High Score: {0}'.format(line), False, align="right", font=("Arial", 16, "bold"))

def score_write():
    score_string = 'Score: {0}'.format(score)
    pen.setposition(-290, 310)
    pen.color('white')
    pen.write(score_string, False, align="left", font=("Arial", 16, "bold"))


def Game_Over():
    pen.setposition(0, -20)
    pen.color('red')
    pen.write('GAME OVER', False, align='center', font=("Arial", 50, "normal"))

wn.listen()
wn.onkeypress(flag_quit, 'q')
wn.onkeypress(right, 'Right')
wn.onkeypress(left, 'Left')
wn.onkeypress(up, 'Up')
wn.onkeypress(down, 'Down')

score_write()
high_score_write()

while True:
    wn.update()
    if flag == True:
        break

    if head.distance(snake_food) < 20:
        food()
        score += 1
        pen.clear()
        score_write()
        high_score_write()
        new_segment = Create_Object('new_segment', 'dark green', 'square')
        new_segment = new_segment.Create()
        segments.append(new_segment)

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].setposition(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    for segment in segments:
        if head.distance(segment) < 20:
            flag = True
        if segment.distance(snake_food) < 20:
            food()

    time.sleep(0.07)
Game_Over()
time.sleep(3)
turtle.bye()
if score > line:
    f = open('high_score.txt', 'w')
    f.write(str(score) + '\r\n')
    f.close()