func=('100+200+300')

def has_operator(func):
    if (func.find("+") >= 0) or (func.find("-") >= 0) or (func.find("*") >= 0) or (func.find("/") >= 0):
        return True
    return False

def get_left_number(func, i_next_op):
    if has_operator(func[i_next_op:len(func)]):
        x=i_next_op+1
        while not has_operator(x):
            x+=1
        x-=1
        print(func[i_next_op:x])
    else:
        print(func[i_next_op:len(func)]




get_left_number('100+200+300',8)
