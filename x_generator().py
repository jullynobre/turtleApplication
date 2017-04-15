import turtle
escala=10

def x_generator():
    num_x=turtle.window_width()/2
    a=(num_x/2)*(-1)
    x=[]
    for i in range(int(num_x)):
        x.append(a)
        a+=1
    return x
    

