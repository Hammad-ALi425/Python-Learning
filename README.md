🐍 Python Basics Repository:

Welcome to this repository!  
This project is designed to help beginners understand the **fundamentals of Python programming** in a simple and easy way.

---

📌 Topics Covered: 

In this repository, the following **Python basics** are covered:

- Variables and Data Types  
- Conditional Statements (if/else)  
- Loops (for and while)
- Strings and Basic String methods 
- Lists and Tuples methods 

---

🔤 Strings in Python

Strings are sequences of characters used to store text.

Example:
```python
name = "Ali"
message = "Hello World"
```

🔤 Python Lists and Tuples

This section covers Python List and Tuple, two of the most commonly used data structures in Python.


## List

A **List** is an ordered, mutable (changeable) collection of items.

**Creating a List**


```python
fruits = ["apple", "banana", "mango"]
```

## Tuple

A Tuple is an ordered, immutable (unchangeable) collection of items.

**Creating a Tuple**
```python
colors = ("red", "green", "blue")
```

## Dictionary

A dictionary in Python is a data structure that stores data in the form of key-value pairs.
Each value is associated with a unique key, which makes data retrieval fast and efficient.

📌 Syntax:
```python
my_dict = {
    "name": "Hammad",
    "age": 20,
    "course": "Python"
}
```

📌 Key Features:

🔑 Data is stored in key-value pairs

⚡ Provides fast data access

🔄 Mutable (can be changed)

❌ Does not allow duplicate keys

# Python Conditional Statements and Loops

A beginner-friendly guide to understanding conditional statements and loops in Python.

---

# 1. Conditional Statements

Conditional statements allow a program to make decisions based on conditions.

## if Statement

Executes a block of code if the condition is `True`.

```python
age = 18

if age >= 18:
    print("Eligible to vote")
```

## if-else Statement

Executes one block if the condition is `True`, otherwise executes another block.

```python
num = 5

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## if-elif-else Ladder

Used when multiple conditions need to be checked.

```python
marks = 75

if marks >= 90:
    print("Grade A")

elif marks >= 80:
    print("Grade B")

elif marks >= 70:
    print("Grade C")

else:
    print("Fail")
```



# 2. Loops

Loops are used to execute a block of code repeatedly.

## for Loop

Used when the number of iterations is known.

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

## range() Function

Syntax:

```python
range(start, stop, step)
```

Example:

```python
for i in range(0, 10, 2):
    print(i)
```

Output:

```text
0
2
4
6
8
```

---

## while Loop

Executes repeatedly while a condition remains `True`.

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output:

```text
1
2
3
4
5
```


