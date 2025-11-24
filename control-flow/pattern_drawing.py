# pattern_drawing.py

# Ask the user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to control rows
while row < size:
    # Inside the while loop, use a for loop to print * side by side
    for i in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1  # Increment the row counter
