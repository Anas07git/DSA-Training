def permute(nums):
    def backtrack(start, end):
        if start == end:
            result.append(nums[:])
        for i in range(start, end):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1, end)
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0, len(nums))
    return result

# Example usage
nums = [1, 2, 3]
print(permute(nums))
