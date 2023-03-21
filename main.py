# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def printHexDualOct(inputNumber):
    print(f'Bin {bin(inputNumber)}');
    print(f'Oct {oct(inputNumber)}');
    print(f'Hex {hex(inputNumber)}');

def saveFileBinary(numberInput):
    filename = "binary_file.bin"  # The filename to save the binary data to
    num = int(numberInput)
    # Convert the string to binary data
    binary_data = num.to_bytes(1, byteorder='big')

    # Write the binary data to a file
    with open(filename, "wb") as file:
        file.write(binary_data)

    print(f"The number '{numberInput}' has been saved as binary data to '{filename}'.")

def saveFileText(numberInput):
    filename = "binary_file.bin"  # The filename to save the binary data to

    # Write the binary data to a file
    with open(filename, "w") as file:
        file.write(numberInput)

    print(f"The number '{numberInput}' has been saved as binary data to '{filename}'.")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number = input('Enter a number: ');
    #printHexDualOct(int(number));
    #saveFileBinary(number);
    saveFileText(number);

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
