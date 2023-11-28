import turtle
t=turtle.Pen()
s=turtle.Screen()
t.pensize(3)
t.penup()          #터틀 팬 때기

x, y = -100,100
t.goto(x, y)
t.pendown()
t.circle(100) #반지름이 100인 원 그리기

#입 그리기
t.penup()
t.goto(x-60.62, y+65)
t.pendown()
t.right(45)
t.circle(80, 100)

#눈 그리기
t.penup()
t.goto(x-60.62, y+120)
t.dot(30)
t.goto(x+60.62, y+120)
t.dot(30)
