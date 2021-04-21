import turtle

## 전역 변수 선언 부분 ##
swidth, sheight = 500, 500

## 메인 코드 부분 ##
turtle.title('무지개색 원그리기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50) #창 크기에 사용할 변수 준비
turtle.screensize(swidth, sheight) # 윈도창 설정
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.speed('fastest') #거북이 속도 설정

for radius in range(-125,124) : #반지름(radius) 1에서 249까지 원을 반복해 그림
    if radius % 6 == 0 :
        turtle.pencolor('red') #반지름에 따라 빨주노초파남보 색상이 반복 설정
    elif radius % 5 == 0 :
        turtle.pencolor('orange')
    elif radius % 4 == 0 :
        turtle.pencolor('yellow')
    elif radius % 3 == 0 :
        turtle.pencolor('green')
    elif radius % 2 == 0 :
        turtle.pencolor('blue')
    elif radius % 1 == 0 :
        turtle.pencolor('navyblue')
    else :
        turtle.pencolor('purple')

    turtle.circle(radius)  #거북이 원을 그림

turtle.done()
