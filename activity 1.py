def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

try:
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")

    choice = int(input("Choose (1-4): "))

    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))

    if choice == 1:
        print("Answer:", add(a,b))
    elif choice == 2:
        print("Answer:", subtract(a,b))
    elif choice == 3:
        print("Answer:", multiply(a,b))
    elif choice == 4:
        print("Answer:", divide(a,b))
    else:
        print("Invalid Choice!!")

except ValueError:
    print("Please enter numbers only!")

except ZeroDivisionError:
    print("Cannot divide by zero!")