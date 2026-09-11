"""
LeetCode #79: Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells 
are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Time Complexity: O(m * n * 4^L) - where m,n are grid dimensions, L is word length
Space Complexity: O(L) - recursion stack depth (plus O(m*n) for visited tracking in some implementations)
"""

from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    """
    Check if word exists in the grid using backtracking (DFS).
    
    Args:
        board: 2D grid of characters
        word: Word to search for
        
    Returns:
        True if word exists in grid, False otherwise
    """
    if not board or not board[0]:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def dfs(row: int, col: int, index: int) -> bool:
        """
        Depth-first search to find word starting from board[row][col].
        
        Args:
            row: Current row position
            col: Current column position
            index: Current position in word
            
        Returns:
            True if word can be formed from this position, False otherwise
        """
        # Base case: if we've matched all characters
        if index == len(word):
            return True
        
        # Check boundaries and character match
        if (row < 0 or row >= rows or col < 0 or col >= cols or 
            board[row][col] != word[index]):
            return False
        
        # Mark current cell as visited by temporarily changing its value
        temp = board[row][col]
        board[row][col] = '#'  # Use '#' as visited marker
        
        # Explore all 4 adjacent directions
        found = (dfs(row + 1, col, index + 1) or  # Down
                dfs(row - 1, col, index + 1) or  # Up
                dfs(row, col + 1, index + 1) or  # Right
                dfs(row, col - 1, index + 1))    # Left
        
        # Backtrack: restore original value
        board[row][col] = temp
        
        return found
    
    # Try starting from each cell in the grid
    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, 0):
                return True
    
    return False

# Alternative approach with explicit visited set (less space efficient but clearer)
def exist_with_visited(board: List[List[str]], word: str) -> bool:
    """
    Check if word exists using DFS with explicit visited set.
    
    Time Complexity: O(m * n * 4^L)
    Space Complexity: O(m * n) for visited set + O(L) for recursion stack
    """
    if not board or not board[0]:
        return False
    
    rows, cols = len(board), len(board[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def dfs(row: int, col: int, index: int) -> bool:
        if index == len(word):
            return True
        
        if (row < 0 or row >= rows or col < 0 or col >= cols or 
            visited[row][col] or board[row][col] != word[index]):
            return False
        
        visited[row][col] = True
        
        found = (dfs(row + 1, col, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row, col - 1, index + 1))
        
        visited[row][col] = False  # Backtrack
        return found
    
    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, 0):
                return True
    
    return False

# Test cases
if __name__ == "__main__":
    # Test case 1: Basic word search
    print("Test Case 1: Basic Word Search")
    board1 = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word1 = "ABCCED"
    print(f"Board: {board1}")
    print(f"Word: '{word1}'")
    print(f"Output: {exist(board1, word1)}")  # Expected: True
    print()
    
    # Test case 2: Same board, different word
    print("Test Case 2: Same Board, Different Word")
    word2 = "SEE"
    print(f"Board: {board1}")
    print(f"Word: '{word2}'")
    print(f"Output: {exist(board1, word2)}")  # Expected: True
    print()
    
    # Test case 3: Word that doesn't exist
    print("Test Case 3: Non-existent Word")
    word3 = "ABCB"
    print(f"Board: {board1}")
    print(f"Word: '{word3}'")
    print(f"Output: {exist(board1, word3)}")  # Expected: False
    print()
    
    # Test case 4: Single cell board
    print("Test Case 4: Single Cell Board")
    board4 = [['A']]
    word4 = "A"
    print(f"Board: {board4}")
    print(f"Word: '{word4}'")
    print(f"Output: {exist(board4, word4)}")  # Expected: True
    print()
    
    # Test case 5: Single cell, wrong word
    print("Test Case 5: Single Cell, Wrong Word")
    word5 = "B"
    print(f"Board: {board4}")
    print(f"Word: '{word5}'")
    print(f"Output: {exist(board4, word5)}")  # Expected: False
    print()
    
    # Test case 6: 2x2 board
    print("Test Case 6: 2x2 Board")
    board6 = [
        ['A','B'],
        ['C','D']
    ]
    word6 = "ABDC"
    print(f"Board: {board6}")
    print(f"Word: '{word6}'")
    print(f"Output: {exist(board6, word6)}")  # Expected: True (A->B->D->C)
    print()
    
    # Test case 7: Same letter reuse prevention
    print("Test Case 7: Prevent Letter Reuse")
    board7 = [
        ['A','A']
    ]
    word7 = "AAA"
    print(f"Board: {board7}")
    print(f"Word: '{word7}'")
    print(f"Output: {exist(board7, word7)}")  # Expected: False (can't reuse same cell)
    print()
    
    # Test case 8: Empty word
    print("Test Case 8: Empty Word")
    board8 = [['A','B'],['C','D']]
    word8 = ""
    print(f"Board: {board8}")
    print(f"Word: '{word8}'")
    print(f"Output: {exist(board8, word8)}")  # Expected: True (empty string always exists)
    print()
    
    # Test case 9: Complex path
    print("Test Case 9: Complex Path")
    board9 = [
        ['A','B','C','E'],
        ['S','F','E','S'],
        ['A','D','E','E']
    ]
    word9 = "ABCESEEEFS"
    print(f"Board: {board9}")
    print(f"Word: '{word9}'")
    print(f"Output: {exist(board9, word9)}")  # Expected: True