# Python Fundamentals for Backend Interviews

## 🐍 Core Python Concepts

### Data Types & Structures
- **Primitive Types**: int, float, bool, str, None
- **Collections**: list, tuple, dict, set
- **Special Types**: bytes, bytearray, range

### Control Flow
- **Conditionals**: if/elif/else, ternary operator (`x if condition else y`)
- **Loops**: for, while, break, continue, else clauses
- **Comprehensions**: list, dict, set, generator expressions

### Functions
- **Definition**: `def func_name(params):`
- **Arguments**: positional, keyword, default, *args, **kwargs
- **Return**: return statement, multiple returns (tuples)
- **Scope**: LEGB rule (Local, Enclosing, Global, Built-in)
- **Lambda**: anonymous functions `lambda x: x*2`

### Object-Oriented Programming
- **Classes**: `class ClassName:`
- **Attributes**: instance (`self.attr`), class (`ClassName.attr`)
- **Methods**: instance, classmethod (`@classmethod`), staticmethod (`@staticmethod`)
- **Inheritance**: `class Child(Parent):`
- **Polymorphism**: method overriding, duck typing
- **Encapsulation**: `_protected`, `__private` (name mangling)
- **Magic Methods**: `__init__`, `__str__`, `__repr__`, `__len__`, `__getitem__`, `__setitem__`, `__call__`, `__enter__`, `__exit__`

### Advanced Features
- **Decorators**: `@decorator`, `@property`, `@staticmethod`, `@classmethod`
- **Generators**: `yield`, `yield from`, generator expressions
- **Iterators**: `__iter__`, `__next__`, `iter()`, `next()`
- **Context Managers**: `with` statement, `__enter__`, `__exit__`
- **Exceptions**: try/except/else/finally, raise, custom exceptions
- **Modules**: import, from, __name__ == "__main__", packages
- **File I/O**: open(), read(), write(), with statement

## 🔧 Python Best Practices

### PEP 8 Style Guide
- **Indentation**: 4 spaces per level
- **Line Length**: 79 characters recommended
- **Naming**: snake_case for variables/functions, UPPER_CASE for constants, PascalCase for classes
- **Imports**: standard library, third-party, local (separated by blank lines)
- **Whitespace**: around operators, after commas, around colons in dicts

### Performance Considerations
- **String Building**: use `join()` instead of `+` in loops
- **Membership Testing**: use `set` for O(1) lookups vs `list` O(n)
- **Pre-allocation**: know size when possible for lists
- **Built-in Functions**: prefer `sum()`, `max()`, `min()` over manual loops
- **List Methods**: `append()` vs `insert(0, item)` for performance

### Testing & Debugging
- **Assertions**: `assert condition, "message"`
- **Logging**: `logging` module vs `print()`
- **Debugging**: `pdb`, breakpoints, logging
- **Unit Testing**: `unittest`, `pytest` frameworks

## 📚 Common Interview Topics

### String Manipulation
- **Formatting**: f-strings, `.format()`, `%` formatting
- **Methods**: `split()`, `join()`, `strip()`, `replace()`, `find()`
- **Encoding/Decoding**: UTF-8, ASCII, base64
- **Regex**: `re` module for pattern matching

### Collections Deep Dive
- **List**: dynamic array, amortized O(1) append
- **Dict**: hash table, O(1) average lookup/insert
- **Set**: hash table, O(1) average membership test
- **Tuple**: immutable, hashable, memory efficient
- **Collections Module**: Counter, defaultdict, OrderedDict, namedtuple, deque

### Functional Programming
- **Higher-order Functions**: map(), filter(), reduce()
- **Lambda Functions**: anonymous functions for short operations
- **Itertools**: product, permutations, combinations, groupby
- **Functools**: partial, lru_cache, wraps

## 💡 Python Idioms & Patterns

### Common Patterns
- **Swapping**: `a, b = b, a`
- **Enumerate**: `for i, val in enumerate(iterable):`
- **Zip**: `for a, b in zip(list1, list2):`
- **Dict Comprehension**: `{k: v for k, v in items if condition}`
- **Set Comprehension**: `{x for x in iterable if condition}`
- **Generator Expression**: `(x*2 for x in iterable if condition)`

### Resource Management
- **Context Managers**: `with open() as f:`, `with lock:`
- **Try-Finally**: guaranteed cleanup
- **With Statement**: automatic resource management

### Concurrency Basics
- **Threading**: `threading` module for I/O-bound tasks
- **Multiprocessing**: `multiprocessing` module for CPU-bound tasks
- **AsyncIO**: `asyncio` for asynchronous I/O
- **GIL**: Global Interpreter Lock implications

## 🎯 Interview Tips

### Problem Solving Approach
1. **Clarify Requirements**: Ask questions about constraints, edge cases
2. **Examples**: Work through examples manually
3. **Brute Force**: Start with naive solution, then optimize
4. **Optimize**: Look for patterns, data structures, algorithms
5. **Code**: Write clean, readable code with comments
6. **Test**: Test with normal cases, edge cases, empty inputs
7. **Analyze**: Discuss time/space complexity

### Python-Specific Tips
- **Use Built-ins**: `sorted()`, `reversed()`, `enumerate()`, `zip()`
- **Prefer Iterators**: over indexing when possible
- **Leverage Libraries**: `collections`, `heapq`, `bisect`, `itertools`
- **Idiomatic Code**: write Pythonic code, not translated from other languages
- **Edge Cases**: empty inputs, single elements, duplicates, negatives