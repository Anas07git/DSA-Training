def subsets(nums):
    result = [[]]
    for num in nums:
        result += [subset + [num] for subset in result]
        
    return result

# Test case
print(subsets([1, 2, 3]))