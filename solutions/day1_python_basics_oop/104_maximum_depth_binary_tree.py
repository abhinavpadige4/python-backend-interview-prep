"""
LeetCode #104: Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Time Complexity: O(n) - where n is number of nodes
Space Complexity: O(h) - where h is height of tree (recursion stack)
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"TreeNode({self.val})"

def max_depth(root: Optional[TreeNode]) -> int:
    """
    Calculate maximum depth of binary tree using DFS recursion.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        Maximum depth of the tree
    """
    if not root:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return max(left_depth, right_depth) + 1

# Iterative approach using BFS (level order traversal)
from collections import deque

def max_depth_bfs(root: Optional[TreeNode]) -> int:
    """
    Calculate maximum depth using BFS (level order traversal).
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        Maximum depth of the tree
    """
    if not root:
        return 0
    
    queue = deque([root])
    depth = 0
    
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1
    
    return depth

# Helper function for testing
def create_binary_tree(values: list) -> Optional[TreeNode]:
    """
    Create a binary tree from level-order traversal list.
    Uses None for missing nodes.
    
    Args:
        values: List representing level-order traversal
        
    Returns:
        Root of the binary tree
    """
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
if __name__ == "__main__":
    # Test case 1: [3,9,20,null,null,15,7] -> depth 3
    # Tree:     3
    #          / \
    #         9  20
    #            / \
    #           15  7
    tree1 = create_binary_tree([3, 9, 20, None, None, 15, 7])
    print(f"Input: root = [3,9,20,null,null,15,7]")
    print(f"Output (DFS): {max_depth(tree1)}")  # Expected: 3
    print(f"Output (BFS): {max_depth_bfs(tree1)}")  # Expected: 3
    print()
    
    # Test case 2: [1,null,2] -> depth 2
    # Tree:   1
    #          \
    #           2
    tree2 = create_binary_tree([1, None, 2])
    print(f"Input: root = [1,null,2]")
    print(f"Output (DFS): {max_depth(tree2)}")  # Expected: 2
    print(f"Output (BFS): {max_depth_bfs(tree2)}")  # Expected: 2
    print()
    
    # Test case 3: [] -> depth 0
    tree3 = create_binary_tree([])
    print(f"Input: root = []")
    print(f"Output (DFS): {max_depth(tree3)}")  # Expected: 0
    print(f"Output (BFS): {max_depth_bfs(tree3)}")  # Expected: 0
    print()
    
    # Test case 4: [1] -> depth 1
    tree4 = create_binary_tree([1])
    print(f"Input: root = [1]")
    print(f"Output (DFS): {max_depth(tree4)}")  # Expected: 1
    print(f"Output (BFS): {max_depth_bfs(tree4)}")  # Expected: 1