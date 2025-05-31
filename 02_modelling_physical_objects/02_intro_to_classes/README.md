# Python Classes and Objects Guide

A comprehensive guide to understanding Classes, Objects, and Instantiation in Python.

## Table of Contents
- [Overview](#overview)
- [Classes and Objects](#classes-and-objects)
- [Class Anatomy](#class-anatomy)
- [The `__init__()` Method](#the-__init__-method)
- [Instance Variables and Scope](#instance-variables-and-scope)
- [Functions vs Methods](#functions-vs-methods)
- [Method Calling](#method-calling)
- [Code Organization](#code-organization)
- [Instantiation Process](#instantiation-process)
- [Examples](#examples)

## Overview

This guide covers the fundamental concepts of Object-Oriented Programming (OOP) in Python, focusing on classes, objects, and the instantiation process.

## Classes and Objects

### Class
A **blueprint** or template for creating objects that defines:
- **Data/State**: Instance variables (e.g., `self.switchIsOn`)
- **Behavior**: Methods (e.g., `turnOn()`, `turnOff()`)

### Object / Instance
A **specific copy** of a class created through instantiation.

```python
# Creating an object from a class
oLightSwitch = LightSwitch()  # oLightSwitch is an instance
```

## Class Anatomy

### Basic Syntax Structure

```python
class ClassName():
    def __init__(self, optional_params):
        # Initialize instance variables
        pass

    def method1(self, optional_params):
        # Method implementation
        pass

    def methodN(self, optional_params):
        # Method implementation
        pass
```

### Key Requirements
- Class names use **CamelCase** convention
- All methods must be indented under the class
- All methods must include `self` as the first parameter
- Instance variables are accessed using `self.variableName`

## The `__init__()` Method

The special initialization method that runs automatically when an object is created.

### Purpose
- Initialize instance variables
- Set up the initial state of the object
- Not strictly required but highly recommended

### Example

```python
class MyClass:
    def __init__(self):
        self.count = 0
        self.name = "Default"
```

## Instance Variables and Scope

### Instance Variables
- Declared using `self.variableName`
- Have **object scope**: accessible in all methods of the class
- Each object instance has its own copy

### Example

```python
class Counter:
    def __init__(self):
        self.count = 0  # Instance variable
    
    def increment(self):
        self.count = self.count + 1  # Accessing instance variable
```

## Functions vs Methods

| Feature | Function | Method |
|---------|----------|---------|
| **Scope** | Global or local | Class/object |
| **Parameters** | As required | First parameter is `self` |
| **Access** | Cannot access object state | Can access instance variables |

## Method Calling

### Syntax
```python
objectName.methodName(arguments)
```

### Example
```python
oLightSwitch = LightSwitch()
oLightSwitch.turnOn()  # Call method
print(oLightSwitch.switchIsOn)  # Access instance variable
```

## Code Organization

Classes can be organized in two ways:

1. **Same File**: Define class in the same file as the main program
2. **Separate File**: Place class in separate file and import using `import`

**Important**: Class definitions must appear **before** they are used (instantiated).

## Instantiation Process

The step-by-step process when creating an object:

1. `oLightSwitch = LightSwitch()` triggers object creation
2. Python allocates memory space for the new object
3. `__init__()` method runs automatically, with the new object passed as `self`
4. Instance variables are initialized
5. The completed object is returned
6. Object reference is assigned to the variable

## Examples

### Complete LightSwitch Class

```python
class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def show(self):
        print(f"Switch is {'ON' if self.switchIsOn else 'OFF'}")

# Usage
oLightSwitch = LightSwitch()
oLightSwitch.show()        # Switch is OFF
oLightSwitch.turnOn()
oLightSwitch.show()        # Switch is ON
```

### Counter Class Example

```python
class Counter:
    def __init__(self, start_value=0):
        self.count = start_value

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def get_count(self):
        return self.count

    def reset(self):
        self.count = 0

# Usage
counter1 = Counter()        # Starts at 0
counter2 = Counter(10)      # Starts at 10

counter1.increment()
print(counter1.get_count()) # 1

counter2.increment()
print(counter2.get_count()) # 11
```

## Key Takeaways

- Classes are blueprints; objects are instances
- `self` refers to the current object instance
- Instance variables belong to individual objects
- Methods can access and modify instance variables
- `__init__()` sets up the initial state of objects
- Each object maintains its own state independently

## Next Steps

- Practice creating your own classes
- Experiment with different types of instance variables
- Try creating multiple objects from the same class
- Explore class inheritance and advanced OOP concepts