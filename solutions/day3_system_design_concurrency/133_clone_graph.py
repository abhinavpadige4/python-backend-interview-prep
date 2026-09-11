"""
LeetCode #133: Clone Graph
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Time Complexity: O(V + E) - where V is number of vertices, E is number of edges
Space Complexity: O(V) - for hash map storing cloned nodes and recursion stack/queue
"""

from typing import Optional, List
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def __str__(self):
        neighbor_vals = [n.val for n in self.neighbors] if self.neighbors else []
        return f"Node({self.val}, neighbors={neighbor_vals})"

class Solution:
    """
    Clone graph using BFS or DFS with hash map to track original -> cloned node mapping.
    """
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clone a connected undirected graph using BFS.
        
        Args:
            node: Reference node in the graph to clone
            
        Returns:
            Reference node of the cloned graph
        """
        if not node:
            return None
        
        # Hash map to store original node -> cloned node mapping
        old_to_new = {}
        
        # Initialize BFS
        queue = deque([node])
        old_to_new[node] = Node(node.val)  # Clone the root node
        
        while queue:
            curr = queue.popleft()
            
            # Iterate through all neighbors of the current node
            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    # Clone the neighbor and add to queue for processing
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # Add the cloned neighbor to current cloned node's neighbors
                old_to_new[curr].neighbors.append(old_to_new[neighbor])
        
        return old_to_new[node]

# Alternative approach using DFS (recursive)
class SolutionDFS:
    """
    Clone graph using DFS recursion.
    """
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clone a connected undirected graph using DFS.
        
        Args:
            node: Reference node in the graph to clone
            
        Returns:
            Reference node of the cloned graph
        """
        if not node:
            return None
        
        # Hash map to store original node -> cloned node mapping
        old_to_new = {}
        
        def dfs_clone(original_node: 'Node') -> 'Node':
            if original_node in old_to_new:
                return old_to_new[original_node]
            
            # Clone the current node
            clone_node = Node(original_node.val)
            old_to_new[original_node] = clone_node
            
            # Recursively clone all neighbors
            for neighbor in original_node.neighbors:
                clone_node.neighbors.append(dfs_clone(neighbor))
            
            return clone_node
        
        return dfs_clone(node)

# Alternative approach using DFS (iterative)
class SolutionDFSIterative:
    """
    Clone graph using iterative DFS with stack.
    """
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clone a connected undirected graph using iterative DFS.
        
        Args:
            node: Reference node in the graph to clone
            
        Returns:
            Reference node of the cloned graph
        """
        if not node:
            return None
        
        # Hash map to store original node -> cloned node mapping
        old_to_new = {}
        
        # Initialize stack
        stack = [node]
        old_to_new[node] = Node(node.val)  # Clone the root node
        
        while stack:
            curr = stack.pop()
            
            # Iterate through all neighbors of the current node
            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    # Clone the neighbor and add to stack for processing
                    old_to_new[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                
                # Add the cloned neighbor to current cloned node's neighbors
                old_to_new[curr].neighbors.append(old_to_new[neighbor])
        
        return old_to_new[node]

# Helper functions for testing
def create_graph_from_adjacency_list(adj_list: List[List[int]]) -> Optional[Node]:
    """
    Create a graph from adjacency list representation.
    
    Args:
        adj_list: Adjacency list where adj_list[i] contains neighbors of node (i+1)
        
    Returns:
        Reference to first node in the graph
    """
    if not adj_list:
        return None
    
    # Create all nodes
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    
    # Set up neighbors based on adjacency list
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[n - 1] for n in neighbors]  # Convert to 0-indexed
    
    return nodes[0] if nodes else None

def graph_to_adjacency_list(node: Optional[Node]) -> List[List[int]]:
    """
    Convert graph to adjacency list representation for easy comparison.
    
    Args:
        node: Reference node in the graph
        
    Returns:
        Adjacency list representation
    """
    if not node:
        return []
    
    # BFS to traverse graph and build adjacency list
    visited = set()
    queue = deque([node])
    adj_list = []
    
    while queue:
        curr = queue.popleft()
        if curr in visited:
            continue
        
        visited.add(curr)
        # Ensure adj_list has enough entries
        while len(adj_list) < curr.val:
            adj_list.append([])
        
        # Add neighbors (sorted for consistent output)
        neighbor_vals = sorted([n.val for n in curr.neighbors])
        adj_list[curr.val - 1] = neighbor_vals
        
        # Add unvisited neighbors to queue
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
    
    return adj_list

# Test cases
if __name__ == "__main__":
    # Test case 1: [[2,4],[1,3],[2,4],[1,3]]
    # Graph: 1--2
    #        |  |
    #        4--3
    adj_list1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    print("Test Case 1: [[2,4],[1,3],[2,4],[1,3]]")
    
    solution = Solution()
    original1 = create_graph_from_adjacency_list(adj_list1)
    cloned1 = solution.cloneGraph(original1)
    
    print(f"Original adjacency list: {adj_list1}")
    print(f"Cloned adjacency list: {graph_to_adjacency_list(cloned1)}")
    print(f"Graphs are identical: {graph_to_adjacency_list(original1) == graph_to_adjacency_list(cloned1)}")
    print()
    
    # Test case 2: [[]]
    # Graph: Single node with no neighbors
    adj_list2 = [[]]
    print("Test Case 2: [[]]")
    
    original2 = create_graph_from_adjacency_list(adj_list2)
    cloned2 = solution.cloneGraph(original2)
    
    print(f"Original adjacency list: {adj_list2}")
    print(f"Cloned adjacency list: {graph_to_adjacency_list(cloned2)}")
    print(f"Graphs are identical: {graph_to_adjacency_list(original2) == graph_to_adjacency_list(cloned2)}")
    print()
    
    # Test case 3: []
    # Graph: Empty graph
    adj_list3 = []
    print("Test Case 3: []")
    
    original3 = create_graph_from_adjacency_list(adj_list3)
    cloned3 = solution.cloneGraph(original3)
    
    print(f"Original adjacency list: {adj_list3}")
    print(f"Cloned adjacency list: {graph_to_adjacency_list(cloned3)}")
    print(f"Both are None: {original3 is None and cloned3 is None}")
    print()
    
    # Test case 4: [[2],[1]]
    # Graph: 1--2 (two nodes connected)
    adj_list4 = [[2], [1]]
    print("Test Case 4: [[2],[1]]")
    
    original4 = create_graph_from_adjacency_list(adj_list4)
    cloned4 = solution.cloneGraph(original4)
    
    print(f"Original adjacency list: {adj_list4}")
    print(f"Cloned adjacency list: {graph_to_adjacency_list(cloned4)}")
    print(f"Graphs are identical: {graph_to_adjacency_list(original4) == graph_to_adjacency_list(cloned4)}")
    print()
    
    # Test case 5: Linear chain [[2],[1,3],[2,4],[3]]
    # Graph: 1--2--3--4
    adj_list5 = [[2], [1, 3], [2, 4], [3]]
    print("Test Case 5: [[2],[1,3],[2,4],[3]] (linear chain)")
    
    original5 = create_graph_from_adjacency_list(adj_list5)
    cloned5 = solution.cloneGraph(original5)
    
    print(f"Original adjacency list: {adj_list5}")
    print(f"Cloned adjacency list: {graph_to_adjacency_list(cloned5)}")
    print(f"Graphs are identical: {graph_to_adjacency_list(original5) == graph_to_adjacency_list(cloned5)}")