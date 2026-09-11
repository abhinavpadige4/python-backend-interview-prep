"""
LeetCode #295: Find Median from Data Stream
The median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value, and the median is the mean of the two middle values.
For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far.

Time Complexity: 
- addNum: O(log n) - heap insertion
- findMedian: O(1) - accessing heap tops
Space Complexity: O(n) - storing all elements in heaps
"""

import heapq

class MedianFinder:
    """
    MedianFinder using two heaps:
    - max_heap (left): stores the smaller half of numbers (as negatives for max-heap behavior)
    - min_heap (right): stores the larger half of numbers
    
    Invariant: len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1
    """
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Max heap for smaller half (store negatives to simulate max heap)
        self.max_heap = []  # Contains smaller half of numbers
        # Min heap for larger half
        self.min_heap = []  # Contains larger half of numbers
    
    def addNum(self, num: int) -> None:
        """
        Add a number from the data stream to the data structure.
        
        Args:
            num: Integer to add to the data stream
        """
        # Add to max_heap first (as negative for max-heap behavior)
        heapq.heappush(self.max_heap, -num)
        
        # Ensure every element in max_heap <= every element in min_heap
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            # Move the largest element from max_heap to min_heap
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        
        # Balance the heaps: size difference should be at most 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            # Move element from max_heap to min_heap
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            # Move element from min_heap to max_heap
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
    
    def findMedian(self) -> float:
        """
        Return the median of all elements so far.
        
        Returns:
            Median as float
        """
        if len(self.max_heap) > len(self.min_heap):
            # Odd number of elements: max_heap has one more element
            return -self.max_heap[0]
        else:
            # Even number of elements: average of two middle elements
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0

# Alternative approach using sorted list (less efficient but simpler)
import bisect

class MedianFinderSortedList:
    """
    MedianFinder using sorted list (O(n) insertion, O(1) median).
    """
    
    def __init__(self):
        self.nums = []
    
    def addNum(self, num: int) -> None:
        """Add number while maintaining sorted order."""
        bisect.insort(self.nums, num)
    
    def findMedian(self) -> float:
        """Find median from sorted list."""
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[n // 2]
        else:
            return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2.0

# Alternative approach using two multisets (conceptual)
class MedianFinderMultiset:
    """
    MedianFinder concept using two multisets (similar to heap approach).
    This is more conceptual as Python doesn't have built-in multiset.
    """
    
    def __init__(self):
        self.small = []  # max heap for smaller half
        self.large = []  # min heap for larger half
    
    def addNum(self, num: int) -> None:
        """Add number maintaining heap invariants."""
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        # Rebalance heaps
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def findMedian(self) -> float:
        """Return median."""
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2.0

# Test cases
if __name__ == "__main__":
    # Test case 1: addNum(1), addNum(2), findMedian() -> 1.5, addNum(3), findMedian() -> 2.0
    print("Test Case 1: Stream [1, 2, 3]")
    medianFinder = MedianFinder()
    
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    median1 = medianFinder.findMedian()
    print(f"After adding [1, 2]: median = {median1}")  # Expected: 1.5
    
    medianFinder.addNum(3)
    median2 = medianFinder.findMedian()
    print(f"After adding [1, 2, 3]: median = {median2}")  # Expected: 2.0
    print()
    
    # Test case 2: addNum(1), findMedian() -> 1, addNum(2), findMedian() -> 1.5
    print("Test Case 2: Stream [1, 2]")
    medianFinder2 = MedianFinder()
    
    medianFinder2.addNum(1)
    median3 = medianFinder2.findMedian()
    print(f"After adding [1]: median = {median3}")  # Expected: 1.0
    
    medianFinder2.addNum(2)
    median4 = medianFinder2.findMedian()
    print(f"After adding [1, 2]: median = {median4}")  # Expected: 1.5
    print()
    
    # Test case 3: addNum(5), addNum(3), addNum(4), findMedian() -> 4.0
    print("Test Case 3: Stream [5, 3, 4]")
    medianFinder3 = MedianFinder()
    
    medianFinder3.addNum(5)
    medianFinder3.addNum(3)
    medianFinder3.addNum(4)
    median5 = medianFinder3.findMedian()
    print(f"After adding [5, 3, 4]: median = {median5}")  # Expected: 4.0
    print()
    
    # Test case 4: Single element
    print("Test Case 4: Single element [100]")
    medianFinder4 = MedianFinder()
    medianFinder4.addNum(100)
    median6 = medianFinder4.findMedian()
    print(f"After adding [100]: median = {median6}")  # Expected: 100.0
    print()
    
    # Test case 5: Duplicate values
    print("Test Case 5: Stream [2, 2, 2, 2]")
    medianFinder5 = MedianFinder()
    
    for _ in range(4):
        medianFinder5.addNum(2)
    
    median7 = medianFinder5.findMedian()
    print(f"After adding [2, 2, 2, 2]: median = {median7}")  # Expected: 2.0
    print()
    
    # Test case 6: Negative numbers
    print("Test Case 6: Stream [-1, -2, -3, -4, -5]")
    medianFinder6 = MedianFinder()
    
    nums = [-1, -2, -3, -4, -5]
    for num in nums:
        medianFinder6.addNum(num)
    
    median8 = medianFinder6.findMedian()
    print(f"After adding {nums}: median = {median8}")  # Expected: -3.0