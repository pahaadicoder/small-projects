logo='''_______________________
|  _________________  |
| |                 | |
| |                 | |
| |                 | |
| |                 | |
| |                 | |
| |_________________| |
|  _________________  |
| |  1  |  2  |  3  | |
| |_____|_____|_____| |
| |  4  |  5  |  6  | |
| |_____|_____|_____| |
| |  7  |  8  |  9  | |
| |_____|_____|_____| |
| |  0  |  +  |  -  | |
| |_____|_____|_____| |
| |  *  |  /  |  =  | |
| |_____|_____|_____| |
|_____________________|

'''




def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2
    
def subtract(n1, n2):
    return n2 - n1

def divide(n1, n2):
    return n1 / n2


dictionary = {"+": add, "*": multiply, "-": subtract, "/": divide}

total = 0
while True:
    print(logo)
    num1 = int(input("What's the first number? "))
    num2 = int(input("What's the second number? "))

    for symbol in dictionary:
        print(symbol)
    
    operation_symbol = input("Pick an operation from the line above: ")

    calculation_function = dictionary[operation_symbol]
    answer = calculation_function(num1, num2)
    total += answer

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    ask = input("Do you want to perform another calculation? Enter 'yes' or 'no': ")
    if ask == 'no':
        break

print("Final output: The total of all calculations is", total)
