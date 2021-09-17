def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    max = numbers[0]
    for digit in numbers:
        if digit > max:
            max = digit
    return max


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
