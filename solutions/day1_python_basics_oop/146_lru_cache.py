"""
LeetCode #146: LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. 
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds 
  the capacity from this operation, evict the least recently used key.

Time Complexity: O(1) for both get and put operations
Space Complexity: O(capacity) - where capacity is the cache size
"""

from collections import OrderedDict

class LRUCache:
    """
    LRU Cache implementation using OrderedDict (maintains insertion order).
    
    OrderedDict allows O(1) operations for:
    - get: check existence and move to end
    - put: insert/update and move to end, popitem for LRU removal
    """
    
    def __init__(self, capacity: int):
        """
        Initialize LRU cache with given capacity.
        
        Args:
            capacity: Maximum number of items the cache can hold
        """
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        """
        Get value by key, marking it as recently used.
        
        Args:
            key: Key to look up
            
        Returns:
            Value if key exists, -1 otherwise
        """
        if key not in self.cache:
            return -1
        
        # Move accessed item to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        """
        Put key-value pair, evicting LRU item if necessary.
        
        Args:
            key: Key to insert/update
            value: Value to associate with key
        """
        if key in self.cache:
            # Update existing key and move to end
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        # Remove least recently used item if over capacity
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove from beginning (LRU)

# Alternative implementation using doubly linked list + hash map
class Node:
    """Doubly linked list node for LRU cache."""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCacheLinkedList:
    """
    LRU Cache implementation using doubly linked list and hash map.
    
    This demonstrates the underlying mechanism without relying on OrderedDict.
    """
    
    def __init__(self, capacity: int):
        """
        Initialize LRU cache with given capacity.
        
        Args:
            capacity: Maximum number of items the cache can hold
        """
        self.capacity = capacity
        self.cache = {}  # Map key to node
        
        # Dummy head and tail nodes for easier edge case handling
        self.head = Node()  # Most recently used items near head
        self.tail = Node()  # Least recently used items near tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: Node) -> None:
        """Remove node from linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_head(self, node: Node) -> None:
        """Add node right after head (most recently used position)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        """
        Get value by key, marking it as recently used.
        
        Args:
            key: Key to look up
            
        Returns:
            Value if key exists, -1 otherwise
        """
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Move accessed node to head (most recently used)
        self._remove(node)
        self._add_to_head(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """
        Put key-value pair, evicting LRU item if necessary.
        
        Args:
            key: Key to insert/update
            value: Value to associate with key
        """
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            # Move to head (most recently used)
            self._remove(node)
            self._add_to_head(node)
        else:
            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            
            # Evict least recently used if over capacity
            if len(self.cache) > self.capacity:
                # Remove node before tail (LRU item)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

# Test cases
if __name__ == "__main__":
    # Test case 1: Basic LRU cache operations
    print("Test Case 1: Basic Operations")
    cache = LRUCache(2)  # Capacity 2
    
    cache.put(1, 1)
    cache.put(2, 2)
    print(f"get(1): {cache.get(1)}")  # Returns 1
    cache.put(3, 3)  # Evicts key 2
    print(f"get(2): {cache.get(2)}")  # Returns -1 (not found)
    cache.put(4, 4)  # Evicts key 1
    print(f"get(1): {cache.get(1)}")  # Returns -1 (not found)
    print(f"get(3): {cache.get(3)}")  # Returns 3
    print(f"get(4): {cache.get(4)}")  # Returns 4
    print()
    
    # Test case 2: Update existing key
    print("Test Case 2: Update Existing Key")
    cache2 = LRUCache(2)
    
    cache2.put(2, 1)
    cache2.put(2, 2)  # Update existing key
    print(f"get(2): {cache2.get(2)}")  # Returns 2
    cache2.put(1, 1)
    cache2.put(3, 3)  # Evicts key 2
    print(f"get(2): {cache2.get(2)}")  # Returns -1 (evicted)
    print()
    
    # Test case 3: Single capacity cache
    print("Test Case 3: Single Capacity")
    cache3 = LRUCache(1)
    
    cache3.put(2, 1)
    print(f"get(2): {cache3.get(2)}")  # Returns 1
    cache3.put(3, 2)  # Evicts key 2
    print(f"get(2): {cache3.get(2)}")  # Returns -1 (evicted)
    print(f"get(3): {cache3.get(3)}")  # Returns 2