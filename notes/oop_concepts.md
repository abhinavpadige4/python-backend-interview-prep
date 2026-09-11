# Object-Oriented Programming Concepts

## 🏛️ Four Pillars of OOP

### 1. Encapsulation
**Definition**: Bundling data and methods that operate on that data within a single unit (class), and restricting access to some of the object's components.

**Python Implementation**:
```python
class BankAccount:
    def __init__(self, __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute (name mangling)
        self._transaction_log = []        # Protected attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_log.append(f"Deposited: {amount}")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_log.append(f"Withdrew: {amount}")
            return True
        return False
    
    def get_balance(self):
        return self.__balance  # Controlled access to private data
    
    # Property for controlled access
    @property
    def balance(self):
        return self.__balance
```

**Benefits**:
- Data hiding and protection
- Reduced complexity through interface separation
- Easier maintenance and modification

### 2. Abstraction
**Definition**: Hiding complex implementation details and showing only essential features to the user.

**Python Implementation**:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
```

**Benefits**:
- Reduced complexity and increased usability
- Avoids code duplication
- Increases reusability
- Improves maintainability

### 3. Inheritance
**Definition**: Mechanism where a new class derives properties and behaviors from an existing class.

**Types of Inheritance**:
```python
# Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Multiple Inheritance
class Flyable:
    def fly(self):
        return "Flying!"

class Swimmable:
    def swim(self):
        return "Swimming!"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return "Quack!"

# Multilevel Inheritance
class Mammal(Animal):
    def warm_blooded(self):
        return True

class Bat(Mammal, Flyable):
    pass
```

**Key Concepts**:
- **super()**: Call parent class methods
- **Method Overriding**: Redefine parent method in child
- **Method Overloading**: Not natively supported (use default args or *args/**kwargs)
- **MRO (Method Resolution Order)**: How Python resolves method calls in inheritance hierarchy

### 4. Polymorphism
**Definition**: Ability of objects of different types to respond to the same method call.

**Types**:
- **Compile-time (Static)**: Method overloading (not in Python)
- **Runtime (Dynamic)**: Method overriding, duck typing

**Python Implementation**:
```python
# Duck Typing - "If it walks like a duck and quacks like a duck, it's a duck"
def make_it_speak(animal):
    return animal.speak()  # Works if animal has speak() method

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep boop!"

# All work with make_it_speak function
print(make_it_speak(Dog()))   # Woof!
print(make_it_speak(Cat()))   # Meow!
print(make_it_speak(Robot())) # Beep boop!
```

## 🔑 Key OOP Principles

### SOLID Principles
1. **S**ingle Responsibility Principle: A class should have only one reason to change
2. **O**pen/Closed Principle: Open for extension, closed for modification
3. **L**iskov Substitution Principle: Subtypes must be substitutable for their base types
4. **I**nterface Segregation Principle: Clients shouldn't depend on interfaces they don't use
5. **D**ependency Inversion Principle: Depend on abstractions, not concretions

### DRY (Don't Repeat Yourself)
- Avoid code duplication through inheritance, composition, and utility functions
- Create reusable components and modules

### KISS (Keep It Simple, Stupid)
- Prefer simple solutions over complex ones
- Don't over-engineer

## 🐍 Python-Specific OOP Features

### Magic Methods (Dunder Methods)
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Equality
    def __eq__(self, other):
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y
    
    # Addition
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Scalar multiplication
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # Length/magnitude
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
    
    # Indexing
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")
    
    # Length
    def __len__(self):
        return 2
    
    # Callable
    def __call__(self):
        return f"Vector at ({self.x}, {self.y})"
```

### Properties
```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
```

### Class Methods and Static Methods
```python
class Employee:
    # Class variable
    employee_count = 0
    raise_amount = 1.04
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    # Instance method
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
    
    # Class method - alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split('-')
        return cls(name, int(salary))
    
    # Class method - modify class variable
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    # Static method - utility function
    @staticmethod
    def is_workday(day):
        return day.weekday() not in (5, 6)  # Monday=0, Sunday=6
```

## 💡 Design Patterns in Python

### Creational Patterns
- **Singleton**: Ensure class has only one instance
- **Factory Method**: Create objects without specifying exact class
- **Abstract Factory**: Create families of related objects
- **Builder**: Construct complex objects step by step
- **Prototype**: Create objects by cloning existing ones

### Structural Patterns
- **Adapter**: Convert interface of a class into another interface clients expect
- **Decorator**: Add responsibilities to objects dynamically
- **Facade**: Provide simplified interface to complex subsystem
- **Proxy**: Provide surrogate or placeholder for another object
- **Flyweight**: Minimize memory usage by sharing data
- **Bridge**: Decouple abstraction from implementation
- **Composite**: Compose objects into tree structures

### Behavioral Patterns
- **Strategy**: Define family of algorithms, encapsulate each one
- **Observer**: Define one-to-many dependency between objects
- **Command**: Encapsulate request as object
- **State**: Allow object to alter behavior when internal state changes
- **Template Method**: Define skeleton of algorithm in operation
- **Iterator**: Provide way to access elements sequentially
- **Memento**: Capture and restore object's internal state
- **Visitor**: Represent operation to be performed on elements

## 🎯 Interview Focus Areas

### Common OOP Interview Questions
1. **Explain the four pillars of OOP** with examples
2. **Difference between abstraction and encapsulation**
3. **When to use composition vs inheritance**
4. **Explain method resolution order (MRO)**
5. **What are decorators and how do they work?**
6. **Difference between @staticmethod and @classmethod**
7. **Explain polymorphism with examples**
8. **How does Python achieve encapsulation without private keywords?**
9. **What is duck typing and why is it important in Python?**
10. **Explain the SOLID principles**

### Coding Problems to Practice
- Design patterns implementation (Singleton, Factory, Observer)
- Inheritance hierarchies (Shapes, Animals, Employees)
- Polymorphism demonstrations
- Encapsulation with properties and private attributes
- Abstract base classes and interfaces
- Class vs instance variables
- Magic methods implementation