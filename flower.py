import turtle

#функція для малювання пелюстки
def draw_petal (t, radius, angle):
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)

# створення черепашки та її параметри
t = turtle.Turtle()
t.speed(24)
t.color("red")

# параметри квітки
number_of_petals = 24
radius = 424
angle = 24

# функція для малювання квітки
for i in range(number_of_petals):
     draw_petal(t, radius, angle)
     t.right(360 / number_of_petals)

turtle.done()
