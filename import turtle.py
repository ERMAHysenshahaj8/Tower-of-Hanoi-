import turtle
import time

def draw_pole(pen, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.forward(10)
    pen.left(90)
    pen.forward(100)
    pen.right(90)

def draw_disk(pen, width, height, color, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

def tower_of_hanoi_visual(n, source, auxiliary, target, pen, speed):
    pole_positions = {'A': -150, 'B': 0, 'C': 150}
    disk_height = 20
    disk_width_factor = 20

    def draw_state(state):
        pen.clear()
        for pole, disks in state.items():
            draw_pole(pen, pole_positions[pole], -50)
            for i, disk in enumerate(disks):
                draw_disk(pen, disk * disk_width_factor, disk_height, 'blue', pole_positions[pole] - (disk * disk_width_factor) / 2, i * disk_height)

        turtle.update()

    def move_disk(source, target):
        disk = towers[source].pop()
        towers[target].append(disk)
        draw_state(towers)
        time.sleep(speed)

    def hanoi_recursive(n, source, auxiliary, target):
        if n > 0:
            hanoi_recursive(n-1, source, target, auxiliary)
            move_disk(source, target)
            hanoi_recursive(n-1, auxiliary, source, target)

    towers = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    draw_state(towers)
    hanoi_recursive(n, source, auxiliary, target)

# Set up the Turtle graphics window
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.tracer(0)  # Turn off automatic updates

pen = turtle.Turtle()

# Set animation speed
speed = 0.1  # Adjust this value for faster/slower animation

# Call the Tower of Hanoi function with 3 disks and the peg names
tower_of_hanoi_visual(3, "A", "B", "C", pen, speed)

# Keep the graphics window open
turtle.done()
