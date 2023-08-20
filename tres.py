def solve(s):
    # Define a string containing vowels
    vowels = "aeiou"

    # Create a dictionary to map characters to their respective values
    char_values = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
        'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
        'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }

    # Initialize variables to store the maximum value and the current substring value
    max_value = 0
    current_value = 0

    # Iterate through the characters in the input string
    for char in s:
        # Check if the character is a consonant (not a vowel)
        if char not in vowels:
            # Update the current substring value by adding the value of the character
            current_value += char_values[char]
        else:
            # If a vowel is encountered, update the maximum value if needed and reset the current substring value
            max_value = max(max_value, current_value)
            current_value = 0

    # Update the maximum value one last time (in case the string ends with consonants)
    max_value = max(max_value, current_value)

    return max_value


