"""
LeetCode #167: Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number.

Time Complexity: O(n) - single pass with two pointers
Space Complexity: O(1) - constant extra space
"""

from typing import List

def two_sum(numbers: List[int], target: int) -> List[int]:
    """
    Find two numbers in sorted array that add up to target using two pointers.
    
    Args:
        numbers: Sorted list of integers (1-indexed in problem description)
        target: Target sum
        
    Returns:
        List containing 1-indexed positions of the two numbers
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # Return 1-indexed positions as required by problem
            return [left + 1, right + 1]
        elif current_sum < target:
            # Need larger sum, move left pointer right
            left += 1
        else:
            # Need smaller sum, move right pointer left
            right -= 1
    
    return []  # No solution found (problem guarantees exactly one solution)

# Alternative approach using binary search for each element
def two_sum_binary_search(numbers: List[int], target: int) -> List[int]:
    """
    Find two numbers using binary search for each element.
    
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    for i in range(len(numbers)):
        complement = target - numbers[i]
        # Binary search for complement in remaining array
        left, right = i + 1, len(numbers) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == complement:
                return [i + 1, mid + 1]  # 1-indexed
            elif numbers[mid] < complement:
                left = mid + 1
            else:
                right = mid - 1
    
    return []

# Test cases
if __name__ == "__main__":
    # Test case 1: [2,7,11,15], target = 9 -> [1,2]
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: numbers = {numbers1}, target = {target1}")
    print(f"Output: {two_sum(numbers1, target1)}")  # Expected: [1, 2]
    print()
    
    # Test case 2: [2,3,4], target = 6 -> [1,3]
    numbers2 = [2, 3, 4]
    target2 = 6
    print(f"Input: numbers = {numbers2}, target = {target2}")
    print(f"Output: {two_sum(numbers2, target2)}")  # Expected: [1, 3]
    print()
    
    # Test case 3: [-1,0], target = -1 -> [1,2]
    numbers3 = [-1, 0]
    target3 = -1
    print(f"Input: numbers = {numbers3}, target = {target3}")
    print(f"Output: {two_sum(numbers3, target3)}")  # Expected: [1, 2]
    print()
    
    # Test case 4: Larger array
    numbers4 = [1, 2, 3, 4, 4, 9, 56, 90]
    target4 = 8
    print(f"Input: numbers = {numbers4}, target = {target4}")
    print(f"Output: {two_sum(numbers4, target4)}")  # Expected: [4, 5] (values 4+4)