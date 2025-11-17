def process_list(numbers):
    """Process a list of numbers: remove duplicates, sort and calculate mean."""
    # Remove duplicates
    unique_numbers = list(set(numbers))
    # Sort
    sorted_numbers = sorted(unique_numbers)
    # Calculate mean
    mean = sum(sorted_numbers) / len(sorted_numbers)
    return mean
