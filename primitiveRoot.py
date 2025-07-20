# Compute primitive roots of given number

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def power_mod(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return result

def find_prime_factors(n):
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors

def is_primitive_root(g, p, phi, prime_factors):
    for factor in prime_factors:
        # Check if g^(phi/factor) ≡ 1 mod p
        if power_mod(g, phi // factor, p) == 1:
            return False
    return True

def primitive_roots(p):
    if p == 2:
        return [1]  # special case

    phi = p - 1
    prime_factors = find_prime_factors(phi)

    roots = []
    for g in range(2, p):
        if is_primitive_root(g, p, phi, prime_factors):
            roots.append(g)
    return roots

def main():
    print("=== Compute Primitive Roots modulo p (p prime) ===")
    p = int(input("Enter a prime number p: "))
    
    # Simple primality check
    if p < 2:
        print("p must be a prime greater than 1.")
        return
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            print("Number is not prime. Primitive roots may not exist.")
            return

    roots = primitive_roots(p)
    print(f"Primitive roots modulo {p} are:\n{roots}")

if __name__ == "__main__":
    main()
