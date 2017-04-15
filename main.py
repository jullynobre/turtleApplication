import turtle
import helper


def x_generator():
    num_x = turtle.window_width()/2
    a = (num_x/2)*(-1)
    x = []
    for i in range(int(num_x)):
        x.append(a)
        a += 1
    return x


def y_generator(x, func):
    y = []
    for i in range(len(x)):
        y.append(helper.get_y(func, x[i]))
    return y


def som_xy(x, y):
    raw_coordinates = []
    for i in range(len(x)):
        raw_coordinates.append(x[i])
        raw_coordinates.append(y[i])


def method():
    scn = turtle.Screen()
    text = scn.textinput("Teste", "Teste Teste")
    x = x_generator()
    y = y_generator(x, text)
    print(y)
method()
