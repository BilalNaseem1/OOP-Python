
## 💡 What is Encapsulation?

> **Encapsulation** = Bundling **data + methods** that work on that data, and **restricting direct access** to the inner workings.

In simple words:

* You **protect the internal state** of an object.
* You **allow interaction only through methods**.

---

## ❌ Example **Without Encapsulation**

Here’s what happens when encapsulation is **not** used:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # Public variable

# Anyone can change it directly
p = Person("Ali", 25)
p.age = -100   # 😱 Invalid age, but no one stopped it!
print(p.age)   # Outputs: -100
```

### 🔴 Problems:

* There's **no control** over how `age` is changed.
* No validation, logging, or protection.
* Anyone can break your class by accident.

---

## ✅ Example **With Encapsulation**

Now let’s fix it using encapsulation:

```python
class Person:
    def __init__(self, name, age):
        self.__name = name          # private
        self.__age = age            # private

    @property
    def age(self):
        return self.__age           # getter

    @age.setter
    def age(self, value):
        if value < 0 or value > 120:
            raise ValueError("Invalid age")
        self.__age = value          # setter

    @property
    def name(self):
        return self.__name
```

### 🔐 Now usage looks clean, but is protected:

```python
p = Person("Ali", 25)

print(p.age)      # ✅ Safe access
p.age = 30        # ✅ Valid
# p.age = -10     # ❌ Will raise error
# print(p.__age)  # ❌ AttributeError: private
```

---

## 🧱 Summary of Key Differences

| Feature                | Without Encapsulation  | With Encapsulation         |
| ---------------------- | ---------------------- | -------------------------- |
| Variable access        | Direct (`p.age = -10`) | Indirect (`p.age = value`) |
| Validation             | ❌ None                 | ✅ Yes, in setter           |
| Internal logic exposed | ✅ Yes                  | ❌ Hidden via methods       |
| Error prevention       | ❌ No protection        | ✅ Controlled logic         |
| OOP principle followed | ❌ No                   | ✅ Yes                      |

---

## 🧁 Think of It Like...

* Without encapsulation: You hand someone your **brain** and say, “Feel free to modify anything inside.”
* With encapsulation: You say, “Ask me through a form. I’ll validate it first.”
