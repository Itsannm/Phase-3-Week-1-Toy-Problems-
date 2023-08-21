#Challenge 2: Two numbers are positive.

def exactly_two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2



result1 = exactly_two_positive(1, 2, -1)
print(result1)  # Output: True (exactly two are positive)

result2 = exactly_two_positive(-1, -2, 3)
print(result2)  # Output: False (only one is positive)

result3 = exactly_two_positive(0, 2, 4)
print(result3)  # Output: True (atleast two positive)

result4 = exactly_two_positive(0, 0, 0)
print(result4)  # Output: False (none are positive)
