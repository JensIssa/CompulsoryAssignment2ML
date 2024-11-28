# filename: order_list.py

def order_list(numbers):
    """
    Orders a list of numbers correctly.
    
    Args:
        numbers (list): A list of numbers to be ordered.
    
    Returns:
        list: The ordered list of numbers.
    
    Raises:
        ValueError: If the input list contains non-numeric values.
    """
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input list must contain only numeric values")
    return sorted(numbers)

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
ordered_numbers = order_list(numbers)
print("Ordered Numbers:", ordered_numbers)

empty_list = []
try:
    ordered_empty_list = order_list(empty_list)
except ValueError as e:
    print(f"Error: {e}")

non_numeric_list = [64, '34', 25, 12, 22, 11, 90]
try:
    ordered_non_numeric_list = order_list(non_numeric_list)
except ValueError as e:
    print(f"Error: {e}")