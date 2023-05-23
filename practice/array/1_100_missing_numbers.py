def find_missing_number(numbers):
    """
    This function finds the missing number in an array of 1-100 numbers.
    """
    expected_sum = sum(range(1, 15))
    actual_sum = sum(numbers)
    missing_number = expected_sum - actual_sum
    return missing_number


# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
print(find_missing_number(numbers))
