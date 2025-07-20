# rsa algorithm 

from math import gcd

# Function to compute modular inverse using Extended Euclidean Algorithm
def mod_inverse(e, phi):
    old_r, r = e, phi
    old_s, s = 1, 0
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    if old_r != 1:
        return None  # Inverse doesn't exist
    else:
        return old_s % phi

# Function to compute power mod (base^exp % mod)
def power_mod(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Function to generate RSA keys
def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = 3
    while gcd(e, phi) != 1:
        e += 2

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))  # (public_key, private_key)

# Function to encrypt a message
def encrypt(msg, public_key):
    e, n = public_key
    cipher = [power_mod(ord(char), e, n) for char in msg]
    return cipher

# Function to decrypt a cipher
def decrypt(cipher, private_key):
    d, n = private_key
    plain = ''.join([chr(power_mod(char, d, n)) for char in cipher])
    return plain

# Main function
def main():
    print("=== RSA Encryption / Decryption ===")
    p = int(input("Enter first prime number (p): "))
    q = int(input("Enter second prime number (q): "))

    public_key, private_key = generate_keys(p, q)

    print(f"Public Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")

    msg = input("Enter message to encrypt: ")
    cipher = encrypt(msg, public_key)

    print(f"Encrypted message (as integers): {cipher}")

    decrypted = decrypt(cipher, private_key)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
