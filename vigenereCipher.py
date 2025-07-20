#Write a program to implement Vigenere Cipher. (Encryption/Decryption/ Input should be taken from user)

def format_text(text):
    return text.upper().replace(" ", "").replace("J", "I")

def generate_full_key(text, key):
    key = key.upper().replace(" ", "")
    key_length = len(key)
    full_key = ''
    for i in range(len(text)):
        full_key += key[i % key_length]
    return full_key

def encrypt_vigenere(plaintext, key):
    plaintext = format_text(plaintext)
    key = generate_full_key(plaintext, key)
    cipher = ''

    for p, k in zip(plaintext, key):
        if p.isalpha():
            encrypted_char = chr(((ord(p) - 65 + ord(k) - 65) % 26) + 65)
            cipher += encrypted_char
        else:
            cipher += p
    return cipher

def decrypt_vigenere(ciphertext, key):
    ciphertext = format_text(ciphertext)
    key = generate_full_key(ciphertext, key)
    plain = ''

    for c, k in zip(ciphertext, key):
        if c.isalpha():
            decrypted_char = chr(((ord(c) - ord(k) + 26) % 26) + 65)
            plain += decrypted_char
        else:
            plain += c
    return plain

def main():
    print("=== Vigenère Cipher ===")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode. Choose 'encrypt' or 'decrypt'.")
        return

    key = input("Enter the key: ")
    text = input("Enter the text: ")

    if mode == "encrypt":
        result = encrypt_vigenere(text, key)
        print("\nEncrypted text:", result)
    else:
        result = decrypt_vigenere(text, key)
        print("\nDecrypted text:", result)

if __name__ == "__main__":
    main()
