# Write a program to implement Playfair Cipher. (Encryption/Decryption/ Input should be taken from user, Display the key matrix as well).

import string

def generate_key_matrix(key):
    key = key.upper().replace("J", "I").replace(" ", "")
    seen = set()
    matrix = []

    for char in key + string.ascii_uppercase:
        if char not in seen and char != 'J':
            seen.add(char)
            matrix.append(char)
        if len(matrix) == 25:
            break

    # Convert flat list to 5x5 matrix
    key_matrix = [matrix[i*5:(i+1)*5] for i in range(5)]
    return key_matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None, None

def prepare_text(text, encrypting=True):
    text = text.upper().replace("J", "I").replace(" ", "")
    prepared = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = ''
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2
        else:
            b = 'X'
            i += 1
        prepared += a + b
    return prepared

def encrypt_pair(a, b, matrix):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:  # same row
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  # same column
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  # rectangle
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(a, b, matrix):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:  # same row
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  # same column
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:  # rectangle
        return matrix[row1][col2] + matrix[row2][col1]

def display_matrix(matrix):
    print("\nPlayfair Key Matrix:")
    for row in matrix:
        print(" ".join(row))
    print()

def main():
    print("=== Playfair Cipher ===")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode. Choose 'encrypt' or 'decrypt'.")
        return

    key = input("Enter the key: ")
    matrix = generate_key_matrix(key)
    display_matrix(matrix)

    text = input("Enter the text: ")

    prepared_text = prepare_text(text, encrypting=(mode == "encrypt"))

    result = ""
    for i in range(0, len(prepared_text), 2):
        a, b = prepared_text[i], prepared_text[i + 1]
        if mode == "encrypt":
            result += encrypt_pair(a, b, matrix)
        else:
            result += decrypt_pair(a, b, matrix)

    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()

# Replace "j" with 'i' (standard in playfair)
#  THE x IS added between repeated letters in parirs