"""
LeetCode #15: 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Time Complexity: O(n^2) - sorting (O(n log n)) + two-pointer scan (O(n^2))
Space Complexity: O(1) or O(n) depending on sorting algorithm
"""

from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero using two-pointer technique.
    
    Args:
        nums: List of integers
        
    Returns:
        List of unique triplets that sum to zero
    """
    nums.sort()  # Sort to enable two-pointer technique and easy duplicate handling
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two-pointer approach for remaining array
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < 0:
                # Need larger sum, move left pointer right
                left += 1
            else:
                # Need smaller sum, move right pointer left
                right -= 1
    
    return result

# Alternative approach using hash set (less efficient due to duplicate handling)
def three_sum_hash(nums: List[int]) -> List[List[int]]:
    """
    Find triplets using hash set for O(n^2) time but more complex duplicate handling.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    nums.sort()
    result = []
    seen = set()
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        target = -nums[i]
        seen_two_sum = set()
        
        for j in range(i + 1, len(nums)):
            complement = target - nums[j]
            
            if complement in seen_two_sum:
                triplet = [nums[i], complement, nums[j]]
                # Sort triplet to handle duplicates consistently
                triplet.sort()
                triplet_tuple = tuple(triplet)
                
                if triplet_tuple not in seen:
                    seen.add(triplet_tuple)
                    result.append(triplet)
            
            seen_two_sum.add(nums[j])
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {three_sum(nums1)}")
    # Expected: [[-1,-1,2], [-1,0,1]] (order may vary)
    print()
    
    # Test case 2: [] -> []
    nums2 = []
    print(f"Input: nums = {nums2}")
    print(f"Output: {three_sum(nums2)}")  # Expected: []
    print()
    
    # Test case 3: [0] -> []
    nums3 = [0]
    print(f"Input: nums = {nums3}")
    print(f"Output: {three_sum(nums3)}")  # Expected: []
    print()
    
    # Test case 4: [0,0,0] -> [[0,0,0]]
    nums4 = [0, 0, 0]
    print(f"Input: nums = {nums4}")
    print(f"Output: {three_sum(nums4)}")  # Expected: [[0,0,0]]
    print()
    
    # Test case 5: No solution
    nums5 = [1, 2, 3]
    print(f"Input: nums = {nums5}")
    print(f"Output: {three_sum(nums5)}")  # Expected: []