# Task: Write a Python function named sum_of_squares(nums)
# It should return the sum of squares of all numbers in the list.
# The function must include:
#  - Input validation (only numbers)
#  - Docstring and example usage
def sum_of_squares(nums):
    """
    Calculate the sum of squares of all numbers in the provided list.

    Parameters:
    nums (list): A list of numbers (integers or floats).

    Returns:
    float: The sum of squares of the numbers in the list.

    Raises:
    ValueError: If any element in the list is not a number.

    Example:
    >>> sum_of_squares([1, 2, 3])
    14
    
    >>> sum_of_squares([-1, -2, -3])
    14
    >>> sum_of_squares([0, 4, 5])
    41
    """
    total = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements in the list must be numbers.")
        total += num ** 2
    return total