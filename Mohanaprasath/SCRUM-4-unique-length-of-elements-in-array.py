def remove_duplicates(nums):
    if not nums:
        return 0
    
    # Initialize a pointer to keep track of unique elements
    unique_index = 0
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous unique element
        if nums[i] != nums[unique_index]:
            # Move the unique_index forward
            unique_index += 1
            # Update the unique element at unique_index position
            nums[unique_index] = nums[i]
    
    # Length of array with unique elements (including the first unique element)
    return unique_index + 1

# Example usage
input_array = [0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3]
unique_length = remove_duplicates(input_array)
print("Length of array with unique elements:", unique_length)

