import turtle
import helper


def main():
    scn = turtle.Screen()
    text = scn.textinput("Teste", "Teste Teste")
    type_f = helper.get_function_type(text)
    print(type_f)

main()
