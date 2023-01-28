from tkinter import *


def button_click(num):
    global expression
    if num in ["+", "-", "/", "*", "."] and len(expression) == 0:
        pass
    elif len(expression) != 0 and num in ["+", "-", "/", "*", "."] and expression[-1] in ["+", "-", "/", "*", "."]:
        pass
    elif "." in expression and num == ".":
        pass
    elif num == "=":
        expression = str(eval(expression))
        equation.set(expression)
    elif num == "C":
        expression = ""
        equation.set(expression)
    else:
        expression = expression + str(num)
        equation.set(expression)


window = Tk()

window.geometry("195x300")
window.resizable(False, False)
window.config(bg="#3B3B3B")

expression = ""
equation = StringVar()
box = Label(window, bg="white", textvariable=equation, anchor="w", height=2, width=40)
box.grid(row=0, column=0, columnspan=30, sticky="W")

button_1 = Button(window, text="1", height=2, width=4, command=lambda: button_click(1), relief="flat", padx=5, pady=5)
button_1.grid(row=4, column=0)

button_2 = Button(window, text="2", height=2, width=4, command=lambda: button_click(2), relief="flat", padx=5, pady=5)
button_2.grid(row=4, column=1)

button_3 = Button(window, text="3", height=2, width=4, command=lambda: button_click(3), relief="flat", padx=5, pady=5)
button_3.grid(row=4, column=2)

button_4 = Button(window, text="4", height=2, width=4, command=lambda: button_click(4), relief="flat", padx=5, pady=5)
button_4.grid(row=3, column=0)

button_5 = Button(window, text="5", height=2, width=4, command=lambda: button_click(5), relief="flat", padx=5, pady=5)
button_5.grid(row=3, column=1)

button_6 = Button(window, text="6", height=2, width=4, command=lambda: button_click(6), relief="flat", padx=5, pady=5)
button_6.grid(row=3, column=2)

button_7 = Button(window, text="7", height=2, width=4, command=lambda: button_click(7), relief="flat", padx=5, pady=5)
button_7.grid(row=2, column=0)

button_8 = Button(window, text="8", height=2, width=4, command=lambda: button_click(8), relief="flat", padx=5, pady=5)
button_8.grid(row=2, column=1)

button_9 = Button(window, text="9", height=2, width=4, command=lambda: button_click(9), relief="flat", padx=5, pady=5)
button_9.grid(row=2, column=2)

button_0 = Button(window, text="0", height=2, width=4, command=lambda: button_click(0), relief="flat", padx=5, pady=5)
button_0.grid(row=5, column=0)

button_dot = Button(window, text=".", height=2, width=4, command=lambda: button_click("."), relief="flat", padx=5, pady=5)
button_dot.grid(row=5, column=1)

button_equals = Button(window, text="=", height=2, width=4, command=lambda: button_click("="), relief="flat", padx=5, pady=5)
button_equals.grid(row=5, column=2)

button_plus = Button(window, text="+", height=2, width=4, command=lambda: button_click("+"), relief="flat", padx=5, pady=5)
button_plus.grid(row=5, column=3)

button_minus = Button(window, text="-", height=2, width=4, command=lambda: button_click("-"), relief="flat", padx=5, pady=5)
button_minus.grid(row=4, column=3)

button_multiply = Button(window, text="*", height=2, width=4, command=lambda: button_click("*"), relief="flat", padx=5, pady=5)
button_multiply.grid(row=3, column=3)

button_divide = Button(window, text="/", height=2, width=4, command=lambda: button_click("/"), relief="flat", padx=5, pady=5)
button_divide.grid(row=2, column=3)

button_clear = Button(window, text="C", height=2, width=4, command=lambda: button_click("C"), relief="flat", padx=5, pady=5)
button_clear.grid(row=1, column=3)

window.mainloop()
