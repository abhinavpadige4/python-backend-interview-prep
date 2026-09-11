"""
LeetCode #238: Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the 
product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Time Complexity: O(n) - two passes through array
Space Complexity: O(1) excluding output array (or O(n) including output)
"""

from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    """
    Calculate product of array except self using prefix and suffix products.
    
    Args:
        nums: List of integers
        
    Returns:
        List where each element is product of all other elements
    """
    n = len(nums)
    answer = [1] * n
    
    # Calculate prefix products: answer[i] contains product of all elements to left of i
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    
    # Calculate suffix products and multiply with prefix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    
    return answer

# Alternative approach using division (not allowed by problem constraints but shown for understanding)
def product_except_self_with_division(nums: List[int]) -> List[int]:
    """
    Calculate product using division (violates problem constraint but simpler).
    
    Time Complexity: O(n)
    Space Complexity: O(1) excluding output
    """
    # Handle zeros specially
    zero_count = nums.count(0)
    
    if zero_count > 1:
        # More than one zero means all products are zero
        return [0] * len(nums)
    elif zero_count == 1:
        # Exactly one zero: only position with zero gets product of non-zeros
        total_product = 1
        for num in nums:
            if num != 0:
                total_product *= num
        
        result = [0] * len(nums)
        zero_index = nums.index(0)
        result[zero_index] = total_product
        return result
    else:
        # No zeros: divide total product by each element
        total_product = 1
        for num in nums:
            total_product *= num
        
        return [total_product // num for num in nums]

# Test cases
if __name__ == "__main__":
    # Test case 1: [1,2,3,4] -> [24,12,8,6]
    nums1 = [1, 2, 3, 4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {product_except_self(nums1)}")  # Expected: [24, 12, 8, 6]
    print()
    
    # Test case 2: [-1,1,0,-3,3] -> [0,0,9,0,0]
    nums2 = [-1, 1, 0, -3, 3]
    print(f"Input: nums = {nums2}")
    print(f"Output: {product_except_self(nums2)}")  # Expected: [0, 0, 9, 0, 0]
    print()
    
    # Test case 3: [0,0] -> [0,0]
    nums3 = [0, 0]
    print(f"Input: nums = {nums3}")
    print(f"Output: {product_except_self(nums3)}")  # Expected: [0, 0]
    print()
    
    # Test case 4: [2,3,4,5] -> [60,40,30,24]
    nums4 = [2, 3, 4, 5]
    print(f"Input: nums = {nums4}")
    print(f"Output: {product_except_self(nums4)}")  # Expected: [60, 40, 30, 24]
    print()
    
    # Test case 5: Single element
    nums5 = [5]
    print(f"Input: nums = {nums5}")
    print(f"Output: {product_except_self(nums5)}")  # Expected: [1]
    print()
    
    # Test case 6: With negative numbers
    nums6 = [-2, 3, -4]
    print(f"Input: nums = {nums6}")
    print(f"Output: {product_except_self(nums6)}")  # Expected: [-12, 8, -6]