# S-box (s1) generated in DES

def get_sbox_output(input_bits):
    # S1 S-Box from DES standard
    S1 = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ]

    # Ensure input is 6 bits
    if len(input_bits) != 6 or not all(bit in '01' for bit in input_bits):
        raise ValueError("Input must be a 6-bit binary string.")

    # Calculate row and column
    row = int(input_bits[0] + input_bits[5], 2)
    col = int(input_bits[1:5], 2)

    # Get value from S1
    s1_value = S1[row][col]

    # Convert to 4-bit binary string
    return format(s1_value, '04b')

def main():
    print("=== S-Box (S1) Output Demo ===")
    input_bits = input("Enter 6-bit binary input (e.g., 011011): ").strip()

    try:
        output = get_sbox_output(input_bits)
        print(f"S1 Output for {input_bits} is: {output}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

