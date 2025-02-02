def pattern_b():
    rows = 5
    numbers = [1, 3, 5, 6, 7] 
    i = 0  # Start with the first index

    while i < rows:  # Loop through each row
        j = 0
        while j < numbers[i]:  # Print the number 'numbers[i]' times
            print(numbers[i], end="")  # Print the number without a newline
            j += 1
        print()  
        i += 1

pattern_b()
