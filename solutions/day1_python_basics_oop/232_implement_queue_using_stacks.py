"""
LeetCode #232: Implement Queue using Stacks
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue 
(push, peek, pop, and empty).

Time Complexity: 
- push: O(1) amortized
- pop/peek: O(1) amortized
- empty: O(1)
Space Complexity: O(n) - where n is number of elements
"""

class MyQueue:
    """
    Queue implementation using two stacks.
    
    Stack 1: Used for pushing elements
    Stack 2: Used for popping/peeking elements (reversed order)
    """
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []  # For push operations
        self.stack2 = []  # For pop/peek operations
    
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        Time Complexity: O(1)
        """
        self.stack1.append(x)
    
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        Time Complexity: O(1) amortized
        """
        self.peek()  # Ensure stack2 has elements if needed
        return self.stack2.pop()
    
    def peek(self) -> int:
        """
        Get the front element.
        Time Complexity: O(1) amortized
        """
        if not self.stack2:
            # Transfer all elements from stack1 to stack2 (reverses order)
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        Time Complexity: O(1)
        """
        return not self.stack1 and not self.stack2

# Alternative implementation with different complexity trade-offs
class MyQueueAlternative:
    """
    Alternative queue implementation where push is O(n) and pop/peek are O(1).
    """
    
    def __init__(self):
        self.stack1 = []  # Main stack
        self.stack2 = []  # Temporary stack
    
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        Time Complexity: O(n) - need to reverse stack
        """
        # Move all elements to stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        # Push new element
        self.stack1.append(x)
        
        # Move elements back to stack1
        while self.stack2:
            self.stack1.append(self.stack2.pop())
    
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        Time Complexity: O(1)
        """
        return self.stack1.pop()
    
    def peek(self) -> int:
        """
        Get the front element.
        Time Complexity: O(1)
        """
        return self.stack1[-1]
    
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        Time Complexity: O(1)
        """
        return not self.stack1

# Test cases
if __name__ == "__main__":
    # Test case 1: Basic queue operations
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(f"Peek: {obj.peek()}")  # Expected: 1
    print(f"Pop: {obj.pop()}")    # Expected: 1
    print(f"Empty: {obj.empty()}") # Expected: False
    print()
    
    # Test case 2: Multiple operations
    obj2 = MyQueue()
    operations = [
        ("push", 1),
        ("push", 2),
        ("push", 3),
        ("peek", None),
        ("pop", None),
        ("push", 4),
        ("pop", None),
        ("peek", None),
        ("pop", None),
        ("empty", None)
    ]
    
    print("Test case 2: Multiple operations")
    for op, val in operations:
        if op == "push":
            obj2.push(val)
            print(f"push({val})")
        elif op == "pop":
            result = obj2.pop()
            print(f"pop() -> {result}")
        elif op == "peek":
            result = obj2.peek()
            print(f"peek() -> {result}")
        elif op == "empty":
            result = obj2.empty()
            print(f"empty() -> {result}")
    print()
    
    # Test case 3: Empty queue behavior
    obj3 = MyQueue()
    print(f"New queue empty: {obj3.empty()}")  # Expected: True
    try:
        obj3.pop()  # This would raise IndexError in real implementation
    except IndexError:
        print("pop() on empty queue: IndexError (expected)")