import turtle
import helper
import draw
import ctypes

scale = 10
raw_coordinates = []


def x_generator():
    num_a = turtle.window_width() / 2
    num_x = turtle.window_width() / scale
    b = (num_x - 1) / (num_a - 1)
    a = (turtle.window_width() / (2 * scale)) * (-1)
    x = []
    for i in range(int(num_a)):
        x.append(a)
        a += b
    return x


def y_generator(x, func):
    y = []
    for i in range(len(x)):
        j = helper.get_y(func, x[i])
        y.append(float(j))
    return y


def som_xy(x, y):
    global raw_coordinates
    for i in range(len(x)):
        raw_coordinates.append(x[i])
        raw_coordinates.append(y[i])
    return raw_coordinates


def upscale():
    turtle.reset()
    global scale
    scale = scale * 1.2
    x = x_generator()
    y = y_generator(x, text)
    raw_coordinates = som_xy(x, y)
    draw.draw(raw_coordinates, scale)

def downscale():
    global scale
    if (scale * 0.8) >= 10:
        turtle.reset()
        scale = scale * 0.8
        x = x_generator()
        y = y_generator(x, text)
        raw_coordinates = som_xy(x, y)
        draw.draw(raw_coordinates, scale)


def main():
    scn = turtle.Screen()
    screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
    turtle.setup(screensize[0], screensize[1])
    turtle.title("Grafic Builder 1.0")
    global text
    text = scn.textinput("Grafic Builder 1.0", "Informe a função")
    x = x_generator()
    y = y_generator(x, text)
    global raw_coordinates
    raw_coordinates = som_xy(x, y)
    draw.draw(raw_coordinates, scale)


main()
turtle.onkey(upscale, 'Up')
turtle.onkey(downscale, 'Down')
turtle.listen()
turtle.exitonclick()
