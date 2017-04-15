def get_y(func, x):
    func = clear_function(func)
    func = replace_x_with_operator(func, x)
    if func.find("(") < 0:
        func = replace_exponents(func)
        while has_operator(func):
            i_op = get_index_of_next_operator(func)
            n1 = get_left_number(func, i_op)
            n2 = get_right_number(func, i_op)
            op = func[i_op]
            result = calc(n1, n2, op)
            func = func.replace(str(n1)+op+str(n2), str(result))
    else:
        sub_func = func[func.find("(") + 1:func.find(")")]
        if not has_operator(func[func.find("(")-1]):
            sub_func = func.replace("("+sub_func+")", "*"+get_y(sub_func, x))
        else:
            sub_func = func.replace("("+sub_func+")", get_y(sub_func, x))
        return get_y(sub_func, x)
    return func


def clear_function(func):
    func = func.lower()
    func = func.replace(" ", "")
    return func


def has_operator(func):
    if (func.find("+") >= 0) or (func.find("-") > 0) or (func.find("*") >= 0) or (func.find("/") >= 0):
        return True
    return False


def get_index_of_next_operator(func):
    if func.find("(") < 0:
        sum = func.find("+")
        sub = func.find("-")
        mul = func.find("*")
        div = func.find("/")
        if (mul != -1) and ((mul < div) or (div == -1)):
            return mul
        elif div != -1:
            return div
        elif sum < sub and sum != -1:
            return sum
        else:
            return sub
    else:
        sub_func = func[func.find("(")+1:func.find(")")]
        return func.find("(") + 1 + get_index_of_next_operator(sub_func)


def get_left_number(func, i_next_op):
    if has_operator(func[0:i_next_op]):
        i = i_next_op - 1
        number = ""
        while not has_operator(func[i]):
            number = func[i] + number
            i -= 1
        return number
    else:
        return func[0:i_next_op]


def get_right_number(func, i_next_op):
    if has_operator(func[i_next_op+1:len(func)]):
        x = i_next_op+1
        number = ""
        number += func[x]
        x += 1
        while x < len(func) and not has_operator(func[x]):
            number += func[x]
            x += 1
        return number
    else:
        return func[i_next_op+1:len(func)]


def calc(n1, n2, op):
    if op == "+":
        return float(n1) + float(n2)
    elif op == "-":
        return float(n1) - float(n2)
    elif op == "*":
        return float(n1) * float(n2)
    elif op == "/":
        return float(n1) / float(n2)


def replace_x_with_operator(func, x):
    while func.find("x") != -1:
        index = func.find("x")
        if index == 0:
            func = str(x) + func[1:len(func)]
        elif has_operator(func[index-1]) or (func[index-1] == "("):
            func = func[0:index] + str(x) + func[index+1:len(func)]
        else:
            func = func[0:index] + "*" + str(x) + func[index+1:len(func)]
    return func


def replace_exponents(func):
    while func.find("²") >= 0:
        index = func.find("²")
        func = func[0:index] + "*" + str(get_left_number(func, index)) + func[index+1:len(func)]
    while func.find("³") >= 0:
        index = func.find("³")
        new = float(get_left_number(func, index)) * float(get_left_number(func, index))
        func = func[0:index] + "*" + str(new) + func[index + 1:len(func)]
    return func

