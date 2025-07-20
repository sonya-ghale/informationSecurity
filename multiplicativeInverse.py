 #Multiplicative inverse in given modulo n using extended eunclidean algorithm

def extended_gcd(a, b):
    """
    Returns: (gcd, x, y) where a*x + b*y = gcd
    """
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (gcd, x, y)

def multiplicative_inverse(a, n):
    gcd, x, y = extended_gcd(a, n)
    if gcd != 1:
        print(f"No multiplicative inverse exists for {a} modulo {n}.")
    else:
        inverse = x % n
        print(f"The multiplicative inverse of {a} modulo {n} is: {inverse}")

def main():
    print("=== Multiplicative Inverse using Extended Euclidean Algorithm ===")
    a = int(input("Enter value of a: "))
    n = int(input("Enter modulo n: "))
    multiplicative_inverse(a, n)

if __name__ == "__main__":
    main()
