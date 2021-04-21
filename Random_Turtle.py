import turtle
import random

turtle.title('거북이') 
turtle.shape('turtle')
turtle.pensize(5)
turtle.screensize(600, 600)

while True :  
    r = random.random()  
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))
    
    slope =  random.randrange(0,360)  
    road = random.randrange(50,300)
        
    turtle.left(slope) 
    turtle.forward(road)

    tX = turtle.xcor()
    tY = turtle.ycor()

    if(tX < -400 or tX > 400):
        turtle.backward(road*2)
    
    if(tY < -400 or tY > 400):
        turtle.backward(road*2)
