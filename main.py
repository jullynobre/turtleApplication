import turtle
import helper


def main():
    scn = turtle.Screen()
    text = scn.textinput("Teste", "Teste Teste")
#   type_f = helper.get_function_type(text)
    print(helper.replace_x_with_operator(text, 2))

main()
