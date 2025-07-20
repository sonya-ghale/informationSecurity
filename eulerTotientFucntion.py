# that tajes any positive number and display the result after computing the totient function

def gcd(a, b):
    while b:
        a,b =b, a % b
    return a

def totient(n):
    count = 0
    for i in range(1, n+1):
        if gcd(i, n) == 1:
            count += 1
    return count

def main():
    print("Euler's totient function")
    try:
        num = int(input("Enter a positive integer:"))
        if num <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a positive integer")
        return
    
    result = totient(num)
    print(f"Totient value φ({num}) = {result}")

if __name__ == "__main__":
    main()