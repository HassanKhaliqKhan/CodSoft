def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation choices
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get user's choice for operation
choice = input("Enter choice (1, 2, 3, or 4): ")

# Perform the selected operation
if choice in ('1', '2', '3', '4'):
    if choice == '1':
        result = add(num1, num2)
        operation = "Addition"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "Multiplication"
    else:
        result = divide(num1, num2)
        operation = "Division"

    # Display the result
    print(f"{operation} result: {result}")
else:
    print("Invalid choice. Please enter a valid operation (1, 2, 3, or 4).")
