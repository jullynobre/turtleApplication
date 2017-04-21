##equação exemplo y=x^2
##escala exemplo 10 pixeis por unidade
##escala=10
##coordenadas_cruas=[-3,9,-2,4,-1,1,0,0,1,1,2,4,3,9]
##coordenadas=[escala*coordenadas for coordenadas in coordenadas_cruas]

import turtle
##turtle.hideturtle()


def background(scale):
    turtle.color('black')
    turtle.hideturtle()
    turtle.tracer(0, 0)
    width = turtle.window_width()
    height = turtle.window_height()
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
    turtle.backward(30)
    turtle.forward(30)
    turtle.left(80)
    turtle.backward(30)
    turtle.forward(30)
    turtle.right(40)
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

    a = int(width/scale*2)
    for i in range(a):
        turtle.forward(int(scale))
        turtle.right(90)
        turtle.forward(5)
        turtle.backward(5)
        turtle.left(90)

    turtle.home()
    turtle.left(180)

    

    for i in range(a):
        turtle.forward(scale)
        turtle.left(90)
        turtle.forward(5)
        turtle.backward(5)
        turtle.right(90)

    turtle.home()

    b=int((height/scale)/2)
    turtle.left(90)
    for i in range(b):
        turtle.forward(scale)
        turtle.right(90)
        turtle.forward(5)
        turtle.backward(5)
        turtle.left(90)

    turtle.home()
    turtle.right(90)

    for i in range(b):
        turtle.forward(scale)
        turtle.left(90)
        turtle.forward(5)
        turtle.backward(5)
        turtle.right(90)

    turtle.home()

    #escala
    turtle.penup()
    turtle.right(90)
    turtle.forward(height/2-20)
    turtle.left(90)
    label_size=len(str(scale))*6+62
    turtle.forward(width/2-label_size-scale-30)

    turtle.write(str(scale))
    turtle.forward(len(str(scale))*6-55)
    turtle.write('Escala =')
    turtle.forward(55)
    turtle.write(':1')

    turtle.forward(17)
    turtle.left(90)
    turtle.forward(8)
    turtle.right(90)

    turtle.pendown()
    turtle.right(90)
    turtle.forward(5)
    turtle.backward(10)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(scale)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(5)
    turtle.backward(10)
    turtle.forward(5)
    turtle.left(90)
    turtle.penup()
    turtle.forward(30)

    turtle.home()
    turtle.pendown()
    turtle.update()


def grafic(coordinates,scale):
##    turtle.shape('triangle')
##    turtle.showturtle()
    turtle.penup()
    turtle.color('red')
    turtle.setpos(coordinates[0],coordinates[1])
    x=int(len(coordinates)/2)
    turtle.pendown()
    cont=0
    
    for i in range(x):
        turtle.setpos(coordinates[cont],coordinates[cont+1])
        cont += 2
    


def draw(raw_coordinates, scale):
    coordinates = [scale*coordinates for coordinates in raw_coordinates]
    background(scale)
    grafic(coordinates, scale)



