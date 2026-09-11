"""
LeetCode #11: Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Time Complexity: O(n) - single pass with two pointers
Space Complexity: O(1) - constant extra space
"""

from typing import List

def max_area(height: List[int]) -> int:
    """
    Find maximum area between two lines using two-pointer technique.
    
    Args:
        height: List of non-negative integers representing line heights
        
    Returns:
        Maximum area of water that can be contained
    """
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        max_area = max(max_area, current_area)
        
        # Move pointer pointing to shorter line
        # This is optimal because area is limited by shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Brute force approach for comparison (O(n^2) time)
def max_area_brute_force(height: List[int]) -> int:
    """
    Brute force solution checking all pairs.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    max_area = 0
    n = len(height)
    
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            current_height = min(height[i], height[j])
            current_area = width * current_height
            max_area = max(max_area, current_area)
    
    return max_area

# Test cases
if __name__ == "__main__":
    # Test case 1: [1,8,6,2,5,4,8,3,7] -> 49
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Input: height = {height1}")
    print(f"Output: {max_area(height1)}")  # Expected: 49
    print(f"Brute force: {max_area_brute_force(height1)}")  # Verification
    print()
    
    # Test case 2: [1,1] -> 1
    height2 = [1, 1]
    print(f"Input: height = {height2}")
    print(f"Output: {max_area(height2)}")  # Expected: 1
    print()
    
    # Test case 3: [4,3,2,1,4] -> 16
    height3 = [4, 3, 2, 1, 4]
    print(f"Input: height = {height3}")
    print(f"Output: {max_area(height3)}")  # Expected: 16
    print()
    
    # Test case 4: [1,2,1] -> 2
    height4 = [1, 2, 1]
    print(f"Input: height = {height4}")
    print(f"Output: {max_area(height4)}")  # Expected: 2
    print()
    
    # Test case 5: Single element
    height5 = [1]
    print(f"Input: height = {height5}")
    print(f"Output: {max_area(height5)}")  # Expected: 0