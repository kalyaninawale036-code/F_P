def convert_and_display_bases():
    """
    Inputs a number from the user and displays its hexadecimal and binary formats.
    """
    try:
        num = int(input("Enter an integer: "))

        hex_num = hex(num)
        bin_num = bin(num)

        print(f"The number in hexadecimal format is: {hex_num}")
        print(f"The number in binary format is: {bin_num}")

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    convert_and_display_bases()