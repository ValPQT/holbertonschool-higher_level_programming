# Python3: Mutable, Immutable… Everything is Object! 🐍

---

## What is an object?

In Python, **everything is an object**. An object is a piece of data stored in memory. Every object has three characteristics:
- an **identity** (its memory address)
- a **type** (what kind of object it is)
- a **value** (the data it holds)

```python
x = 42
print(type(x))   # <class 'int'>
print(id(x))     # memory address, e.g. 140234567891234
print(x)         # value: 42
```

---

## What is the difference between a class and an object or instance?

A **class** is a blueprint or template that defines the structure and behavior of objects.
An **object** (or **instance**) is a concrete realization of that class — it is created from the class and lives in memory.

```python
class Dog:
    def __init__(self, name):
        self.name = name

# Dog is the CLASS (the blueprint)
# rex is an OBJECT / INSTANCE of that class
rex = Dog("Rex")
print(type(rex))  # <class '__main__.Dog'>
```

> 💡 The class is the recipe. The object is the cake.

---

## What is the difference between an immutable object and a mutable object?

| | Mutable | Immutable |
|---|---|---|
| Can be changed after creation? | ✅ Yes | ❌ No |
| `id()` stays the same after modification? | ✅ Yes | ❌ No (new object created) |

```python
# Mutable — same object, modified in place
my_list = [1, 2, 3]
print(id(my_list))  # e.g. 140000000001
my_list.append(4)
print(id(my_list))  # same id ✅

# Immutable — a new object is created
x = "hello"
print(id(x))        # e.g. 140000000002
x += " world"
print(id(x))        # different id ❌ (new string)
```

---

## What is a reference?

A **reference** is a link (pointer) from a variable name to an object in memory. In Python, variables do not store the object itself — they store a **reference** to it.

```python
a = [1, 2, 3]
# 'a' is a reference pointing to the list object in memory
```

Multiple variables can reference the same object:

```python
a = [1, 2, 3]
b = a  # b now references the same object as a
```

---

## What is an assignment?

An **assignment** binds a variable name to an object. It does not copy the object — it creates a new reference pointing to it.

```python
x = 42       # x references the int object 42
name = "Alice"  # name references the string "Alice"

a = [1, 2, 3]
b = a        # b references the SAME list as a (not a copy!)
```

---

## What is an alias?

An **alias** occurs when two or more variables reference the **same object** in memory. Modifying the object through one alias affects all of them.

```python
a = [1, 2, 3]
b = a          # b is an alias of a

b.append(4)
print(a)       # [1, 2, 3, 4] — a is also affected!
print(a is b)  # True — they point to the same object
```

To avoid aliasing, use a copy:

```python
import copy
b = copy.copy(a)    # shallow copy
b = copy.deepcopy(a) # deep copy (for nested objects)
```

---

## How to know if two variables are identical?

Two variables are **identical** if they reference the **exact same object** in memory. Use the `is` operator:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True  — same object
print(a is c)  # False — different objects, same value
```

> ⚠️ `is` checks identity (same object). `==` checks equality (same value).

```python
print(a == c)  # True  — same value
print(a is c)  # False — different objects
```

---

## How to know if two variables are linked to the same object?

Use the `is` operator or compare their `id()` values:

```python
a = [1, 2, 3]
b = a

print(a is b)        # True
print(id(a) == id(b))  # True — same memory address
```

---

## How to display the variable identifier (memory address)?

Use the built-in `id()` function. In CPython, it returns the memory address of the object:

```python
x = 42
print(id(x))        # e.g. 140234567891234

my_list = [1, 2, 3]
print(id(my_list))  # e.g. 140234512345678

# Display in hexadecimal (like C pointers)
print(hex(id(x)))   # e.g. 0x7f8b1c2d3e56
```

---

## What is mutable and immutable?

- **Mutable**: an object whose **value can be changed** after it is created, without changing its identity (`id()`).
- **Immutable**: an object whose **value cannot be changed** after creation. Any "modification" produces a new object with a new `id()`.

```python
# Mutable
lst = [1, 2]
print(id(lst))   # 140000000001
lst[0] = 99
print(id(lst))   # 140000000001 — same object, value changed ✅

# Immutable
s = "hi"
print(id(s))     # 140000000002
s += "!"
print(id(s))     # 140000000099 — new object created ❌
```

---

## What are the built-in mutable types?

| Type | Example |
|------|---------|
| `list` | `[1, 2, 3]` |
| `dict` | `{"key": "value"}` |
| `set` | `{1, 2, 3}` |
| `bytearray` | `bytearray(b"hello")` |

```python
# list
my_list = [1, 2, 3]
my_list.append(4)       # modifies in place ✅

# dict
my_dict = {"a": 1}
my_dict["b"] = 2        # modifies in place ✅

# set
my_set = {1, 2, 3}
my_set.add(4)           # modifies in place ✅
```

---

## What are the built-in immutable types?

| Type | Example |
|------|---------|
| `int` | `42` |
| `float` | `3.14` |
| `str` | `"hello"` |
| `tuple` | `(1, 2, 3)` |
| `bool` | `True`, `False` |
| `frozenset` | `frozenset({1, 2, 3})` |
| `bytes` | `b"hello"` |
| `NoneType` | `None` |

```python
# str — cannot be modified
s = "hello"
# s[0] = "H"  # ❌ TypeError

# tuple — cannot be modified
t = (1, 2, 3)
# t[0] = 99   # ❌ TypeError

# int — n += 1 creates a NEW int
n = 5
print(id(n))   # e.g. 140000000010
n += 1
print(id(n))   # different id — new object ❌
```

---

## How does Python pass variables to functions?

Python uses **"pass by object reference"** (also called "pass by assignment"). The function receives a **reference** to the object — not a copy.

### With immutable objects → the original is never changed

```python
def increment(n):
    n += 1          # creates a new int object locally
    print("Inside:", n)

x = 10
increment(x)
print("Outside:", x)  # 10 — unchanged ✅
```

> Because `int` is immutable, `n += 1` creates a new local object. The original `x` is untouched.

### With mutable objects → the original CAN be changed

```python
def add_item(lst):
    lst.append(99)  # modifies the original object

my_list = [1, 2, 3]
add_item(my_list)
print(my_list)  # [1, 2, 3, 99] ⚠️
```

> Because `list` is mutable, the function modifies the same object in memory.

### Reassignment inside a function does NOT affect the caller

```python
def replace(lst):
    lst = [100, 200]  # creates a new local reference only
    print("Inside:", lst)

my_list = [1, 2, 3]
replace(my_list)
print("Outside:", my_list)  # [1, 2, 3] — unchanged ✅
```

> Reassigning `lst` inside the function only rebinds the local variable. The original reference is unaffected.

---

*#Python #Programming #100DaysOfCode #ALX #SoftwareDevelopment*
