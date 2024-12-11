def is_safe(levels):
    # Convert string of numbers to list of integers
    nums = list(map(int, levels.split()))
    
    # Check if sequence has any duplicates
    if len(set(nums)) != len(nums):
        return False
    
    # Get differences between adjacent numbers
    diffs = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    
    # Check if all differences are between 1 and 3 or -3 and -1
    valid_diffs = all(1 <= abs(d) <= 3 for d in diffs)
    
    # Check if all differences have the same sign (all increasing or all decreasing)
    same_direction = all(d > 0 for d in diffs) or all(d < 0 for d in diffs)
    
    return valid_diffs and same_direction

def is_safe_with_dampener(levels):
    # First check if it's safe without dampener
    if is_safe(levels):
        return True
    
    # Convert string to list of numbers
    nums = list(map(int, levels.split()))
    
    # Try removing each number one at a time
    for i in range(len(nums)):
        # Create new list without current number
        test_nums = nums[:i] + nums[i+1:]
        # Convert back to string format
        test_levels = ' '.join(map(str, test_nums))
        # Check if safe with this number removed
        if is_safe(test_levels):
            return True
    
    return False

def process_input_file(filename):
    try:
        with open(filename, 'r') as file:
            # Read all lines and count safe reports
            return sum(1 for line in file if is_safe_with_dampener(line.strip()))
    except FileNotFoundError:
        print(f"Error: Could not find file {filename}")
        return None
    except Exception as e:
        print(f"Error processing file: {e}")
        return None

# Run the solution
result = process_input_file('Day 2 Input.txt')
if result is not None:
    print(f"Number of safe reports with Problem Dampener: {result}")