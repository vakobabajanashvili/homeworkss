from turtle import*

width(5)
speed(50)

def otxkutxedi():
    for i in range(4):
        forward(100)
        left(90)
otxkutxedi()

penup()
goto(100, 100)
pendown()
otxkutxedi()

penup()
goto(-100, -100)
pendown()
otxkutxedi()

penup()
left(90)
forward(200)
pendown()
def kubiki():
    for i in range(4):
        forward(100)
        right(90)
kubiki()

penup()
right(90)
forward(200)
right(90)
forward(100)
pendown()
def kubikuri():
    for i in range(4):
        forward(100)
        left(90)
kubikuri()
exitonclick()