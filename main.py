import turtle
import helper
import draw


def x_generator():
    num_x=turtle.window_width()/2
    a=(num_x/2)*(-1)
    x=[]
    for i in range(int(num_x)):
        x.append(a)
        a+=1
    return x


def y_generator(x,func):
    y=[]
    for i in range(len(x)):
        y.append(get_y(func, x[i]))
    return y


def som_xy(x,y):
    raw_coordinates=[]
    for i in range(len(x)):
        raw_coordinates.append(x[i])
        raw_coordinates.append(y[i])


def main():
    scn = turtle.Screen()
    text = scn.textinput("Teste", "Teste Teste")
    print(helper.get_y(text, 2))
main()
