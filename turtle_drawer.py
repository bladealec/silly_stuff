import turtle

#initialize the screen
screen = turtle.Screen()
screen.title("Test of Turtle")
screen.bgcolor("black")

#initialize the turtle
pen = turtle.Turtle()
pen.speed(2)  #drawing speed

def draw_square(size):
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

def draw_triangle(size):
    for _ in range(3):
        pen.forward(size)
        pen.right(120)

def draw_circle(radius):
    pen.circle(radius)

#drawing sequence
pen.color("blue")
pen.penup()
pen.goto(-150, 100)
pen.pendown()
draw_square(100) 

pen.color("green")
pen.penup()
pen.goto(100, 100)
pen.pendown()
draw_triangle(100)  

pen.color("red")
pen.penup()
pen.goto(0, -100)
pen.pendown()
draw_circle(50)

#hide turtle and display result
pen.hideturtle()
screen.mainloop()
