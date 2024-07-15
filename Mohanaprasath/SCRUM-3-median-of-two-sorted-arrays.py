def find_median_sorted_arrays(nums1, nums2):
    merged_array = sorted(nums1 + nums2)
    total_length = len(merged_array)
    if total_length % 2 == 1:
        median = merged_array[total_length // 2]
    else:
        median = (merged_array[total_length // 2 - 1] + merged_array[total_length // 2]) / 2.0
    return median

# Input from the user
nums1 = list(map(int, input("Enter the elements of nums1 separated by space: ").split()))
nums2 = list(map(int, input("Enter the elements of nums2 separated by space: ").split()))

# Find the median
median = find_median_sorted_arrays(nums1, nums2)

# Output the result
print("Median of the two sorted arrays:", median)
