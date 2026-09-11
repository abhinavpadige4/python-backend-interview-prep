"""
LeetCode #347: Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Time Complexity: O(n log k) using min-heap, or O(n) using bucket sort
Space Complexity: O(n) - for frequency map and heap/buckets
"""

from typing import List
import heapq
from collections import Counter

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements using min-heap.
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
        
    Returns:
        List of k most frequent elements
    """
    # Count frequency of each element
    freq_map = Counter(nums)
    
    # Use min-heap to keep track of k most frequent elements
    # We store (-frequency, element) to simulate max-heap with min-heap
    # Actually, we'll use min-heap of size k to keep the k largest elements
    min_heap = []
    
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        # Keep heap size at most k
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # Extract elements from heap
    return [num for freq, num in min_heap]

# Alternative approach using bucket sort (O(n) time)
def top_k_frequent_bucket_sort(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements using bucket sort.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Count frequency of each element
    freq_map = Counter(nums)
    
    # Create buckets where index = frequency
    # Maximum frequency is len(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    # Place elements in buckets based on frequency
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    # Collect results from highest frequency buckets
    result = []
    for freq in range(len(buckets) - 1, 0, -1):  # From high to low frequency
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result

# Alternative approach using sorting
def top_k_frequent_sort(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements using sorting.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    freq_map = Counter(nums)
    # Sort by frequency (descending) and take top k
    return [num for num, _ in sorted(freq_map.items(), key=lambda x: x[1], reverse=True)[:k]]

# Test cases
if __name__ == "__main__":
    # Test case 1: [1,1,1,2,2,3], k = 2 -> [1,2]
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output (heap): {top_k_frequent(nums1, k1)}")  # Expected: [1, 2] (order may vary)
    print(f"Output (bucket): {top_k_frequent_bucket_sort(nums1, k1)}")  # Expected: [1, 2]
    print()
    
    # Test case 2: [1], k = 1 -> [1]
    nums2 = [1]
    k2 = 1
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {top_k_frequent(nums2, k2)}")  # Expected: [1]
    print()
    
    # Test case 3: [1,2,1,2,1,2,3,1,3,2], k = 2 -> [1,2]
    nums3 = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
    k3 = 2
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {top_k_frequent(nums3, k3)}")  # Expected: [1, 2] (1 appears 4 times, 2 appears 4 times)
    print()
    
    # Test case 4: [4,1,-1,2,-1,2,3], k = 2 -> [-1,2] or [2,-1]
    nums4 = [4, 1, -1, 2, -1, 2, 3]
    k4 = 2
    print(f"Input: nums = {nums4}, k = {k4}")
    print(f"Output: {top_k_frequent(nums4, k4)}")  # Expected: [-1, 2] or [2, -1] (both appear 2 times)
    print()
    
    # Test case 5: All same elements
    nums5 = [5, 5, 5, 5, 5]
    k5 = 1
    print(f"Input: nums = {nums5}, k = {k5}")
    print(f"Output: {top_k_frequent(nums5, k5)}")  # Expected: [5]