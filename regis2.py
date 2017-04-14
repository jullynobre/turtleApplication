func=('100+200+300')

def has_operator(func):
    if (func.find("+") >= 0) or (func.find("-") >= 0) or (func.find("*") >= 0) or (func.find("/") >= 0):
        return True
    return False

def get_left_number(func, i_next_op):
    if has_operator(func[i_next_op:len(func)]):
        i = i_next_op - 1
        number = "";
        while not has_operator(func[i]):
            number = func[i] + number
            i -= 1
        return number
    else:
        print(func[i_next_op:len(func)])
get_left_number('100+200+300',8)
