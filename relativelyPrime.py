import math

def are_relatively_prime(a, b):
    return math.gcd(a, b) == 1

def main():
    print("Check relatively prime Number")
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Please enter valid integers")
        return
    
    if are_relatively_prime(num1, num2):
        print(f"{num1} and {num2} are relatively prime.")
    else: 
        print(f"{num1} and {num2} are not relatively prime.")

if __name__ == "__main__":
    main()

# math = bult in fucntion provides mathematical functions, and math.gcd returns the greatest common divisor divisor 
# cause if 2 number have no common positive divisor except 1, and gcd is 1, and gcd tells the largest number and if GCD(a, b) == 1 means no number other than 1 divides both a and b
