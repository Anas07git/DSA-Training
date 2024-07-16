def maxDepth(s: str) -> int:
    max_depth = 0
    current_depth = 0
    
    for char in s:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1
    
    return max_depth

# Test cases
print(maxDepth("(1+(2*3)+((8)/4))+1"))  # Output: 3
print(maxDepth("(1)+((2))+(((3)))"))    # Output: 3
print(maxDepth("1+(2*3)/(2-1)"))        # Output: 1
print(maxDepth("1"))                    # Output: 0