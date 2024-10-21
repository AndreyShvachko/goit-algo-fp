import turtle
import math

#Функція для створення дерева Піфагора з заданою довжиною гілки, кутом та рівнем рекурсії
def draw_pythagoras_tree(branch_len, level):
    if level == 0:
        return

    turtle.forward(branch_len)
    turtle.left(45)
    draw_pythagoras_tree(branch_len * math.sqrt(2) / 2, level -1)
    turtle.right(90)
    draw_pythagoras_tree(branch_len * math.sqrt(2) / 2, level -1)
    turtle.left(45)
    turtle.backward(branch_len)

#Налаштування середовища для малювання дерева Піфагора
def setup_pythagoras_tree(level):
    turtle.speed('fastest')
    turtle.left(90)
    turtle.up()
    turtle.goto(0, -200)
    turtle.down()

    branch_len = 100
    

    draw_pythagoras_tree(branch_len, level)

    turtle.done()

if __name__ == "__main__":
    recursion_level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
    setup_pythagoras_tree(recursion_level)


