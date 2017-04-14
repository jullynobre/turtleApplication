import turtle
import helper


def main():
    scn = turtle.Screen()
    text = scn.textinput("Teste", "Teste Teste")
    print(helper.get_index_of_next_operator(text))
main()
