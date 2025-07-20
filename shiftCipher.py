# Lab 1: Write a program to implement Shift Cipher. (Encryption/Decryption/ Input (key/plaint text for encryption/ cipher text for decryption) should be taken from user).

def encrypt(text, key): #text= message to encrypt, key=positions to shift each letter int
    result = ""
    for char in text:
        if char.isalpha(): # condition inside the loop to check the character is letter or not
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            # below if the character is uppercase, set the base =65 (ASCII)
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # leave non-letters unchanged
    return result

def decrypt(text, key):
    return encrypt(text, -key)  # decryption is reverse of encryption

def main():
    print("=== Shift Cipher ===")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode. Choose 'encrypt' or 'decrypt'.")
        return

    key_input = input("Enter key (shift value): ").strip()
    if not key_input.isdigit():
        print("Key must be a number.")
        return
    key = int(key_input)

    text = input("Enter the text: ")

    if mode == "encrypt":
        result = encrypt(text, key)
        print("Encrypted text:", result)
    else:
        result = decrypt(text, key)
        print("Decrypted text:", result)

if __name__ == "__main__":
    main()
 # make sure the main() function runs only if the file is run directly, not imported in another file