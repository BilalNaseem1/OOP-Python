### 🔹 Understanding **State** and **Behavior** in Object-Oriented Programming (OOP)

In **Object-Oriented Programming (OOP)**, every object has:

1. **State**:

   * It refers to the data or properties that describe the object at a given time.
   * Example: A `LightSwitch` object could have a state like `isOn = True` or `isOn = False`.

2. **Behavior**:

   * It refers to the actions or methods the object can perform.
   * Example: The `LightSwitch` might have behaviors like `turnOn()` and `turnOff()`.

---

### 🔹 The Code You Provided

```python
switchIsOn = False

def turnOn():
    global switchIsOn
    switchIsOn = True

def turnOff():
    global switchIsOn
    switchIsOn = False

print(switchIsOn)     # False
turnOn()
turnOn()
print(switchIsOn)     # True
turnOff()
print(switchIsOn)     # False
```

#### ✅ What's Happening?

* **State**: `switchIsOn` is a global variable that holds the current state of the switch (`True` for ON, `False` for OFF).
* **Behavior**: The functions `turnOn()` and `turnOff()` define how the state can be changed.

---

### 🔹 Output Explanation:

1. Initially, `switchIsOn = False`, so `print(switchIsOn)` prints:

   ```
   False
   ```

2. You call `turnOn()` twice, which sets `switchIsOn = True`, and print:

   ```
   True
   ```

3. You call `turnOff()`, which sets `switchIsOn = False`, and print:

   ```
   False
   ```

---
