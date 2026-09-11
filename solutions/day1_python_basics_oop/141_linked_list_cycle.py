"""
LeetCode #141: Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.

Time Complexity: O(n) - where n is number of nodes
Space Complexity: O(1) - Floyd's Tortoise and Hare algorithm
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect cycle in linked list using Floyd's Tortoise and Hare algorithm.
    
    Args:
        head: Head node of the linked list
        
    Returns:
        True if cycle exists, False otherwise
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False

# Alternative approach using hash set (O(n) space)
def has_cycle_hashset(head: Optional[ListNode]) -> bool:
    """
    Detect cycle using hash set to track visited nodes.
    
    Args:
        head: Head node of the linked list
        
    Returns:
        True if cycle exists, False otherwise
    """
    visited = set()
    current = head
    
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    
    return False

# Helper functions for testing
def create_linked_list(values: list, pos: int = -1) -> Optional[ListNode]:
    """
    Create a linked list from values, optionally creating a cycle.
    
    Args:
        values: List of node values
        pos: Position to connect tail to (0-indexed), -1 means no cycle
        
    Returns:
        Head of the linked list
    """
    if not values:
        return None
    
    nodes = [ListNode(val) for val in values]
    
    # Connect nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Create cycle if specified
    if pos >= 0 and pos < len(nodes):
        nodes[-1].next = nodes[pos]
    
    return nodes[0] if nodes else None

# Test cases
if __name__ == "__main__":
    # Test case 1: [3,2,0,-4] with cycle at position 1
    head1 = create_linked_list([3, 2, 0, -4], pos=1)
    print(f"Input: head = [3,2,0,-4], pos = 1")
    print(f"Output: {has_cycle(head1)}")  # Expected: True
    print()
    
    # Test case 2: [1,2] with cycle at position 0
    head2 = create_linked_list([1, 2], pos=0)
    print(f"Input: head = [1,2], pos = 0")
    print(f"Output: {has_cycle(head2)}")  # Expected: True
    print()
    
    # Test case 3: [1] with no cycle
    head3 = create_linked_list([1], pos=-1)
    print(f"Input: head = [1], pos = -1")
    print(f"Output: {has_cycle(head3)}")  # Expected: False
    print()
    
    # Test case 4: Empty list
    head4 = create_linked_list([])
    print(f"Input: head = []")
    print(f"Output: {has_cycle(head4)}")  # Expected: False