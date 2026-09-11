"""
LeetCode #207: Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you 
must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Time Complexity: O(V + E) - where V is number of courses, E is number of prerequisites
Space Complexity: O(V + E) - for adjacency list and visited tracking
"""

from typing import List
from collections import deque, defaultdict

def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determine if all courses can be finished using topological sort (Kahn's algorithm).
    
    Args:
        numCourses: Total number of courses
        prerequisites: List of prerequisite pairs [course, prerequisite]
        
    Returns:
        True if all courses can be finished, False if there's a cycle
    """
    # Build adjacency list and in-degree count
    adj_list = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
        in_degree[course] += 1
    
    # Initialize queue with courses having no prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    courses_taken = 0
    
    # Process courses in topological order
    while queue:
        course = queue.popleft()
        courses_taken += 1
        
        # Reduce in-degree for all dependent courses
        for dependent in adj_list[course]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    # If we took all courses, no cycle exists
    return courses_taken == numCourses

# Alternative approach using DFS with cycle detection
def can_finish_dfs(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determine if all courses can be finished using DFS cycle detection.
    
    Args:
        numCourses: Total number of courses
        prerequisites: List of prerequisite pairs [course, prerequisite]
        
    Returns:
        True if all courses can be finished, False if there's a cycle
    """
    # Build adjacency list
    adj_list = defaultdict(list)
    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
    
    # 0 = unvisited, 1 = visiting (in current path), 2 = visited
    visited = [0] * numCourses
    
    def has_cycle(course: int) -> bool:
        if visited[course] == 1:  # Currently in path -> cycle detected
            return True
        if visited[course] == 2:  # Already processed -> no cycle from this node
            return False
        
        visited[course] = 1  # Mark as visiting
        
        # Check all neighbors for cycles
        for neighbor in adj_list[course]:
            if has_cycle(neighbor):
                return True
        
        visited[course] = 2  # Mark as visited
        return False
    
    # Check for cycles starting from each course
    for course in range(numCourses):
        if visited[course] == 0:  # Unvisited
            if has_cycle(course):
                return False
    
    return True

# Test cases
if __name__ == "__main__":
    # Test case 1: numCourses = 2, prerequisites = [[1,0]] -> True
    # To take course 1 you should have finished course 0. So it's possible.
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print(f"Input: numCourses = {numCourses1}, prerequisites = {prerequisites1}")
    print(f"Output (BFS): {can_finish(numCourses1, prerequisites1)}")  # Expected: True
    print(f"Output (DFS): {can_finish_dfs(numCourses1, prerequisites1)}")  # Expected: True
    print()
    
    # Test case 2: numCourses = 2, prerequisites = [[1,0],[0,1]] -> False
    # To take course 1 you should have finished course 0, and to take course 0 you should
    # also have finished course 1. So it's impossible.
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print(f"Input: numCourses = {numCourses2}, prerequisites = {prerequisites2}")
    print(f"Output (BFS): {can_finish(numCourses2, prerequisites2)}")  # Expected: False
    print(f"Output (DFS): {can_finish_dfs(numCourses2, prerequisites2)}")  # Expected: False
    print()
    
    # Test case 3: numCourses = 3, prerequisites = [[1,0]] -> True
    numCourses3 = 3
    prerequisites3 = [[1, 0]]
    print(f"Input: numCourses = {numCourses3}, prerequisites = {prerequisites3}")
    print(f"Output (BFS): {can_finish(numCourses3, prerequisites3)}")  # Expected: True
    print(f"Output (DFS): {can_finish_dfs(numCourses3, prerequisites3)}")  # Expected: True
    print()
    
    # Test case 4: numCourses = 1, prerequisites = [] -> True
    numCourses4 = 1
    prerequisites4 = []
    print(f"Input: numCourses = {numCourses4}, prerequisites = {prerequisites4}")
    print(f"Output (BFS): {can_finish(numCourses4, prerequisites4)}")  # Expected: True
    print(f"Output (DFS): {can_finish_dfs(numCourses4, prerequisites4)}")  # Expected: True
    print()
    
    # Test case 5: Complex case with multiple dependencies
    # 0 <- 1 <- 2 <- 3 (linear chain) -> True
    numCourses5 = 4
    prerequisites5 = [[1, 0], [2, 1], [3, 2]]
    print(f"Input: numCourses = {numCourses5}, prerequisites = {prerequisites5}")
    print(f"Output (BFS): {can_finish(numCourses5, prerequisites5)}")  # Expected: True
    print(f"Output (DFS): {can_finish_dfs(numCourses5, prerequisites5)}")  # Expected: True
    print()
    
    # Test case 6: Cycle in middle
    # 0 <- 1 <- 2 -> 0 (cycle) -> False
    numCourses6 = 3
    prerequisites6 = [[1, 0], [2, 1], [0, 2]]
    print(f"Input: numCourses = {numCourses6}, prerequisites = {prerequisites6}")
    print(f"Output (BFS): {can_finish(numCourses6, prerequisites6)}")  # Expected: False
    print(f"Output (DFS): {can_finish_dfs(numCourses6, prerequisites6)}")  # Expected: False