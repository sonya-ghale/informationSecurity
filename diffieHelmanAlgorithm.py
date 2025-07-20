# Diffie -Helman key exchange algorithm

def power_mod(base, exponent, modulus):
    """Efficient modular exponentiation"""
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

def diffie_hellman(p, g, a, b):
    # Public keys
    A = power_mod(g, a, p)
    B = power_mod(g, b, p)

    print(f"Soniya public key (A): {A}")
    print(f"Mingma public key (B): {B}")

    # Shared secret keys
    shared_key_soniya = power_mod(B, a, p)
    shared_key_mingma = power_mod(A, b, p)

    return shared_key_soniya, shared_key_mingma

def main():
    print("=== Diffie-Hellman Key Exchange ===")
    
    # Inputs
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a primitive root modulo p (g): "))
    
    a = int(input("Enter Soniya private key (a): "))
    b = int(input("Enter Mingma private key (b): "))

    shared_a, shared_b = diffie_hellman(p, g, a, b)

    print(f"\nShared secret computed by Soniya: {shared_a}")
    print(f"Shared secret computed by Mingma:   {shared_b}")

    if shared_a == shared_b:
        print("Key exchange successful! Shared keys match.")
    else:
        print("Key exchange failed! Shared keys do not match.")

if __name__ == "__main__":
    main()
