def is_palindrome(obj):
    # Convert input to string
    s = str(obj)
    # Compare the string with its reverse
    return s == s[::-1]

# Test cases
print(is_palindrome(121))      # True
print(is_palindrome("1231"))   # False
print(is_palindrome("racecar"))  # True
print(is_palindrome(12321))    # True
print(is_palindrome(1.1))      # True