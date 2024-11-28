# filename: average_numbers.py

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers.
    """
    # Check if the input is a list
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")

    # Check if the list contains at least one number
    if len(numbers) == 0:
        return None

    # Calculate the sum of the numbers
    total = sum(numbers)

    # Calculate the average
    average = total / len(numbers)

    return average


# Example usage:
numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("The average is:", average)