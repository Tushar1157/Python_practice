"""Write a python code to take two inputs from user and performing division operation.
Handle ValueError and ZeroDivisionError exceptions."""
def input_numbers():

    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    return a, b


x, y = input_numbers()


try:
    print(f"{x} / {y} is {x/y}")

except ZeroDivisionError:

    print("Cannot divide by zero")
    x, y = input_numbers()