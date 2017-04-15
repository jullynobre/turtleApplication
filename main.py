import turtle
import helper


def main():
    scn = turtle.Screen()
    text = scn.textinput("Teste", "Teste Teste")
    print(helper.get_y(text, 2))
main()


def x_generator():
    num_x=turtle.window_width()/2
    a=(num_x/2)*(-1)
    x=[]
    for i in range(int(num_x)):
        x.append(a)
        a+=1
    return x
    
