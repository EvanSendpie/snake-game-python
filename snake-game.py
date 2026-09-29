import turtle

wn = turtle.Screen()
wn.title("Ular Kadut Khas Lowokwaru")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Kepala uler
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")

wn.mainloop()