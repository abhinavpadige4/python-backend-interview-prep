"""
LeetCode #3: Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Time Complexity: O(n) - single pass with sliding window
Space Complexity: O(min(m, n)) - where m is size of character set
"""

def length_of_longest_substring(s: str) -> int:
    """
    Find length of longest substring without repeating characters using sliding window.
    
    Args:
        s: Input string
        
    Returns:
        Length of longest substring without repeating characters
    """
    char_index_map = {}  # character -> most recent index
    max_length = 0
    left = 0  # start of sliding window
    
    for right in range(len(s)):
        char = s[right]
        
        # If character is in current window, move left pointer
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1
        
        # Update character's most recent index
        char_index_map[char] = right
        
        # Update max length
        current_length = right - left + 1
        max_length = max(max_length, current_length)
    
    return max_length

# Alternative approach using array for ASCII characters
def length_of_longest_substring_array(s: str) -> int:
    """
    Find length using fixed-size array for ASCII character set.
    
    Time Complexity: O(n)
    Space Complexity: O(1) - fixed size 128 for ASCII
    """
    if not s:
        return 0
    
    char_array = [-1] * 128  # ASCII character set
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        char_index = ord(s[right])
        
        # If character seen in current window, move left pointer
        if char_array[char_index] >= left:
            left = char_array[char_index] + 1
        
        # Update character's most recent index
        char_array[char_index] = right
        
        # Update max length
        current_length = right - left + 1
        max_length = max(max_length, current_length)
    
    return max_length

# Test cases
if __name__ == "__main__":
    # Test case 1: "abcabcbb" -> 3 ("abc")
    s1 = "abcabcbb"
    print(f"Input: s = '{s1}'")
    print(f"Output: {length_of_longest_substring(s1)}")  # Expected: 3
    print()
    
    # Test case 2: "bbbbb" -> 1 ("b")
    s2 = "bbbbb"
    print(f"Input: s = '{s2}'")
    print(f"Output: {length_of_longest_substring(s2)}")  # Expected: 1
    print()
    
    # Test case 3: "pwwkew" -> 3 ("wke")
    s3 = "pwwkew"
    print(f"Input: s = '{s3}'")
    print(f"Output: {length_of_longest_substring(s3)}")  # Expected: 3
    print()
    
    # Test case 4: "" -> 0
    s4 = ""
    print(f"Input: s = '{s4}'")
    print(f"Output: {length_of_longest_substring(s4)}")  # Expected: 0
    print()
    
    # Test case 5: "abcdefg" -> 7
    s5 = "abcdefg"
    print(f"Input: s = '{s5}'")
    print(f"Output: {length_of_longest_substring(s5)}")  # Expected: 7
    print()
    
    # Test case 6: "abba" -> 2 ("ab" or "ba")
    s6 = "abba"
    print(f"Input: s = '{s6}'")
    print(f"Output: {length_of_longest_substring(s6)}")  # Expected: 2