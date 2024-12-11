def calculate_list_distance(filename):
    """
    Part 1: Calculate total distance between sorted pairs from two lists.
    """
    # Read the input file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Create two lists for left and right numbers
    left_list = []
    right_list = []
    
    # Parse each line and add numbers to respective lists
    for line in lines:
        if line.strip():  # Skip empty lines
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate total distance between corresponding pairs
    total_distance = 0
    for i in range(len(left_list)):
        distance = abs(left_list[i] - right_list[i])
        total_distance += distance
    
    return total_distance

def calculate_similarity_score(filename):
    """
    Part 2: Calculate similarity score based on number occurrences.
    """
    # Read the input file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Create two lists for left and right numbers
    left_list = []
    right_list = []
    
    # Parse each line and add numbers to respective lists
    for line in lines:
        if line.strip():  # Skip empty lines
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    # Calculate similarity score
    similarity_score = 0
    
    # For each number in left list
    for num in left_list:
        # Count how many times it appears in right list
        count_in_right = right_list.count(num)
        # Add to similarity score (num * count)
        similarity_score += num * count_in_right
        
    return similarity_score

if __name__ == "__main__":
    input_file = "Day 1 Input.txt"
    
    # Part 1
    distance = calculate_list_distance(input_file)
    print("Part 1 - Total Distance:", distance)
    
    # Part 2
    similarity = calculate_similarity_score(input_file)
    print("Part 2 - Similarity Score:", similarity)