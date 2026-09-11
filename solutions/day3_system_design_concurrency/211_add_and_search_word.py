"""
LeetCode #211: Add and Search Word - Data structure design
Design a data structure that supports adding new words and finding if a string matches 
any previously added string.

Implement the WordDictionary class:
- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string in the data structure that 
  matches word or false otherwise. word may contain dots '.' where dots can be matched 
  with any letter.

Time Complexity: 
- addWord: O(L) where L is length of word
- search: O(L * 26^d) where d is number of dots (worst case)
Space Complexity: O(T * L) where T is number of words, L is average length
"""

class TrieNode:
    """Node in the Trie data structure."""
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end_of_word = False

class WordDictionary:
    """
    WordDictionary using Trie (prefix tree) with DFS for wildcard matching.
    
    Time Complexity:
    - addWord: O(L) where L is word length
    - search: O(L) for exact match, O(L * 26^d) for wildcards where d is dot count
    Space Complexity: O(T * L) where T is number of words, L is average length
    """
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        """
        Adds a word to the data structure.
        
        Args:
            word: Word to add to the dictionary
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the data structure that matches the given word.
        Word may contain dots '.' where dots can be matched with any letter.
        
        Args:
            word: Word to search for (may contain '.')
            
        Returns:
            True if word exists in dictionary, False otherwise
        """
        return self._dfs_search(self.root, word, 0)
    
    def _dfs_search(self, node: TrieNode, word: str, index: int) -> bool:
        """
        Helper method to search for word using DFS (handles wildcards).
        
        Args:
            node: Current TrieNode
            word: Word to search for
            index: Current position in word
            
        Returns:
            True if word found from this node, False otherwise
        """
        if index == len(word):
            return node.is_end_of_word
        
        char = word[index]
        
        if char == '.':
            # Wildcard: try all possible children
            for child in node.children.values():
                if self._dfs_search(child, word, index + 1):
                    return True
            return False
        else:
            # Regular character: check if child exists
            if char not in node.children:
                return False
            return self._dfs_search(node.children[char], word, index + 1)

# Alternative approach using hash set (less efficient for wildcards)
class WordDictionaryHashSet:
    """
    WordDictionary using hash set (simple but inefficient for wildcards).
    
    Time Complexity:
    - addWord: O(1) average
    - search: O(N * L) where N is number of words, L is word length
    Space Complexity: O(T * L) where T is number of words, L is average length
    """
    
    def __init__(self):
        self.words = set()
    
    def addWord(self, word: str) -> None:
        """Add word to hash set."""
        self.words.add(word)
    
    def search(self, word: str) -> bool:
        """Search for word with wildcard support."""
        if '.' not in word:
            return word in self.words
        
        # Handle wildcards by checking all words of same length
        word_len = len(word)
        for candidate in self.words:
            if len(candidate) != word_len:
                continue
            
            match = True
            for i, char in enumerate(word):
                if char != '.' and char != candidate[i]:
                    match = False
                    break
            if match:
                return True
        
        return False

# Alternative approach using Trie without recursion (iterative with stack)
class WordDictionaryIterative:
    """
    WordDictionary using Trie with iterative search (explicit stack).
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        """Add word to Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """Search for word using iterative DFS with stack."""
        stack = [(self.root, 0)]  # (node, index_in_word)
        
        while stack:
            node, index = stack.pop()
            
            if index == len(word):
                if node.is_end_of_word:
                    return True
                continue
            
            char = word[index]
            
            if char == '.':
                # Wildcard: add all children to stack
                for child in node.children.values():
                    stack.append((child, index + 1))
            else:
                # Regular character: check if child exists
                if char in node.children:
                    stack.append((node.children[char], index + 1))
        
        return False

# Test cases
if __name__ == "__main__":
    # Test case 1: Basic functionality
    print("Test Case 1: Basic Operations")
    wordDict = WordDictionary()
    
    wordDict.addWord("bad")
    wordDict.addWord("dad")
    wordDict.addWord("mad")
    
    print(f"search('pad'): {wordDict.search('pad')}")  # Expected: False
    print(f"search('bad'): {wordDict.search('bad')}")  # Expected: True
    print(f"search('.ad'): {wordDict.search('.ad')}")  # Expected: True (matches bad, dad, mad)
    print(f"search('b..'): {wordDict.search('b..')}")  # Expected: True (matches bad)
    print()
    
    # Test case 2: Empty dictionary
    print("Test Case 2: Empty Dictionary")
    wordDict2 = WordDictionary()
    
    print(f"search('a'): {wordDict2.search('a')}")  # Expected: False
    print(f"search('.'): {wordDict2.search('.')}")  # Expected: False
    print(f"search('..'): {wordDict2.search('..')}")  # Expected: False
    print()
    
    # Test case 3: Single character words
    print("Test Case 3: Single Character Words")
    wordDict3 = WordDictionary()
    
    wordDict3.addWord("a")
    wordDict3.addWord("b")
    
    print(f"search('a'): {wordDict3.search('a')}")  # Expected: True
    print(f"search('b'): {wordDict3.search('b')}")  # Expected: True
    print(f"search('c'): {wordDict3.search('c')}")  # Expected: False
    print(f"search('.'): {wordDict3.search('.')}")  # Expected: True (matches a or b)
    print()
    
    # Test case 4: Multiple wildcards
    print("Test Case 4: Multiple Wildcards")
    wordDict4 = WordDictionary()
    
    wordDict4.addWord("abc")
    wordDict4.addWord("def")
    wordDict4.addWord("ghi")
    
    print(f"search('a.c'): {wordDict4.search('a.c')}")  # Expected: True (matches abc)
    print(f"search('..f'): {wordDict4.search('..f')}")  # Expected: True (matches def)
    print(f"search('...'): {wordDict4.search('...')}")  # Expected: True (matches any 3-letter word)
    print(f"search('....'): {wordDict4.search('....')}")  # Expected: False (no 4-letter words)
    print()
    
    # Test case 5: Overlapping prefixes
    print("Test Case 5: Overlapping Prefixes")
    wordDict5 = WordDictionary()
    
    wordDict5.addWord("a")
    wordDict5.addWord("ab")
    wordDict5.addWord("abc")
    wordDict5.addWord("abcd")
    
    print(f"search('a'): {wordDict5.search('a')}")  # Expected: True
    print(f"search('ab'): {wordDict5.search('ab')}")  # Expected: True
    print(f"search('abc'): {wordDict5.search('abc')}")  # Expected: True
    print(f"search('abcd'): {wordDict5.search('abcd')}")  # Expected: True
    print(f"search('abcde'): {wordDict5.search('abcde')}")  # Expected: False
    print(f"search('a.'): {wordDict5.search('a.')}")  # Expected: True (matches ab)
    print(f"search('ab.'): {wordDict5.search('ab.')}")  # Expected: True (matches abc)
    print(f"search('.bc'): {wordDict5.search('.bc')}")  # Expected: True (matches abc)
    print()
    
    # Test case 6: Empty string edge case
    print("Test Case 6: Empty String")
    wordDict6 = WordDictionary()
    
    wordDict6.addWord("")  # Add empty string
    
    print(f"search(''): {wordDict6.search('')}")  # Expected: True
    print(f"search('a'): {wordDict6.search('a')}")  # Expected: False
    print(f"search('.'): {wordDict6.search('.')}")  # Expected: False