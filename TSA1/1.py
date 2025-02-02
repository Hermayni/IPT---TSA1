def count_characters(input_string):
    vowels = 'aeiouAEIOU'
    num_vowels = 0
    num_consonants = 0
    num_spaces = 0
    num_others = 0
    
    # Loop through each character in the input string
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
        elif char.isspace():  # Check if the character is a space
            num_spaces += 1
        else:  # Any other character (digits, punctuation, etc.)
            num_others += 1
            
    # Display the results
    print(f"Vowels: {num_vowels}")
    print(f"Consonants: {num_consonants}")
    print(f"Spaces: {num_spaces}")
    print(f"Others: {num_others}")

# Ask the user for input and call the function
input_string = input("Enter a string: ")
count_characters(input_string)
