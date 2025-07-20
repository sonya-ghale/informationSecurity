# Implement AES(Advanced Encryption Standard) Algorithm

#using cryptography library from python 

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def encrypt_aes(plaintext, key):
    # Generate a random 16-byte IV
    iv = os.urandom(16)

    # Pad plaintext to be multiple of block size (16 bytes)
    padder = padding.PKCS7(128).padder()
    padded_text = padder.update(plaintext.encode()) + padder.finalize()

    # Create AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(padded_text) + encryptor.finalize()
    return iv + ciphertext  # Prepend IV for use in decryption

def decrypt_aes(ciphertext, key):
    # Extract the IV from the beginning
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()

    # Unpad the plaintext
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode()

def main():
    key = os.urandom(32)  # AES-256 requires 32 bytes key
    print("Key (hex):", key.hex())

    plaintext = input("Enter plaintext: ")
    ciphertext = encrypt_aes(plaintext, key)
    print("Encrypted (hex):", ciphertext.hex())

    decrypted = decrypt_aes(ciphertext, key)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()

# pip install cryptography
# AES is widely used for symmetric encryption algorithm for protecting electronics data. uses the same key for both encryption and decryption. 