# Building a calculator.
from art import logo
from replit import clear


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    num1 = float(input("What's the first number: "))
    symbol_group = ""
    for symbol in operations:
        symbol_group += symbol + " "
    print(symbol_group)
    end_of_calculator = False

    while not end_of_calculator:
        operation_symbol = input("Pick an operation:  ")
        num2 = float(input("What's the next number:  "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        to_continue = input(
            "Type y if you want to continue with the result or type n if you want to start new calculator "
        ).lower()
        if to_continue == "y":
            num1 = answer
        elif to_continue == "n":
            clear()
            calculator()


# Calling out the calculator() for the start of the program
calculator()
