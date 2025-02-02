# Ask the user for input
input_string = input("Enter a string: ")

# Initialize sum variable
total_sum = 0


for char in input_string:
    if char >= '0' and char <= '9':  # Check if it's a digit
        total_sum += int(char)  # Convert to integer and add

# Print the result
print("Sum of digits:", total_sum)

