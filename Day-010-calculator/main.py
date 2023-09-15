from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2
    
def subtract(n1, n2):
    return n1 - n2
    
def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What\'s the first number?: "))
    for op in operations:
        print(op)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        new_num = float(input("what is the next number?: "))
        answer = operations[operation_symbol](num1, new_num)
        print(f"{num1} {operation_symbol} {new_num} = {answer}")
        num1 = answer
        a = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if a == "n":
            calculator()
            
calculator()