##equação exemplo y=x^2
##escala exemplo 10 pixeis por unidade
##escala=10
##coordenadas_cruas=[-3,9,-2,4,-1,1,0,0,1,1,2,4,3,9]
##coordenadas=[escala*coordenadas for coordenadas in coordenadas_cruas]

import turtle
##turtle.hideturtle()


def background(scale):
    width = turtle.window_width()
    height = turtle.window_height()
    turtle.tracer(0, 0)
    turtle.color('blue')
    turtle.pensize(1)
    a = int(width/scale*2)
    for i in range(a):
        turtle.penup()
        turtle.forward(int(scale))
        turtle.pendown()
        turtle.right(90)
        turtle.forward(height/2)
        turtle.backward(height)
        turtle.forward(height/2)
        turtle.left(90)
    
    turtle.penup()
    turtle.home()
    turtle.left(180)

    

    for i in range(a):
        turtle.penup()
        turtle.forward(int(scale))
        turtle.pendown()
        turtle.right(90)
        turtle.forward(height/2)
        turtle.backward(height)
        turtle.forward(height/2)
        turtle.left(90)

    turtle.penup()
    turtle.home()

    b=int((height/scale)/2)
    turtle.left(90)
    for i in range(b):
        turtle.penup()
        turtle.forward(int(scale))
        turtle.pendown()
        turtle.right(90)
        turtle.forward(width/2)
        turtle.backward(width)
        turtle.forward(width/2)
        turtle.left(90)

    turtle.penup()
    turtle.home()
    turtle.right(90)

    for i in range(b):
        turtle.penup()
        turtle.forward(int(scale))
        turtle.pendown()
        turtle.right(90)
        turtle.forward(width/2)
        turtle.backward(width)
        turtle.forward(width/2)
        turtle.left(90)

    #turtle.penup()
    turtle.home()
    turtle.hideturtle()
    turtle.bgcolor('Navy')
    turtle.color('white')
    turtle.pensize(3)
    turtle.left(90)
    turtle.forward(height/2)

    turtle.right(40)
    turtle.backward(20)
    turtle.forward(20)
    turtle.left(80)
    turtle.backward(20)
    turtle.forward(20)
    turtle.right(40)
    turtle.backward(50)
    turtle.penup()
    turtle.left(90)
    turtle.forward(15)
    turtle.write('Y')
    turtle.backward(15)
    turtle.right(90)
    turtle.forward(50)
    turtle.pendown()
    
    turtle.backward(height)
    turtle.forward(height/2)
    turtle.right(90)
    turtle.forward(width/2)

    turtle.backward(10)
    turtle.right(40)
    turtle.backward(20)
    turtle.forward(20)
    turtle.left(80)
    turtle.backward(20)
    turtle.forward(20)
    turtle.right(40)
    turtle.forward(10)

    turtle.backward(50)
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.write('X')
    turtle.backward(20)
    turtle.left(90)
    turtle.forward(60)
    turtle.pendown()
    
    turtle.backward(width)
    turtle.home()

    

    #legenda
    turtle.color('white')
    turtle.pensize(2)
    turtle.penup()
    turtle.right(90)
    turtle.forward(height/2-45)
    turtle.left(90)
    label_size = len(str(scale))*4.7 + scale / 2 + 48 + 60
    turtle.forward(width/2-label_size-scale)
    turtle.write('Escala =')
    turtle.forward(55)
    turtle.write(str(scale))
    turtle.forward(len(str(scale))*6)
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
    turtle.penup()
    turtle.right(90)
    turtle.forward(turtle.window_height() / 2 - 60)
    turtle.right(90)
    turtle.forward(turtle.window_width() / 2 - 40)
    turtle.right(180)
    turtle.write('para aumetar a escala use tecla com seta para baixo')
    turtle.right(90)
    turtle.forward(15)
    turtle.write('para reduzir a escala use tecla com seta para cima')
    turtle.home()
    turtle.pendown()
    turtle.update()

    


def grafic(coordinates,scale):
##    turtle.shape('triangle')
##    turtle.showturtle()
    turtle.penup()
    turtle.pensize(3)
    turtle.color('red')
    turtle.setpos(coordinates[0],coordinates[1])
    x=int(len(coordinates)/2)
    turtle.pendown()
    cont=0
    
    for i in range(x):
        turtle.setpos(coordinates[cont],coordinates[cont+1])
        cont += 2
    turtle.home()
    


def draw(raw_coordinates, scale):
    coordinates = [scale*coordinates for coordinates in raw_coordinates]
    background(scale)
    grafic(coordinates, scale)



