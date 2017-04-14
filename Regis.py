coordenadas=[-30,90,-20,40,-10,10,0,0,10,10,20,40,30,90]
import turtle
turtle.speed(-5)
turtle.hideturtle()
def scale():
    width=turtle.window_width()
    height=turtle.window_height()
    turtle.left(90)
    turtle.forward(height/2)

    turtle.backward(10)
    turtle.right(40)
    turtle.backward(30)
    turtle.forward(30)
    turtle.left(80)
    turtle.backward(30)
    turtle.forward(30)
    turtle.right(40)
    turtle.backward(50)
    turtle.penup()
    turtle.right(90)
    turtle.forward(15)
    turtle.write('x')
    turtle.backward(15)
    turtle.left(90)
    turtle.forward(60)
    turtle.pendown()
    
    
    
    turtle.backward(height)
    turtle.forward(height/2)
    turtle.right(90)
    turtle.forward(width/2)

    turtle.backward(10)
    turtle.right(40)
    turtle.begin_fill()
    turtle.backward(30)
    turtle.forward(30)
    turtle.left(80)
    turtle.backward(30)
    turtle.forward(30)
    turtle.right(40)
    turtle.end_fill()
    turtle.forward(10)

    turtle.backward(50)
    turtle.penup()
    turtle.left(90)
    turtle.forward(15)
    turtle.write('y')
    turtle.backward(15)
    turtle.right(90)
    turtle.forward(60)
    turtle.pendown()
    
    turtle.backward(width)
    turtle.home()

    #escala

    #distancia x vezes escala igual a distancia em pixeis

    escala=10
    a=int((width/escala)/2)
    for i in range(a):
        turtle.forward(escala)
        turtle.right(90)
        turtle.forward(5)
        turtle.backward(5)
        turtle.left(90)

    turtle.home()
    turtle.left(180)

    for i in range(a):
        turtle.forward(escala)
        turtle.left(90)
        turtle.forward(5)
        turtle.backward(5)
        turtle.right(90)

    turtle.home()

    b=int((height/escala)/2)
    turtle.left(90)
    for i in range(b):
        turtle.forward(escala)
        turtle.right(90)
        turtle.forward(5)
        turtle.backward(5)
        turtle.left(90)

    turtle.home()
    turtle.right(90)

    for i in range(b):
        turtle.forward(escala)
        turtle.left(90)
        turtle.forward(5)
        turtle.backward(5)
        turtle.right(90)

    turtle.home()



    
def grafic():
    turtle.tracer(0,0)
    scale()
    turtle.penup()
    turtle.setpos(coordenadas[0],coordenadas[1])
    x=int(len(coordenadas)/2)
    turtle.pendown()
    cont=0
    for i in range(x):
        turtle.setpos(coordenadas[cont],coordenadas[cont+1])
        cont += 2
    turtle.update()
grafic()
turtle.update()
#lines()
