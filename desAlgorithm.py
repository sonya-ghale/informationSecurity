# Crypto graphy doesn't support DES(Data encryption standard), symmetric-key block cipher that encrypts 64-bit blocks of data using a 56-bit key.

# pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

# DES key must be 8 bytes long
def get_key():
    key = input("Enter 8-character key: ")
    while len(key) != 8:
        key = input("Key must be exactly 8 characters. Try again: ")
    return key.encode()

def encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode(), DES.block_size)
    encrypted = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted).decode()

def decrypt(cipher_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(cipher_text))
    return unpad(decrypted, DES.block_size).decode()

def main():
    print("=== DES Encryption/Decryption ===")
    choice = input("Do you want to (encrypt/decrypt)? ").strip().lower()

    key = get_key()

    if choice == "encrypt":
        text = input("Enter plaintext: ")
        encrypted = encrypt(text, key)
        print("Encrypted text:", encrypted)

    elif choice == "decrypt":
        text = input("Enter encrypted text (base64): ")
        try:
            decrypted = decrypt(text, key)
            print("Decrypted text:", decrypted)
        except ValueError:
            print("Decryption failed. Possibly wrong key or corrupted data.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
