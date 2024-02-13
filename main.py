from turtle import Turtle, Screen
import random

# #race
tim = Turtle()
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
# turtles = []
# num_turtles = 5

# for i in range(num_turtles):
#     turtle = Turtle()
#     turtle.color(random.choice(colors))
#     turtle.penup()
#     turtle.goto(-200, -100 + i * 50)
#     turtles.append(turtle)

# for turtle in turtles:
#     turtle.speed(random.randint(1, 10))

# race_distance = 300

# while any(turtle.xcor() < race_distance for turtle in turtles):
#     for turtle in turtles:
#         turtle.forward(turtle.speed())
#         if turtle.xcor() >= race_distance:
#             turtle.goto(race_distance, turtle.ycor())

# screen.exitonclick()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")

screen.mainloop()