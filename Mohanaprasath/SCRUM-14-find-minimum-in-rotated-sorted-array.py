def find_min_in_rotated_sorted_array(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]

# Example usage
input1 = [3, 4, 5, 1, 2]
input2 = [4, 5, 6, 7, 0, 1, 2]

output1 = find_min_in_rotated_sorted_array(input1)
output2 = find_min_in_rotated_sorted_array(input2)

print("Input:", input1)
print("Output:", output1)

print("Input:", input2)
print("Output:", output2)
