# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt

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

def plot():
    # Create a grid of pixels
    n = 1000
    x, y = np.meshgrid(np.linspace(0, 1, n), np.linspace(0, 1, n))

    # Create the first circle
    x0, y0, r0 = 0.4, 0.5, 0.2
    circle0 = np.sqrt((x - x0) ** 2 + (y - y0) ** 2) < r0

    # Create the second circle
    x1, y1, r1 = 0.5, 0.6, 0.2
    circle1 = np.sqrt((x - x1) ** 2 + (y - y1) ** 2) < r1

    # Create the third circle
    x2, y2, r2 = 0.6, 0.5, 0.2
    circle2 = np.sqrt((x - x2)**2 + (y - y2)**2) < r2

    # Combine the circles using additive blending
    additive_blend = np.zeros((n, n, 3))
    additive_blend[:, :, 0] = circle0
    additive_blend[:, :, 1] = circle1
    additive_blend[:, :, 2] = circle2
    #additive_blend = np.clip(additive_blend, 0, 1)
    #additive_blend = 1 - np.exp(-additive_blend ** 2)

    # Create a figure and plot the additive blend
    fig, ax = plt.subplots()
    ax.imshow(additive_blend)

    # Hide the axis labels and ticks
    ax.axis('off')

    # Show the plot
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #number = input('Enter a number: ');
    #printHexDualOct(int(number));
    #saveFileBinary(number);
    #saveFileText(number);
    plot();

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
