import turtle
import time
import random

delay = 0.1

# Skor
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Ular Kadut Khas Lowokwaru")
wn.bgcolor("grey")
wn.setup(width=600, height=600)
wn.tracer(0) # Buat matiin screen updatenya

# Kepala uler
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#355E3B")
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

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("SCORE: 0  HIGH SCORE: 0", align= "center", font =("Courier", 24, "normal"))

# Fungsi pokoknya
def go_up():
    if head.direction != "down":
        head.direction = "up"
    
def go_down():
    if head.direction != "up":
        head.direction = "down"
    
def go_left():
    if head.direction != "right":
        head.direction = "left"
    
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
            
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
            
    elif head.direction == "right":
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
    
    # Ngecek tabrakan dengan border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        # Sembunyikan segment
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Bersihkan segments list
        segments.clear()
        
        # Reset skor
        score = 0
        
        # Reset delay
        delay = 0.1
        
        # Update display skor
        pen.clear() 
        pen.write("SCORE: {}  HIGH SCORE:  {}".format(score, high_score), align="center", font =("Courier", 24, "normal"))
        
        continue
    
    # Cek tabrakan dengan makanan
    if head.distance(food) < 20:
        # Taruh makanan ke random posisi
        x = random.randrange(-280, 281, 20)
        y = random.randrange(-280, 281, 20)
        food.goto(x, y)
        
        # Nambah segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#568203")
        new_segment.penup()
        segments.append(new_segment)
        
        # Kurangin delay (naikin kesulitan tiap makan)
        delay = max(0.03, delay - 0.001)
        
        # Naikin skor
        score += 1
        
        if score > high_score:
            high_score = score
           
        pen.clear() 
        pen.write("SCORE: {}  HIGH SCORE:  {}".format(score, high_score), align="center", font =("Courier", 24, "normal"))
    
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
    
    # Cek tabrakan dengan badan sendiri
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            # Sembunyikan segment
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Bersihkan segments list
            segments.clear()
            
            # Reset skor
            score = 0
            
            # Reset delay
            delay = 0.1
            
            # Update display skor
            pen.clear() 
            pen.write("SCORE: {}  HIGH SCORE:  {}".format(score, high_score), align="center", font =("Courier", 24, "normal"))

            continue
    
    time.sleep(delay)

# wn.mainloop()