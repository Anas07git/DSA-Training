def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # In case k is larger than n
    return arr[-k:] + arr[:-k]

# Example usage
input_array = [1, 2, 3, 4, 5]
k = 2
output_array = rotate_array(input_array, k)
print("Input array:", input_array)
print("Number of rotations:", k)
print("Rotated array:", output_array)
