def extended_euclidean(a, b):
    print(f"{'Step':<6}{'r1':<8}{'r2':<8}{'q':<6}{'t1':<8}{'t2':<8}")
    print("-" * 50)

    r1, r2 = a, b
    t1, t2 = 1, 0
    s1, s2 = 0, 1
    step = 1

    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        t = t1 - q * t2
        s = s1 - q * s2

        print(f"{step:<6}{r1:<8}{r2:<8}{q:<6}{t1:<8}{t2:<8}")

        r1, r2 = r2, r
        t1, t2 = t2, t
        s1, s2 = s2, s
        step += 1

    print(f"{step:<6}{r1:<8}{r2:<8}{'':<6}{t1:<8}{t2:<8}")
    print("\nGCD:", r1)
    print(f"Coefficients: x = {s1}, y = {t1}")
    print(f"Result: {a}*({s1}) + {b}*({t1}) = {r1}")

def main():
    print("=== Extended Euclidean Algorithm ===")
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    print()
    extended_euclidean(a, b)

if __name__ == "__main__":
    main()


# value of a= 99, b=78