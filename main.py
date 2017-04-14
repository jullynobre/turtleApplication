import turtle
import helper


def main():
    scn = turtle.Screen()
    text = scn.textinput("Teste", "Teste Teste")
    print(helper.get_y(text, 2))
main()
