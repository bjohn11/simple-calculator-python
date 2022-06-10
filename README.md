# Simple Calculator

## Story

Your task is to implement a simple calculator script that asks the user
to enter a number, then an operation (like `+` and `/`), then a
number again. After the second number input, the result of the
operation is calculated and printed out. After that, the program
asks again for a first number.

The script exits when the user enters a non-numeric
expression (such as a letter) _for the first number_ input.

## What are you going to learn?

- more advanced conditional statements
- type conversion
- basic exception handling

## Tasks

1. Implement `is_number(str)` function, which checks whether given string can be converted into a numeric value.
    - If the given string contains a valid number, the function returns `True`.
    - If the given string contains an invalid value, the function returns `False`.
    - The function works for non-negative integers, like `5` or `1000`.
    - The function works for negative integers, like `-5` and `-1000`.
    - The function works for any real numbers, like `5.25` or `-1000.14`

2. Implement `convert_number(str)` function, which converts given string into a numeric value.
    - The function returns the coverted numeric value from given string.
    - The function works for non-negative integers, like `5` or `1000`.
    - The function works for negative integers, like `-5` and `-1000`.
    - The function works for any real numbers, like `5.25` or `-1000.14`

3. Implement `ask_for_a_number(force_valid_input)` to return the numeric value of the user input. The function continuously asks for input from the user until the input is numeric when `force_valid_input` is `True`. When the `force_valid_input` is `False` and the user input is not numeric, the function returns with `None`.
    - The function asks for input from the user, e.g.&#58; 'Please provide a number! '.
    - The function returns the numeric value of the input string if it represents a valid number.
    - The function returns `None` when the user input does not represent any number and `force_valid_input` is `False`.
    - If `force_valid_input` is `True`, the function continuously asks for a number, until the input string represents a valid number. After an unsuccessful input, the program informs the user about the wrong input, e.g.&#58; 'This didn't look like a number, try again.'.

4. Implement an `is_valid_operator(operator)` to return `True` if the `operator` input parameter represents a valid operator, and otherwise return `False`.
    - Valid operators are the following&#58; +, -, *, /.

5. Implement an `ask_for_an_operator(force_valid_input)` to return a valid operator. The function continuously asks the user for an operator until the input is valid when `force_valid_input` is `True`. When `force_valid_input` is `False` and the user input is not a valid operator, the function returns `None`.
    - The function asks the user for input, e.g.&#58; 'Please provide an operator (one of +, -, *, /)! '.
    - The function returns an operator if the input string represents a valid operator.
    - The function returns `None` when the user input does not represent a valid operator and `force_valid_input` is `False`.
    - If `force_valid_input` is `True`, the function continuously asks for an operator until the input string represents a valid operator. After an unsuccessful input, the program informs the user about the wrong input, e.g.&#58; 'Unknown operator.'.

6. Implement a `calc(operator, a, b)` to calculate the result of the 'a' 'operator' 'b' operator. The function returns `None` if any operand or the operator is not valid. The function handles division by zero, in this case the returned value is `None`
    - The function checks the validity of the operands and the operator. Returns `None` in case of invalid input.
    - The function returns the result of 'a' + 'b' if the operator is '+'.
    - The function returns the result of 'a' - 'b' if the operator is '-'.
    - The function returns the result of 'a' \* 'b' if the operator is '\*'.
    - The function returns the result of 'a' / 'b' if the operator is '/' and b is not equal to 0. If 'b' is equal to 0, the function prints an error message, e.g.&#58; 'Error&#58; Division by zero' and returns `None`.

7. Implement `simple_calculator()` to create the calculator. The function continuously asks for number 'a' and 'b' and an operator and calculates the result of 'a' 'operator' 'b'.
    - The function checks the validity of the operands and the operator. Exit from the program if the 'a' operand is not valid. If 'a' operand is valid, the function ensures that operand 'b' and the operator are valid.
    - The function prints the calculation results, e.g.&#58; 'The result is 10'.

## General requirements

None

## Hints

- You need a function that asks for input numbers from the user.
For the first number request, non-number input is acceptable (this triggers
the exit from the program), but for the second input request, it is not allowed.
You can distinguish between the two cases with a boolean variable.


## Background materials

- <i class="far fa-exclamation"></i> [Control structures]
- <i class="far fa-exclamation"></i> [Error handling and exceptions]
- <i class="far fa-exclamation"></i> [Top-level script environment](https://docs.python.org/3/library/__main__.html)
- <i class="far fa-candy-cane"></i> [Conditional Statements in Python](https://realpython.com/python-conditional-statements/)
- <i class="far fa-candy-cane"></i> [Python "while" Loops](https://realpython.com/python-while-loop/)
- <i class="far fa-candy-cane"></i> [Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)


