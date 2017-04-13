coordenadas=[-30,90,-20,40,-10,10,0,0,10,10,20,40,30,90]
import turtle
turtle.speed(0)
turtle.hideturtle()
def lines():
    width=turtle.window_width()
    height=turtle.window_height()
    turtle.left(90)
    turtle.forward(height/2)
    turtle.backward(height)
    turtle.forward(height/2)
    turtle.right(90)
    turtle.forward(width/2)
    turtle.backward(width)
    turtle.home()
def grafic():
    lines()
    turtle.penup()
    turtle.setpos(coordenadas[0],coordenadas[1])
    x=int(len(coordenadas)/2)
    turtle.pendown()
    cont=0
    for i in range(x):
        turtle.setpos(coordenadas[cont],coordenadas[cont+1])
        cont += 2

grafic()
#lines()
