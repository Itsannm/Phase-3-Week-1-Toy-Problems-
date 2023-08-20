# Phase-3-Week-1-Toy-Problems
This ReadMe presents solutions to three coding challenges using Python. Each challenge is described, followed by its corresponding solution. These challenges cover various aspects of Python programming, from time conversion to conditional logic.

## Challenge 1: Converting 12-hour Time to 24-hour Time

### Problem Statement:
You are given an hour (in the range of 1 to 12), a minute (in the range of 0 to 59), and a period (either "am" or "pm"). Your task is to convert this 12-hour time into 24-hour time.

### Solution:
```python
def convert_to_24_hour(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    return f"{hour:02d}:{minute:02d}"
```

## Challenge 2: Counting Positive Integers

### Problem Statement:
Given three integers `a`, `b`, and `c`, the task is to determine if exactly two of them are positive numbers (greater than zero).

### Solution:
```python
def exactly_two_positive(a, b, c):
    positive_count = 0
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    return positive_count == 2
```

## Challenge 3: Finding the Highest Value of Consonant Substrings

### Problem Statement:
Given a lowercase string containing only alphabetic characters (no spaces), find the highest value of consonant substrings. Consonants are any letters except "aeiou," and their values are assigned (a = 1, b = 2, c = 3, ..., z = 26).

### Solution:
```python
def highest_consonant_value(s):
    vowels = "aeiou"
    char_values = {'a': 1, 'b': 2, ... 'z': 26}
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
```

These solutions demonstrate the use of basic Python functions, conditional statements, and loops to address common coding challenges. Feel free to use and adapt these solutions for your own projects.