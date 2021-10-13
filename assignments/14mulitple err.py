
def input_numbers():

    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    return a, b


x, y = input_numbers()


try:
    print(f"{x} / {y} is {x/y}")
    val =input_numbers()
    print(f"Your age is {val}")

except ZeroDivisionError:

    print("Cannot divide by zero")
    x, y = input_numbers()
except ( ValueError) as e:
    print("Insterted value is not in  int fromat")
    x, y = input_numbers()
    print(e)