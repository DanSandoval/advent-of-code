def count_xmas_occurrences(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_word(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check_word(x, y, dx, dy):
                    count += 1
    return count

def check_mas(chars):
    # Check if three characters form MAS (forward or backward)
    return (chars[0] == 'M' and chars[1] == 'A' and chars[2] == 'S') or \
           (chars[0] == 'S' and chars[1] == 'A' and chars[2] == 'M')

def count_x_mas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_x_pattern(x, y):
        # Need valid positions for both diagonals through center
        if not all(is_valid(x+dx, y+dy) for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]):
            return False
            
        # Get the characters in each diagonal
        # First diagonal: top-left to bottom-right
        diag1 = [grid[x-1][y-1], grid[x][y], grid[x+1][y+1]]
        # Second diagonal: top-right to bottom-left
        diag2 = [grid[x-1][y+1], grid[x][y], grid[x+1][y-1]]
        
        # Both diagonals must form valid MAS patterns (either direction)
        return check_mas(diag1) and check_mas(diag2)

    for x in range(1, rows-1):  # Skip edges since we need valid diagonals
        for y in range(1, cols-1):
            if check_x_pattern(x, y):
                count += 1
                
    return count

# Read input and solve both parts
try:
    with open("Day 4 Input.txt", 'r') as file:
        grid = [line.strip() for line in file]
        
    # Solve Part 1
    xmas_count = count_xmas_occurrences(grid)
    print(f"Part 1 - XMAS occurrences: {xmas_count}")
    
    # Solve Part 2
    x_mas_count = count_x_mas_patterns(grid)
    print(f"Part 2 - X-MAS patterns: {x_mas_count}")
    
except FileNotFoundError:
    print("Error: Could not find file Day 4 Input.txt")