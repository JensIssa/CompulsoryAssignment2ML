# filename: average_numbers.py

import time
import numpy as np

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        float: The average of the numbers in the list.
    """
    start_time = time.time()
    
    # Check if the input is a list
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list of numbers.")
    
    # Check if all elements in the list are numbers
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be numbers.")
    
    # Calculate the average using NumPy
    average = np.mean(numbers)
    
    end_time = time.time()
    run_time = (end_time - start_time) * 1000
    
    print(f"Average: {average}")
    print(f"Run Time: {run_time:.2f} ms")
    
    if run_time < 50:
        print("TERMINATE")
    else:
        # Repeat the process with a more optimal solution
        pass

# Example usage:
numbers = [1, 2, 3, 4, 5]
calculate_average(numbers)