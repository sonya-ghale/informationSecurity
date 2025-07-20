# Write a program to implement Robin Miller algorithm for primality test.

# is a probabolistic algorithm used to dtermine if a given number is likeyly prime. Based on the properties of modular arithmetic and fermat's little theorem.

import random

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Run k trials
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue  # go to next trial

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # definitely composite

    return True  # probably prime

def main():
    print("=== Rabin-Miller Primality Test ===")
    num = int(input("Enter a number to test: "))
    if is_prime(num):
        print(f"{num} is probably prime.")
    else:
        print(f"{num} is composite.")

if __name__ == "__main__":
    main()
