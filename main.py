import turtle as t
import random
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    rgb_tuple = (r,g,b)
    return rgb_tuple

timmmy_the_turtle = t.Turtle()
timmmy_the_turtle.speed(50)
def draw_spirograph(size_of_gap):
    angle = size_of_gap
    for _ in range(360//size_of_gap):    
        timmmy_the_turtle.circle(100)
        timmmy_the_turtle.setheading(angle)
        timmmy_the_turtle.color(random_color())
        angle+=size_of_gap
draw_spirograph(10)
screen = t.Screen()
screen.exitonclick()