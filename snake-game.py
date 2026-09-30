import turtle
import time
import random

delay = 0.1

wn = turtle.Screen()
wn.title("Ular Kadut Khas Lowokwaru")
wn.bgcolor("cyan")
wn.setup(width=600, height=600)
wn.tracer(0) # Buat matiin screen updatenya

# Kepala uler
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Makanan Uler
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
food.direction = "stop"

def go_up():
    head.direction = "up"
    
def go_down():
    head.direction = "down"
    
def go_left():
    head.direction = "left"
    
def go_right():
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
            
# Keybind
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Main game loop
while True:
    wn.update()
    
    if head.distance(food) < 20:
        # Taruh makanan ke random posisi
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)
    
    move()
    
    time.sleep(delay)

wn.mainloop()