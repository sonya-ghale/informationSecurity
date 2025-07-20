def euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    print("=== Euclidean Algorithm to Find GCD ===")
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    gcd = euclidean_gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {gcd}")

if __name__ == "__main__":
    main()


#  Euclidean algorithm is a method for efficiently finding the greatest common divisor (GCD) of two integers