# Malicous logic code (Tojan horse) program that performs some malicious work 
# "Trojan" logs something secretly
def harmless_trojan(operation, num1, num2, result):
    with open("trojan_data.txt", "a") as file:
        file.write("I am a harmless trojan! \n")
        file.write("I am Hidden \n")
        file.write(f"User did: {num1} {operation} {num2} = {result}\n")

# Start the program
print("Simple Calculator")

# Get user inputs
try:
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Perform calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Cannot divide by zero.")
            result = None
        else:
            result = num1 / num2
    else:
        print("Invalid operation.")
        result = None

    # Show and log result
    if result is not None:
        print(f"Result: {result}")
        harmless_trojan(operation, num1, num2, result)

except ValueError:
    print("Please enter valid numbers.")


