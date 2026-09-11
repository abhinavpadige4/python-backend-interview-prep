"""
LeetCode #21: Merge Two Sorted Lists
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Time Complexity: O(n + m) - where n and m are lengths of the two lists
Space Complexity: O(1) - iterative approach
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"ListNode({self.val}) -> {self.next}" if self.next else f"ListNode({self.val})"

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists.
    
    Args:
        list1: Head of first sorted linked list
        list2: Head of second sorted linked list
        
    Returns:
        Head of merged sorted linked list
    """
    # Dummy node to simplify edge cases
    dummy = ListNode()
    current = dummy
    
    # Traverse both lists
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach remaining elements
    current.next = list1 if list1 else list2
    
    return dummy.next

# Recursive approach
def merge_two_lists_recursive(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists recursively.
    
    Args:
        list1: Head of first sorted linked list
        list2: Head of second sorted linked list
        
    Returns:
        Head of merged sorted linked list
    """
    # Base cases
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Recursive case
    if list1.val < list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_recursive(list1, list2.next)
        return list2

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
    # Test case 1: [1,2,4] + [1,3,4] -> [1,1,2,3,4,4]
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = merge_two_lists(list1, list2)
    print(f"Input: list1 = [1,2,4], list2 = [1,3,4]")
    print(f"Output: {linked_list_to_list(merged)}")  # Expected: [1,1,2,3,4,4]
    print()
    
    # Test case 2: [] + [] -> []
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = merge_two_lists(list1, list2)
    print(f"Input: list1 = [], list2 = []")
    print(f"Output: {linked_list_to_list(merged)}")  # Expected: []
    print()
    
    # Test case 3: [] + [0] -> [0]
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = merge_two_lists(list1, list2)
    print(f"Input: list1 = [], list2 = [0]")
    print(f"Output: {linked_list_to_list(merged)}")  # Expected: [0]
    print()
    
    # Test case 4: [5] + [1,2,3] -> [1,2,3,5]
    list1 = create_linked_list([5])
    list2 = create_linked_list([1, 2, 3])
    merged = merge_two_lists(list1, list2)
    print(f"Input: list1 = [5], list2 = [1,2,3]")
    print(f"Output: {linked_list_to_list(merged)}")  # Expected: [1,2,3,5]