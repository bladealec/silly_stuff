import turtle
import random

def draw_square(size, pen):
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

def draw_triangle(size, pen):
    for _ in range(3):
        pen.forward(size)
        pen.right(120)

def draw_star(size, pen):
    for _ in range(5):
        pen.forward(size)
        pen.right(144)

def draw_circle(radius, pen):
    pen.circle(radius)

def draw_spirograph(radius, offset, pen):
    for angle in range(0, 360, offset):
        pen.setheading(angle)
        pen.circle(radius)

def draw_branch(t, branch_length, angle, depth):
    if depth == 0:
        return
    t.forward(branch_length)
    t.left(angle)
    draw_branch(t, branch_length * 0.7, angle, depth - 1)
    t.right(angle * 2)
    draw_branch(t, branch_length * 0.7, angle, depth - 1)
    t.left(angle)
    t.backward(branch_length)

def draw_fractal_tree(pen):
    pen.left(90)
    draw_branch(pen, 100, 30, 5)

def draw_firework(pen):
    colors = ["red", "yellow", "blue", "green", "purple", "orange"]
    for _ in range(36):
        pen.color(random.choice(colors))
        pen.forward(random.randint(50, 150))
        pen.backward(random.randint(50, 150))
        pen.right(10)

def draw_kaleidoscope(pen):
    colors = ["red", "yellow", "blue", "green", "purple", "orange"]
    for _ in range(36):
        pen.color(random.choice(colors))
        pen.forward(100)
        pen.left(60)
        pen.forward(50)
        pen.left(120)
        pen.forward(50)
        pen.right(90)
        pen.forward(30)
        pen.right(90)
        pen.forward(30)
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        pen.right(10)

def draw_mandala(pen):
    for _ in range(36):
        for _ in range(6):
            pen.forward(50)
            pen.backward(50)
            pen.right(60)
        pen.right(10)

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Shape Drawing Program")
    pen = turtle.Turtle()
    pen.speed(0)

    while True:
        print("Select a shape or pattern to draw:")
        print("1: Square")
        print("2: Triangle")
        print("3: Star")
        print("4: Circle")
        print("5: Spirograph")
        print("6: Fractal Tree")
        print("7: Firework")
        print("8: Kaleidoscope")
        print("9: Mandala")
        print("0: Exit")

        choice = input("Enter your choice (0-9): ")
        pen.clear()
        pen.reset()
        pen.speed(0)
        if choice == "1":
            draw_square(100, pen)
        elif choice == "2":
            draw_triangle(100, pen)
        elif choice == "3":
            draw_star(150, pen)
        elif choice == "4":
            draw_circle(100, pen)
        elif choice == "5":
            draw_spirograph(100, 15, pen)
        elif choice == "6":
            draw_fractal_tree(pen)
        elif choice == "7":
            draw_firework(pen)
        elif choice == "8":
            draw_kaleidoscope(pen)
        elif choice == "9":
            draw_mandala(pen)
        elif choice == "0":
            screen.bye()
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
