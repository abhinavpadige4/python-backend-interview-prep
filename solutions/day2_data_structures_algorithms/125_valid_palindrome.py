"""
LeetCode #125: Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Time Complexity: O(n) - single pass through string
Space Complexity: O(1) - constant extra space (two pointers)
"""

def is_palindrome(s: str) -> bool:
    """
    Check if string is palindrome after removing non-alphanumeric and lowercasing.
    
    Args:
        s: Input string
        
    Returns:
        True if palindrome, False otherwise
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# Alternative approach: preprocess string then check
def is_palindrome_preprocess(s: str) -> bool:
    """
    Check palindrome by preprocessing string first.
    
    Time Complexity: O(n)
    Space Complexity: O(n) - for cleaned string
    """
    # Filter alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if cleaned string is palindrome
    return cleaned == cleaned[::-1]

# Test cases
if __name__ == "__main__":
    # Test case 1: "A man, a plan, a canal: Panama" -> True
    s1 = "A man, a plan, a canal: Panama"
    print(f"Input: s = '{s1}'")
    print(f"Output: {is_palindrome(s1)}")  # Expected: True
    print()
    
    # Test case 2: "race a car" -> False
    s2 = "race a car"
    print(f"Input: s = '{s2}'")
    print(f"Output: {is_palindrome(s2)}")  # Expected: False
    print()
    
    # Test case 3: " " -> True (empty string after removing non-alphanumeric)
    s3 = " "
    print(f"Input: s = '{s3}'")
    print(f"Output: {is_palindrome(s3)}")  # Expected: True
    print()
    
    # Test case 4: "0P" -> False
    s4 = "0P"
    print(f"Input: s = '{s4}'")
    print(f"Output: {is_palindrome(s4)}")  # Expected: False
    print()
    
    # Test case 5: "a." -> True
    s5 = "a."
    print(f"Input: s = '{s5}'")
    print(f"Output: {is_palindrome(s5)}")  # Expected: True
    print()
    
    # Test case 6: "ab_a" -> True
    s6 = "ab_a"
    print(f"Input: s = '{s6}'")
    print(f"Output: {is_palindrome(s6)}")  # Expected: True