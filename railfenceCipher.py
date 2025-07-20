#: Write a program to implement Rail Fence Cipher. (Encryption/Decryption/ Input should be taken from user).

def encrypt_rail_fence(text, key):
    rail = ['' for _ in range(key)]
    direction_down = False
    row = 0

    for char in text:
        rail[row] += char
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1

    return ''.join(rail)

def decrypt_rail_fence(cipher, key):
    # Create a matrix to mark the pattern
    pattern = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    direction_down = None
    row, col = 0, 0

    # Mark positions with '*'
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        pattern[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    # Fill the matrix with the cipher text
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if pattern[i][j] == '*' and index < len(cipher):
                pattern[i][j] = cipher[index]
                index += 1

    # Read the matrix in zigzag to decrypt
    result = ''
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        result += pattern[row][col]
        col += 1
        row += 1 if direction_down else -1

    return result

def main():
    print("=== Rail Fence Cipher ===")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode. Choose 'encrypt' or 'decrypt'.")
        return

    key_input = input("Enter the key (number of rails): ").strip()
    if not key_input.isdigit() or int(key_input) < 2:
        print("Key must be a number greater than 1.")
        return
    key = int(key_input)

    text = input("Enter the text: ").replace(" ", "")

    if mode == "encrypt":
        result = encrypt_rail_fence(text, key)
        print("\nEncrypted text:", result)
    else:
        result = decrypt_rail_fence(text, key)
        print("\nDecrypted text:", result)

if __name__ == "__main__":
    main()
