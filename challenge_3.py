#Challenge 3: Consonant value


def solve(s):
    vowels = "aeiou"
    char_values = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
        'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
        'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }

    max_value = 0
    current_value = 0

    for char in s:
        if char not in vowels:
            current_value += char_values[char]
        else:
            max_value = max(max_value, current_value)
            current_value = 0

    max_value = max(max_value, current_value)

    return max_value


print(solve("zodiacs"))   # Output: 26
print(solve("strength"))  # Output: 57