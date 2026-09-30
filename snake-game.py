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

# Fungsi pokoknya
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

segments = []

# Main game loop
while True:
    wn.update()
    
    # Ngecek tabrakan dengan border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        # Sembunyikan segment
        for segment in segments:
            segment.got0(1000, 1000)
        
        # Bersihkan segments list
        segments.clear()
    
    # Cek tabrakan dengan makanan
    if head.distance(food) < 20:
        # Taruh makanan ke random posisi
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)
        
        # Nambah segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
    
    # Memindahkan segment akhir ke awal 
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    # Move segment 0 to where the head is (gatau indonya)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
    move()
    
    time.sleep(delay)

wn.mainloop()