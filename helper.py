def get_function_type(func):
    clear_function(func)
    return 1


def clear_function(func):
    func = func.lower()
    func = func.replace(" ", "")
    print(func)


def get_y(func, x):
    func = func.replace("x", "*" + x)
    while has_operator(func):
        i_op = get_index_of_next_operator(func)
        n1 = get_left_number(func, i_op)
        n2 = get_right_number(func, i_op)
        op = func[i_op]
        result = calc(n1, n2, op)
        func = func.replace(n1 + n2, result)
    return func


def has_operator(func):
    if (func.find("+") < 0) or (func.find("-") < 0) or (func.find("*") < 0) or (func.find("/") < 0):
        return True
    return False


def get_index_of_next_operator(func):
    return 1


def get_left_number(func, i_next_op):
    return 1


def get_right_number(func, i_next_op):
    return 1


def calc(n1, n2, op):
    if op == "+":
        return float(n1) + float(n2)
    elif op == "-":
        return float(n1) - float(n2)
    elif op == "*":
        return float(n1) * float(n2)
    elif op == "/":
        return float(n1) / float(n2)
