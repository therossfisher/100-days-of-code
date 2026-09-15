import art
print(art.logo)


# define arithmetic as functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# put the functions into a dictionary
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# define the calculator as a function
def calculator(num1, num2, operation_symbol):
    result = operations[operation_symbol](num1, num2)
    return f"The result is: {result}"


should_accumulate = True

while True:
    try:
        num1 = float(input("Enter first number: \n"))   
        break
    except ValueError:
        print("Only numbers are allowed!")

# loop through the program so it can run again
while should_accumulate:

    # ask the user what operation they want to use
    operation_symbol = input("What operation would you like to try?\n"
                    "+ = add\n- = subtract\n* = multiply\n/ = divide\n")

    # validate user input for operation
    while operation_symbol not in ["+", "-", "*", "/"]:
        print("Please pick a valid operation")
        operation_symbol = input("What operation would you like to try?\n"
                    "+ = add\n- = subtract\n* = multiply\n/ = divide\n")

    # validate user input for numbers to do arithmetic on
    while True:
        try:               
            num2 = float(input("Enter second number: \n"))
            break
        except ValueError:
            print("Only numbers are allowed!")

    # run the function
    answer = operations[operation_symbol](num1, num2)

    # prints the final answer formatted with the operations symbols
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    # asks the user if they want to continue to calculate with the answer given
    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.\n")

    if choice == "y":
        num1 = answer
    else:
        should_accumulate = False
        print("\n" * 50)