# Write a program that computes additive inverse in given modulo n.

def additive_inverse(a, n):
    return (n - a) % n

def main():
    print("=== Additive Inverse in Modulo n ===")
    try:
        a = int(input("Enter a number (a): "))
        n = int(input("Enter modulo (n): "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    inverse = additive_inverse(a, n)
    print(f"The additive inverse of {a} modulo {n} is: {inverse}")
    print(f"Check: ({a} + {inverse}) % {n} = {(a + inverse) % n}")

if __name__ == "__main__":
    main()


# the number that, when added to the original number, results in zero 7, 10 check