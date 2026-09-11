"""
LeetCode #297: Serialize and Deserialize Binary Tree
Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string 
can be deserialized to the original tree structure.

Time Complexity: O(n) - where n is number of nodes
Space Complexity: O(n) - for storage and recursion stack
"""

from typing import Optional, List
import json

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        return f"TreeNode({self.val})"

class Codec:
    """
    Serializes and deserializes binary tree using pre-order traversal with markers for null nodes.
    """
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Encodes a tree to a single string using pre-order traversal.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            String representation of the tree
        """
        def preorder(node):
            if not node:
                return ['None']
            return [str(node.val)] + preorder(node.left) + preorder(node.right)
        
        return ','.join(preorder(root))
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Decodes your encoded data to tree.
        
        Args:
            data: String representation of the tree
            
        Returns:
            Root of the deserialized binary tree
        """
        def build_tree(values):
            val = next(values)
            if val == 'None':
                return None
            node = TreeNode(int(val))
            node.left = build_tree(values)
            node.right = build_tree(values)
            return node
        
        values = iter(data.split(','))
        return build_tree(values)

# Alternative approach using level-order traversal (BFS)
from collections import deque

class CodecBFS:
    """
    Serializes and deserializes binary tree using level-order traversal.
    """
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Encodes a tree to a single string using level-order traversal.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            String representation of the tree
        """
        if not root:
            return ""
        
        queue = deque([root])
        result = []
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")
        
        # Remove trailing None values for cleaner representation
        while result and result[-1] == "None":
            result.pop()
        
        return ','.join(result)
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Decodes your encoded data to tree using level-order traversal.
        
        Args:
            data: String representation of the tree
            
        Returns:
            Root of the deserialized binary tree
        """
        if not data:
            return None
        
        values = data.split(',')
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1
        
        while queue and i < len(values):
            node = queue.popleft()
            
            # Left child
            if i < len(values) and values[i] != "None":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            
            # Right child
            if i < len(values) and values[i] != "None":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        
        return root

# Alternative approach using JSON (more verbose but handles complex data)
class CodecJSON:
    """
    Serializes and deserializes binary tree using JSON format.
    """
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Encodes a tree to a JSON string.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            JSON string representation of the tree
        """
        def tree_to_dict(node):
            if not node:
                return None
            return {
                'val': node.val,
                'left': tree_to_dict(node.left),
                'right': tree_to_dict(node.right)
            }
        
        return json.dumps(tree_to_dict(root))
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Decodes your encoded JSON data to tree.
        
        Args:
            data: JSON string representation of the tree
            
        Returns:
            Root of the deserialized binary tree
        """
        def dict_to_tree(data_dict):
            if not data_dict:
                return None
            node = TreeNode(data_dict['val'])
            node.left = dict_to_tree(data_dict['left'])
            node.right = dict_to_tree(data_dict['right'])
            return node
        
        if not data:
            return None
        
        tree_dict = json.loads(data)
        return dict_to_tree(tree_dict)

# Helper functions for testing
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

def tree_to_list(root: Optional[TreeNode]) -> list:
    """
    Convert binary tree to level-order list for easy comparison.
    
    Args:
        root: Root of the binary tree
        
    Returns:
        List representation of the tree (level-order)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1: [1,2,3,null,null,4,5]
    # Tree:     1
    #          / \
    #         2   3
    #            / \
    #           4   5
    codec = Codec()
    tree1 = create_binary_tree([1, 2, 3, None, None, 4, 5])
    
    print("Test Case 1: [1,2,3,null,null,4,5]")
    serialized = codec.serialize(tree1)
    print(f"Serialized: {serialized}")
    
    deserialized = codec.deserialize(serialized)
    print(f"Deserialized tree: {tree_to_list(deserialized)}")  # Expected: [1,2,3,null,null,4,5]
    print()
    
    # Test case 2: Empty tree
    print("Test Case 2: Empty Tree")
    tree2 = create_binary_tree([])
    serialized2 = codec.serialize(tree2)
    print(f"Serialized: '{serialized2}'")
    
    deserialized2 = codec.deserialize(serialized2)
    print(f"Deserialized tree: {tree_to_list(deserialized2)}")  # Expected: []
    print()
    
    # Test case 3: Single node
    print("Test Case 3: Single Node")
    tree3 = create_binary_tree([1])
    serialized3 = codec.serialize(tree3)
    print(f"Serialized: {serialized3}")
    
    deserialized3 = codec.deserialize(serialized3)
    print(f"Deserialized tree: {tree_to_list(deserialized3)}")  # Expected: [1]
    print()
    
    # Test case 4: Left-skewed tree
    print("Test Case 4: Left-Skewed Tree [1,2,3,4]")
    tree4 = create_binary_tree([1, 2, 3, 4])
    serialized4 = codec.serialize(tree4)
    print(f"Serialized: {serialized4}")
    
    deserialized4 = codec.deserialize(serialized4)
    print(f"Deserialized tree: {tree_to_list(deserialized4)}")  # Expected: [1,2,3,4]
    print()
    
    # Test case 5: Right-skewed tree
    print("Test Case 5: Right-Skewed Tree [1,null,2,null,3]")
    tree5 = create_binary_tree([1, None, 2, None, 3])
    serialized5 = codec.serialize(tree5)
    print(f"Serialized: {serialized5}")
    
    deserialized5 = codec.deserialize(serialized5)
    print(f"Deserialized tree: {tree_to_list(deserialized5)}")  # Expected: [1,null,2,null,3]