import re

def calculate_sum_of_multiplications(corrupted_memory):
    # Define the regex pattern for valid mul(X,Y)
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find all matches in the corrupted memory
    matches = re.findall(pattern, corrupted_memory)
    
    # Calculate the sum of all valid multiplications
    total = 0
    for match in matches:
        x, y = map(int, match)  # Convert extracted numbers to integers
        total += x * y          # Multiply and add to the total
    
    return total

def calculate_sum_with_conditions(corrupted_memory):
    # Define the regex pattern for all relevant instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    
    # Find all matches in the order they appear
    matches = re.finditer(pattern, corrupted_memory)
    
    total = 0
    enabled = True  # Multiplications are enabled by default

    for match in matches:
        # Extract matched content
        instruction = match.group(0)
        
        if instruction.startswith("mul("):  # Valid mul(X,Y) instruction
            if enabled:  # Only process if enabled
                # Extract numbers and calculate product
                x, y = map(int, match.groups())
                total += x * y
        elif instruction == "do()":  # Enable future mul instructions
            enabled = True
        elif instruction == "don't()":  # Disable future mul instructions
            enabled = False
    
    return total

# Read input from the file
input_file = "Day 3 Input.txt"

try:
    with open(input_file, "r") as file:
        corrupted_memory = file.read()  # Read the entire file content
    
    # Compute the result
    result = calculate_sum_with_conditions(corrupted_memory)
    
    # Print the result
    print("Total Sum of Enabled Multiplications:", result)

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")

