"""
LeetCode #20: Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Time Complexity: O(n) - single pass through string
Space Complexity: O(n) - stack storage
"""

def is_valid(s: str) -> bool:
    """
    Check if parentheses string is valid using stack.
    
    Args:
        s: String containing parentheses characters
        
    Returns:
        True if valid, False otherwise
    """
    # Mapping of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in bracket_map:  # Closing bracket
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:  # Opening bracket
            stack.append(char)
    
    # String is valid if stack is empty (all brackets matched)
    return len(stack) == 0

# Alternative approach using replace (less efficient but concise)
def is_valid_replace(s: str) -> bool:
    """Alternative solution using string replacement."""
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return len(s) == 0

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(((({{[[]]}}))))", True),
        ("[({})](]", False)
    ]
    
    print("Testing Valid Parentheses solution:")
    print("-" * 40)
    for s, expected in test_cases:
        result = is_valid(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}' -> Output: {result} (Expected: {expected})")