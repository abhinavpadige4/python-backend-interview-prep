"""
LeetCode #206: Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Time Complexity: O(n) - single pass through list
Space Complexity: O(1) - iterative approach uses constant space
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"ListNode({self.val}) -> {self.next}" if self.next else f"ListNode({self.val})"

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list iteratively.
    
    Args:
        head: Head node of the linked list
        
    Returns:
        New head of the reversed linked list
    """
    prev = None
    current = head
    
    while current:
        # Store next node
        next_temp = current.next
        # Reverse current node's pointer
        current.next = prev
        # Move pointers forward
        prev = current
        current = next_temp
    
    return prev

# Recursive approach (O(n) space due to call stack)
def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list recursively.
    
    Args:
        head: Head node of the linked list
        
    Returns:
        New head of the reversed linked list
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverse_list_recursive(head.next)
    # Put first element at the end
    head.next.next = head
    head.next = None
    
    return new_head

# Helper functions for testing
def create_linked_list(values: list) -> Optional[ListNode]:
    """Create a linked list from a list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> list:
    """Convert linked list to Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1: [1,2,3,4,5] -> [5,4,3,2,1]
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed1 = reverse_list(head1)
    print(f"Input: [1,2,3,4,5]")
    print(f"Output: {linked_list_to_list(reversed1)}")  # Expected: [5,4,3,2,1]
    print()
    
    # Test case 2: [1,2] -> [2,1]
    head2 = create_linked_list([1, 2])
    reversed2 = reverse_list(head2)
    print(f"Input: [1,2]")
    print(f"Output: {linked_list_to_list(reversed2)}")  # Expected: [2,1]
    print()
    
    # Test case 3: [] -> []
    head3 = create_linked_list([])
    reversed3 = reverse_list(head3)
    print(f"Input: []")
    print(f"Output: {linked_list_to_list(reversed3)}")  # Expected: []
    print()
    
    # Test case 4: Single node
    head4 = create_linked_list([1])
    reversed4 = reverse_list(head4)
    print(f"Input: [1]")
    print(f"Output: {linked_list_to_list(reversed4)}")  # Expected: [1]