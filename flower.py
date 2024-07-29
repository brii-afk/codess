import turtle
import time

screen = turtle.Screen()
screen.bgcolor("light blue")

pen = turtle.Turtle()
pen.speed(3)  # Set the turtle speed to the fastest


def draw_petal(size, color):
    pen.color(color)
    pen.begin_fill()
    pen.circle(size, 60)
    pen.left(120)
    pen.circle(size, 60)
    pen.left(120)
    pen.end_fill()


def draw_flower(x, y, size, num_petals, colors):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    for i in range(num_petals):
        pen.setheading(360 / num_petals * i)
        draw_petal(size, colors[i % len(colors)])
        time.sleep(1)


colors = ["#FFB6C1", "#FF69B4", "#FF1493", "#DB7093", "#C71585"]

draw_flower(0, 0, 100, 12, colors)

pen.hideturtle()
screen.mainloop()