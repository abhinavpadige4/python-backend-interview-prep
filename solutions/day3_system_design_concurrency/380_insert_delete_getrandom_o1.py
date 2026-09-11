"""
LeetCode #380: Insert Delete GetRandom O(1)
Implement the RandomizedSet class:
- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. 
  Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. 
  Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements 
  (it's guaranteed that at least one element exists when this method is called). 
  Each element must have the same probability of being returned.

Time Complexity: O(1) average for all operations
Space Complexity: O(n) - where n is number of elements in set
"""

import random

class RandomizedSet:
    """
    RandomizedSet using hash map and list for O(1) operations.
    
    - List stores elements for O(1) random access
    - Hash map stores value -> index mapping for O(1) lookup
    - To remove in O(1): swap element with last element, then pop last
    """
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []           # List to store elements
        self.val_to_index = {}   # Hash map: value -> index in nums list
    
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        
        Args:
            val: Value to insert
            
        Returns:
            True if value was inserted, False if it already existed
        """
        if val in self.val_to_index:
            return False
        
        # Add to end of list and update hash map
        self.val_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        
        Args:
            val: Value to remove
            
        Returns:
            True if value was removed, False if it didn't exist
        """
        if val not in self.val_to_index:
            return False
        
        # Get index of element to remove
        index_to_remove = self.val_to_index[val]
        last_element = self.nums[-1]
        
        # Move last element to the position of element to remove
        self.nums[index_to_remove] = last_element
        self.val_to_index[last_element] = index_to_remove
        
        # Remove last element
        self.nums.pop()
        del self.val_to_index[val]
        
        return True
    
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        
        Returns:
            Random element from the set
        """
        return random.choice(self.nums)

# Alternative approach using only list (O(n) for insert/remove, O(1) for getRandom)
class RandomizedSetListOnly:
    """
    RandomizedSet using only list (less efficient but simpler).
    
    Time Complexity:
    - insert: O(n) - need to check for duplicates
    - remove: O(n) - need to find and remove element
    - getRandom: O(1) - random choice from list
    """
    
    def __init__(self):
        self.nums = []
    
    def insert(self, val: int) -> bool:
        """Insert value if not present."""
        if val in self.nums:
            return False
        self.nums.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        """Remove value if present."""
        if val not in self.nums:
            return False
        self.nums.remove(val)  # O(n) operation
        return True
    
    def getRandom(self) -> int:
        """Get random element."""
        return random.choice(self.nums) if self.nums else None

# Test cases
if __name__ == "__main__":
    # Test case 1: Basic operations
    print("Test Case 1: Basic Operations")
    randomizedSet = RandomizedSet()
    
    # Insert 1
    result1 = randomizedSet.insert(1)
    print(f"insert(1): {result1}")  # Expected: True
    
    # Remove 2 (doesn't exist)
    result2 = randomizedSet.remove(2)
    print(f"remove(2): {result2}")  # Expected: False
    
    # Insert 2
    result3 = randomizedSet.insert(2)
    print(f"insert(2): {result3}")  # Expected: True
    
    # Get random element
    result4 = randomizedSet.getRandom()
    print(f"getRandom(): {result4}")  # Expected: 1 or 2
    
    # Remove 1
    result5 = randomizedSet.remove(1)
    print(f"remove(1): {result5}")  # Expected: True
    
    # Insert 2 (already exists)
    result6 = randomizedSet.insert(2)
    print(f"insert(2): {result6}")  # Expected: False
    
    # Get random element
    result7 = randomizedSet.getRandom()
    print(f"getRandom(): {result7}")  # Expected: 2
    print()
    
    # Test case 2: Multiple insertions and deletions
    print("Test Case 2: Multiple Operations")
    randomizedSet2 = RandomizedSet()
    
    operations = [
        ("insert", 1, True),
        ("insert", 2, True),
        ("insert", 3, True),
        ("insert", 1, False),  # Duplicate
        ("remove", 2, True),
        ("insert", 2, True),   # Re-insert
        ("getRandom", None, None),  # Should be 1, 2, or 3
        ("remove", 3, True),
        ("remove", 3, False),  # Already removed
        ("getRandom", None, None)   # Should be 1 or 2
    ]
    
    for op, val, expected in operations:
        if op == "insert":
            result = randomizedSet2.insert(val)
            print(f"{op}({val}): {result}" + (" ✓" if result == expected else " ✗"))
        elif op == "remove":
            result = randomizedSet2.remove(val)
            print(f"{op}({val}): {result}" + (" ✓" if result == expected else " ✗"))
        elif op == "getRandom":
            result = randomizedSet2.getRandom()
            print(f"{op}(): {result}" + (" (valid: 1 or 2)" if result in [1, 2] else " (invalid)"))
    print()
    
    # Test case 3: Large number of operations
    print("Test Case 3: Performance Test")
    randomizedSet3 = RandomizedSet()
    
    # Insert 1000 elements
    for i in range(1000):
        randomizedSet3.insert(i)
    
    print(f"After inserting 0-999: size = {len(randomizedSet3.nums)}")
    
    # Remove 500 elements
    for i in range(0, 1000, 2):  # Remove even numbers
        randomizedSet3.remove(i)
    
    print(f"After removing evens: size = {len(randomizedSet3.nums)}")
    
    # Test getRandom multiple times
    samples = [randomizedSet3.getRandom() for _ in range(10)]
    print(f"10 random samples: {samples}")
    print(f"All samples in range [0,999]: {all(0 <= x < 1000 for x in samples)}")
    print()
    
    # Test case 4: Empty set behavior
    print("Test Case 4: Empty Set")
    empty_set = RandomizedSet()
    print(f"insert(5) on empty set: {empty_set.insert(5)}")  # Expected: True
    print(f"getRandom() after insert: {empty_set.getRandom()}")  # Expected: 5
    print(f"remove(5): {empty_set.remove(5)}")  # Expected: True
    print(f"remove(5) again: {empty_set.remove(5)}")  # Expected: False
    print(f"getRandom() on empty set: {empty_set.getRandom()}")  # Expected: None (or error in real implementation)