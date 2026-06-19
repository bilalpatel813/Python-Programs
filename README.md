# 🐍 Python Complete Developer Guide

> A comprehensive reference covering every core concept a Python developer needs to know — from variables to design patterns.

---

## 📋 Table of Contents

1. [Variables](#1-variables)
2. [Data Types](#2-data-types)
3. [Operators](#3-operators)
4. [Conditions](#4-conditions)
5. [Loops](#5-loops)
6. [Functions](#6-functions)
7. [Lists, Tuples, Sets & Dictionaries](#7-lists-tuples-sets--dictionaries)
8. [Strings](#8-strings)
9. [Classes](#9-classes)
10. [Objects & Constructors (`__init__`)](#10-objects--constructors-__init__)
11. [OOP — 4 Pillars](#11-oop--4-pillars)
12. [Comprehensions](#12-comprehensions)
13. [Decorators](#13-decorators)
14. [Exception Handling](#14-exception-handling)
15. [File Handling](#15-file-handling)
16. [Modules & Packages](#16-modules--packages)
17. [Async/Await](#17-asyncawait)
18. [Database (SQL)](#18-database-sql)
19. [Web Frameworks (Flask/Django)](#19-web-frameworks-flaskdjango)
20. [Design Patterns](#20-design-patterns)

---

## 1. Variables

A **variable** is a name bound to a value. Python is dynamically typed — no type declaration needed.

```python
# Assignment
age = 25
name = "Alice"
is_active = True

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0          # all point to the same value

# Swap without a temp variable
x, y = y, x

# Constants — Python has no true constants; UPPER_CASE is a convention
PI = 3.14159

# Type hints (optional, for clarity/tooling — not enforced at runtime)
age: int = 25
name: str = "Alice"
```

> **Key rule:** Python uses **dynamic typing** — a variable's type can change at runtime, but each value has a fixed type.

---

## 2. Data Types

### Built-in Types

```python
num_int    = 42                # int
num_float  = 3.14              # float
num_complex = 2 + 3j           # complex
text       = "hello"           # str
flag       = True              # bool
nothing    = None              # NoneType

# Checking type
type(42)            # <class 'int'>
isinstance(42, int) # True
```

### Type Conversion

```python
int("42")        # 42
float("3.14")    # 3.14
str(42)          # "42"
bool(0)          # False
bool("")         # False
bool("hello")    # True

# Between collections
list((1, 2, 3))     # [1, 2, 3] — tuple → list
tuple([1, 2, 3])    # (1, 2, 3) — list → tuple
set([1, 2, 2, 3])   # {1, 2, 3} — list → set (dedupes)
```

### Mutable vs Immutable

```python
# Immutable: int, float, str, tuple, bool, frozenset
s = "hello"
# s[0] = "H"        # ❌ TypeError — strings can't be modified in place

# Mutable: list, dict, set
lst = [1, 2, 3]
lst[0] = 99         # ✅ allowed
```

---

## 3. Operators

### Arithmetic

```python
a, b = 10, 3
a + b    # 13
a - b    # 7
a * b    # 30
a / b    # 3.333...  (true division — always returns float)
a // b   # 3         (floor division — rounds down)
a % b    # 1         (modulus / remainder)
a ** b   # 1000       (exponentiation)
```

### Comparison

```python
a == b   a != b   a > b   a < b   a >= b   a <= b
```

### Logical

```python
True and False   # False
True or False     # True
not True          # False
```

### Identity & Membership

```python
x = [1, 2, 3]
y = [1, 2, 3]
x == y    # True  (same VALUE)
x is y    # False (different OBJECT in memory)

3 in [1, 2, 3]      # True (membership test)
"a" in "abc"        # True
```

### Assignment Shortcuts

```python
n = 10
n += 5   # 15
n -= 3   # 12
n *= 2   # 24
n //= 4  # 6
n **= 2  # 36

# Walrus operator (Python 3.8+) — assign within an expression
if (length := len([1, 2, 3])) > 2:
    print(f"List is long: {length}")
```

---

## 4. Conditions

### if / elif / else

```python
score = 75

if score >= 90:
    print("A")
elif score >= 70:
    print("B")     # ← prints this
else:
    print("F")
```

### Ternary (Conditional Expression)

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
```

### match Statement (Python 3.10+) — structural pattern matching

```python
day = "Monday"

match day:
    case "Monday":
        print("Start of week")
    case "Friday":
        print("End of week")
    case _:                    # default case
        print("Midweek")

# Matching with patterns
def handle(command):
    match command.split():
        case ["go", direction]:
            print(f"Going {direction}")
        case ["look"]:
            print("Looking around")
        case _:
            print("Unknown command")
```

### Truthy & Falsy Values

```python
# Falsy: False, 0, 0.0, "", [], {}, (), set(), None
# Everything else is truthy

if []:
    print("never runs")
if [1]:
    print("runs — non-empty list is truthy")
```

---

## 5. Loops

### for Loop — iterate over a sequence

```python
for i in range(5):          # 0,1,2,3,4
    print(i)

for i in range(2, 10, 2):   # start, stop, step → 2,4,6,8
    print(i)

fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):   # with index
    print(index, fruit)
```

### while Loop

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

### Loop Control

```python
for i in range(10):
    if i == 3:
        continue   # skip 3
    if i == 7:
        break      # stop at 7
    print(i)

# else on a loop — runs if loop completes WITHOUT break
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")  # ← this runs
```

---

## 6. Functions

```python
# Basic function
def add(a, b):
    return a + b

# Default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

# *args — variable positional arguments (as a tuple)
def total(*numbers):
    return sum(numbers)
total(1, 2, 3, 4)   # 10

# **kwargs — variable keyword arguments (as a dict)
def print_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30)

# Combining all parameter types
def func(a, b, *args, c=10, **kwargs):
    print(a, b, args, c, kwargs)

# Lambda — anonymous, single-expression function
square = lambda x: x * x
add2 = lambda a, b: a + b
square(5)  # 25

# Type hints
def multiply(a: int, b: int) -> int:
    return a * b

# Keyword-only and positional-only arguments
def func2(pos_only, /, normal, *, kw_only):
    pass
```

### Docstrings

```python
def divide(a, b):
    """Divide a by b and return the result.

    Raises:
        ZeroDivisionError: if b is 0.
    """
    return a / b

print(divide.__doc__)
```

---

## 7. Lists, Tuples, Sets & Dictionaries

### Lists — ordered, mutable

```python
fruits = ["Apple", "Banana", "Cherry"]

fruits.append("Date")        # add to end
fruits.insert(1, "Elder")    # insert at index
fruits.remove("Banana")      # remove by value
fruits.pop()                  # remove & return last item
fruits.pop(0)                 # remove & return item at index

len(fruits)                   # length
fruits[0]                     # access
fruits[-1]                    # last item
fruits[1:3]                   # slicing
fruits.sort()                 # sort in place
fruits.reverse()              # reverse in place
sorted(fruits, reverse=True)  # new sorted list (non-mutating)
```

### Tuples — ordered, immutable

```python
point = (3, 4)
x, y = point          # unpacking
point[0]               # 3
# point[0] = 5         # ❌ TypeError — tuples can't be modified

single = (5,)          # trailing comma required for single-item tuple
```

### Sets — unordered, unique elements

```python
a = {1, 2, 3}
b = {2, 3, 4}

a.add(5)
a.remove(1)

a | b    # union           {2, 3, 4, 5}
a & b    # intersection    {2, 3}
a - b    # difference      {5}
a ^ b    # symmetric diff  {4, 5}
```

### Dictionaries — key/value pairs

```python
person = {"name": "Alice", "age": 30}

person["city"] = "NYC"        # add
person["age"] = 31            # update
del person["city"]            # delete
person.get("age", 0)          # safe access with default
person.pop("age")             # remove & return value

person.keys()      # dict_keys(['name'])
person.values()    # dict_values(['Alice'])
person.items()     # dict_items([('name', 'Alice')])

for key, value in person.items():
    print(f"{key}: {value}")

# Merging (Python 3.9+)
merged = person | {"country": "USA"}
```

---

## 8. Strings

```python
s = "Hello, World!"

s.upper()              # "HELLO, WORLD!"
s.lower()               # "hello, world!"
s.strip()               # remove leading/trailing whitespace
s.replace("Hello", "Hi") # "Hi, World!"
s.split(",")             # ["Hello", " World!"]
",".join(["a", "b", "c"]) # "a,b,c"
s.find("World")           # index of substring (or -1)
s.startswith("Hello")     # True
len(s)                    # 13

# Slicing
s[0:5]      # "Hello"
s[-6:]      # "World!"
s[::-1]     # reversed string

# f-strings (formatted string literals) — preferred way to format
name, age = "Alice", 30
f"{name} is {age} years old"        # "Alice is 30 years old"
f"{3.14159:.2f}"                     # "3.14" (2 decimal places)
f"{name=}"                           # "name='Alice'" (debug formatting)

# .format() and % (older styles)
"{} is {}".format(name, age)
"%s is %d" % (name, age)
```

---

## 9. Classes

```python
class Car:
    # Class variable — shared across ALL instances
    category = "Vehicle"

    def __init__(self, brand, year):
        # Instance variables — unique to each object
        self.brand = brand
        self.year = year

    def start(self):           # instance method (self = the calling object)
        print(f"{self.brand} is starting...")

    @classmethod
    def from_string(cls, car_str):   # alternate constructor
        brand, year = car_str.split("-")
        return cls(brand, int(year))

    @staticmethod
    def get_category():        # doesn't need self or cls
        return "Vehicle"

    def __str__(self):          # string representation (for print())
        return f"{self.year} {self.brand}"

    def __repr__(self):         # representation (for debugging)
        return f"Car('{self.brand}', {self.year})"
```

---

## 10. Objects & Constructors (`__init__`)

```python
# Creating objects (instances)
car1 = Car("Toyota", 2022)
car2 = Car("Honda", 2023)

car1.start()              # Toyota is starting...
print(car1)                # uses __str__ → "2022 Toyota"

# Using alternate constructor
car3 = Car.from_string("BMW-2024")

# Accessing class vs instance variables
print(Car.category)        # "Vehicle" (class-level)
print(car1.category)       # "Vehicle" (inherited from class)
```

### Magic / Dunder Methods

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):           # supports `+`
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):            # supports `==`
        return self.x == other.x and self.y == other.y

    def __len__(self):                  # supports len()
        return 2

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2          # Point(4, 6) via __add__
print(p1 == Point(1, 2))  # True via __eq__
```

---

## 11. OOP — 4 Pillars

---

### 1. Encapsulation — control access using naming conventions

```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance        # "protected" — convention only (single underscore)
        self.__pin = "1234"            # "private" — name-mangled (double underscore)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    @property
    def balance(self):                 # controlled read access
        return self._balance

acc = BankAccount(100)
acc.deposit(50)
print(acc.balance)       # 150 (via property, not direct field access)
# acc.__pin               # ❌ AttributeError (name-mangled to _BankAccount__pin)
```

---

### 2. Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("...")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)         # call parent constructor
        self.breed = breed

    def speak(self):                   # override
        super().speak()                # call parent method
        print(f"{self.name} says Woof!")

dog = Dog("Rex", "Labrador")
dog.speak()    # ... \n Rex says Woof!

# Multiple inheritance
class Swimmer:
    def swim(self): print("Swimming")

class Duck(Animal, Swimmer):           # inherits from both
    pass
```

---

### 3. Polymorphism

```python
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

animals = [Dog("Rex", "Lab"), Cat("Whiskers")]
for animal in animals:
    animal.speak()      # each calls its OWN version of speak()

# Duck typing — Python cares about behavior, not declared type
def make_it_speak(thing):
    thing.speak()        # works for ANY object with a speak() method
```

---

### 4. Abstraction — using the `abc` module

```python
from abc import ABC, abstractmethod

class Shape(ABC):                      # abstract base class
    @abstractmethod
    def area(self):
        pass                             # no implementation — subclasses MUST override

    def display(self):                  # concrete method, shared by all
        print(f"Area: {self.area()}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

c = Circle(5)
c.display()        # Area: 78.53975
# Shape()           # ❌ TypeError — can't instantiate abstract class
```

---

## 12. Comprehensions

```python
# List comprehension
squares = [n ** 2 for n in range(10)]
evens   = [n for n in range(20) if n % 2 == 0]
nested  = [[i * j for j in range(3)] for i in range(3)]

# Dictionary comprehension
squares_dict = {n: n ** 2 for n in range(5)}
filtered = {k: v for k, v in {"a": 1, "b": 2}.items() if v > 1}

# Set comprehension
unique_lengths = {len(word) for word in ["hi", "hello", "hey"]}

# Generator expression — lazy, memory-efficient (use () instead of [])
gen = (n ** 2 for n in range(1000000))   # doesn't compute all at once
next(gen)    # 0
next(gen)    # 1

# Conditional (ternary) inside comprehension
labels = ["even" if n % 2 == 0 else "odd" for n in range(5)]
```

---

## 13. Decorators

A **decorator** wraps a function to extend its behavior without modifying it.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        result = func(*args, **kwargs)
        print("After the function runs")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# Before the function runs
# Hello, Alice!
# After the function runs
```

### Decorators with Arguments

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi!")

greet()   # prints "Hi!" three times
```

### Common Built-in Decorators

```python
class Demo:
    @property                # read-only computed attribute
    def value(self):
        return 42

    @staticmethod             # no self/cls
    def utility(): pass

    @classmethod               # receives the class, not instance
    def create(cls): return cls()

# functools.wraps — preserve original function metadata
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# functools.lru_cache — automatic caching/memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

## 14. Exception Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError) as e:    # multiple exception types
    print(f"Type/Value error: {e}")
except Exception as e:                   # catch-all
    print(f"Unexpected error: {e}")
else:
    print("No errors occurred")          # runs if NO exception raised
finally:
    print("Always runs")                 # cleanup code
```

### Raising Exceptions

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)   # "Age cannot be negative"
```

### Custom Exceptions

```python
class InsufficientFundsError(Exception):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Insufficient funds. Needed: {amount}")

try:
    raise InsufficientFundsError(500)
except InsufficientFundsError as e:
    print(e.amount, str(e))
```

### Common Built-in Exceptions

| Exception              | Cause                                |
|-------------------------|----------------------------------------|
| `ValueError`            | Right type, invalid value             |
| `TypeError`             | Wrong type used in operation          |
| `KeyError`              | Dictionary key not found              |
| `IndexError`            | List index out of range               |
| `FileNotFoundError`     | File doesn't exist                     |
| `ZeroDivisionError`     | Division by zero                       |
| `AttributeError`        | Object has no such attribute/method   |
| `ImportError`           | Module/import failed                   |

### Context Managers (`with`)

```python
# Automatically handles setup/cleanup (e.g., closing files)
with open("data.txt") as f:
    content = f.read()
# file is automatically closed here, even if an error occurs

# Custom context manager
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Elapsed: {self.start}")

with Timer():
    pass
```

---

## 15. File Handling

```python
# Writing
with open("hello.txt", "w") as f:
    f.write("Hello, World!\n")

with open("hello.txt", "a") as f:        # append mode
    f.write("Another line\n")

# Reading
with open("hello.txt", "r") as f:
    content = f.read()                    # entire file as string

with open("hello.txt", "r") as f:
    lines = f.readlines()                 # list of lines

with open("hello.txt", "r") as f:
    for line in f:                        # memory-efficient line-by-line
        print(line.strip())

# File modes: "r" read, "w" write (overwrite), "a" append, "x" create,
#             "b" binary (combine, e.g. "rb")
```

### Working with Paths (`pathlib` — modern approach)

```python
from pathlib import Path

p = Path("data") / "files" / "report.txt"   # cross-platform path joining

p.exists()              # check existence
p.is_file()             # is it a file?
p.parent                # parent directory
p.suffix                # ".txt"
p.stem                  # "report"

p.parent.mkdir(parents=True, exist_ok=True)  # create directories
p.write_text("Hello")                          # quick write
text = p.read_text()                            # quick read

for file in Path(".").glob("*.txt"):           # list matching files
    print(file)
```

### Working with CSV / JSON

```python
import csv, json

# CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 30])

with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# JSON
data = {"name": "Alice", "age": 30}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json") as f:
    loaded = json.load(f)
```

---

## 16. Modules & Packages

```python
# mymodule.py
def add(a, b):
    return a + b

PI = 3.14159

# main.py
import mymodule
mymodule.add(2, 3)

from mymodule import add, PI            # import specific names
from mymodule import add as sum_fn      # rename on import
import mymodule as mm                    # alias the module

# __name__ == "__main__" — only run when executed directly, not imported
if __name__ == "__main__":
    print("Running as script")
```

### Packages — folder with an `__init__.py`

```
myproject/
├── mypackage/
│   ├── __init__.py
│   ├── module_a.py
│   └── module_b.py
└── main.py
```

```python
from mypackage import module_a
from mypackage.module_b import some_function
```

### pip — Python's package manager

```bash
pip install requests
pip install -r requirements.txt
pip freeze > requirements.txt
pip uninstall requests

# Virtual environments (isolate dependencies per project)
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

---

## 17. Async/Await

```python
import asyncio

async def fetch_data():
    print("Fetching...")
    await asyncio.sleep(2)        # non-blocking wait
    print("Done fetching")
    return "data"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
```

### Running Multiple Tasks Concurrently

```python
async def main():
    # Run multiple coroutines concurrently
    results = await asyncio.gather(
        fetch_data(),
        fetch_data(),
        fetch_data(),
    )
    print(results)

asyncio.run(main())
```

### Creating Tasks

```python
async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(fetch_data())

    await task1
    await task2
```

---

## 18. Database (SQL)

### sqlite3 — built-in lightweight database

```python
import sqlite3

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")

# Insert (parameterized — prevents SQL injection)
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
conn.commit()

# Query
cursor.execute("SELECT * FROM users WHERE age > ?", (18,))
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
```

### SQLAlchemy — ORM approach

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///mydb.db")
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id   = Column(Integer, primary_key=True)
    name = Column(String)
    age  = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Insert
new_user = User(name="Bob", age=25)
session.add(new_user)
session.commit()

# Query
users = session.query(User).filter(User.age > 18).all()
for u in users:
    print(u.name, u.age)
```

---

## 19. Web Frameworks (Flask/Django)

### Flask — lightweight micro-framework

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/users/<int:user_id>")
def get_user(user_id):
    return jsonify({"id": user_id, "name": "Alice"})

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

### Django — full-featured framework

```python
# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age  = models.IntegerField()

# views.py
from django.http import JsonResponse
from .models import User

def user_list(request):
    users = User.objects.all().values()
    return JsonResponse(list(users), safe=False)

def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return JsonResponse({"name": user.name, "age": user.age})

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.user_list),
    path("users/<int:user_id>/", views.user_detail),
]
```

```bash
django-admin startproject myproject
python manage.py startapp myapp
python manage.py migrate
python manage.py runserver
```

### FastAPI — modern, async-first framework

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"id": user_id, "name": "Alice"}

@app.post("/users")
async def create_user(user: User):
    return user

# Run with: uvicorn main:app --reload
```

---

## 20. Design Patterns

---

### Singleton

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)   # True
```

### Factory

```python
class ShapeFactory:
    @staticmethod
    def create(shape_type):
        shapes = {
            "circle": Circle,
            "square": Square,
        }
        if shape_type not in shapes:
            raise ValueError(f"Unknown shape: {shape_type}")
        return shapes[shape_type]()

shape = ShapeFactory.create("circle")
```

### Builder

```python
class QueryBuilder:
    def __init__(self):
        self._table = ""
        self._where = ""
        self._limit = 100

    def from_table(self, table):
        self._table = table
        return self

    def where(self, condition):
        self._where = condition
        return self

    def limit(self, n):
        self._limit = n
        return self

    def build(self):
        sql = f"SELECT * FROM {self._table}"
        if self._where:
            sql += f" WHERE {self._where}"
        return sql + f" LIMIT {self._limit}"

query = QueryBuilder().from_table("users").where("age > 18").limit(50).build()
```

### Observer

```python
class EventEmitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event, *args):
        for callback in self._listeners.get(event, []):
            callback(*args)

emitter = EventEmitter()
emitter.on("user_login", lambda user: print(f"{user} logged in"))
emitter.emit("user_login", "Alice")
```

### Strategy

```python
class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy(data)

bubble_sort = lambda data: sorted(data)         # simplified
quick_sort  = lambda data: sorted(data)

sorter = Sorter(bubble_sort)
sorter.sort([3, 1, 2])

sorter.strategy = quick_sort       # swap strategy at runtime
```

### Decorator Pattern (structural, not the `@` syntax)

```python
class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    def cost(self):
        return self._coffee.cost() + 2

coffee = MilkDecorator(Coffee())
print(coffee.cost())   # 7
```

---

## Quick Reference Card

| Concept           | Key Syntax                                          |
|-------------------|------------------------------------------------------|
| Variable          | dynamic typing, no declaration needed                |
| Conditions        | `if`, `elif`, `else`, `match`/`case`                 |
| Loop              | `for`, `while`, `range()`, `enumerate()`             |
| Function          | `def`, `lambda`, `*args`, `**kwargs`                 |
| Collections       | `list`, `tuple`, `set`, `dict`                        |
| OOP               | `class`, `self`, `__init__`, `super()`                |
| Comprehension     | `[x for x in y]`, `{k:v for ...}`                     |
| Decorator         | `@decorator_name`                                     |
| Exceptions        | `try`, `except`, `finally`, `raise`                   |
| File I/O          | `open()`, `with`, `pathlib.Path`                       |
| Modules           | `import`, `from ... import`, `pip`                    |
| Async             | `async def`, `await`, `asyncio.gather()`              |
| Web               | Flask, Django, FastAPI                                |
| Design Patterns   | Singleton, Factory, Builder, Observer, Strategy       |

---
# 👨‍💻 Author

# Bilal Patel

---

# ⭐ Support

If you find this useful:

  - ⭐ Star the repo
  - 🍴 Fork it
  - 📢 Share it

---

# 💡 “Start small, build big with Python.”
