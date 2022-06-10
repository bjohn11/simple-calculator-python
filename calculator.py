from os import truncate


def is_number(str):
    pass
    try:
        float(str)
        return True
    except ValueError:
        return False


def convert_number(str):
    pass
    return int(str)


def is_valid_operator(operator):
    pass
    Operators = ("+", "-", "/", "*")
    return operator in Operators


def ask_for_a_number(force_valid_input):
    pass
    while True:
        user_number = input("Please, enter a number! ")
        if is_number(user_number):
            return float(user_number)
        else:
            if not force_valid_input:
                return None
            print("This is not a number")


def ask_for_an_operator(force_valid_input):
    pass
    while True:
        operation = input("Please, enter an operator '+ ', '-', ' /', ' * ' ")
        if is_valid_operator(operation):
            return operation
        else:
            if not force_valid_input:
                return None
            print("Operator unknown")


def calc(operator, a, b):
    pass
    if not is_valid_operator(operator) or not is_number(a) or not is_number(b):
        return None
    result = None
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '/':
        if b != 0:
            result = a/b
    elif operator == '*':
        result = a*b
    return result


def simple_calculator():
    pass
    while True:
        a = ask_for_a_number(force_valid_input=False)
        if not a:
            break
        op = ask_for_an_operator(force_valid_input=True)
        b = ask_for_a_number(force_valid_input=True)
        result = calc(op, a, b)
        if result:
            print(f'result is {op, a, b}')




if __name__ == "__main__":
    simple_calculator()
