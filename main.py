import turtle
import helper


def main():
    scn = turtle.Screen()
    text = scn.textinput("Teste", "Teste Teste")
    text = helper.clear_function(text)
    x = x_generator()
    y = y_generator(text, x)
    print(y)


def x_generator():
    num_x = turtle.window_width()/2
    a = (num_x/2)*(-1)
    x = []
    for i in range(int(num_x)):
        x.append(a)
        a += 1
    return x


def y_generator(func, x):
    y = []
    for i in range(len(x)):
        y.append(helper.get_y(func, x[i]))
    return y
main()
