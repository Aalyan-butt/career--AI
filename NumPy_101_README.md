# 🔢 NumPy 101 — Beginner to Intermediate Tutorial

This guide walks you through the essentials of **NumPy**, the foundation of scientific computing in Python — from creating your first array to broadcasting, linear algebra, and a mini project.

---

## 📦 What Is NumPy?

**NumPy** (**Num**erical **Py**thon) is an open-source library for working with **arrays of numbers** quickly and efficiently. It is the base that libraries like **Pandas, Matplotlib, SciPy, scikit-learn, and TensorFlow** are built on.

The core data structure in NumPy is:

- `ndarray`: an **n-dimensional array** — a grid of values that all share the **same data type**

### ✅ Why use NumPy instead of Python lists?

| Feature | Python List | NumPy Array |
|---|---|---|
| Speed | Slow (loops needed) | Very fast (vectorized, written in C) |
| Memory | Uses more memory | Compact, efficient |
| Math on whole data | Needs a loop | `arr * 2` works directly |
| Data types | Mixed allowed | One type per array |
| Multi-dimensional | Awkward (list of lists) | Built in |

---

## 📚 Table of Contents

1. Installing & Importing
2. Creating Arrays
3. Array Attributes
4. Data Types
5. Indexing & Slicing
6. Modifying Arrays
7. Arithmetic Operations
8. Mathematical Functions
9. Statistics & Aggregations
10. Boolean Masking & Conditions
11. Reshaping Arrays
12. Adding & Removing Elements
13. Joining & Splitting
14. Repeating Arrays
15. Broadcasting
16. Sorting & Searching
17. Set Operations
18. Random Numbers
19. Linear Algebra
20. Missing Values (NaN & Inf)
21. Copy vs View
22. Saving & Loading Data
23. Iterating Over Arrays
24. Other Handy Functions
25. Mini Project — Student Marks Analysis
26. Practice Exercises
27. Cheat Sheet

---

## 💻 1. Installing & Importing

```bash
pip install numpy
```

The universal convention is to import NumPy as `np`:

```python
import numpy as np

print(np.__version__)
```

**Output:**

```
2.4.4
```

---

## 🏗️ 2. Creating Arrays

### 📌 From Python Lists — `np.array()`

```python
a = np.array([1, 2, 3, 4, 5])                 # 1D array (vector)
m = np.array([[1, 2, 3], [4, 5, 6]])          # 2D array (matrix)
t = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])              # 3D array

print(a)
print(m)
print(t)
```

**Output:**

```
[1 2 3 4 5]
[[1 2 3]
 [4 5 6]]
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
```

- A **flat list** → 1D array
- A **list of lists** → 2D array (rows and columns)
- A **list of lists of lists** → 3D array

### 📌 Built-in Array Creators

```python
print(np.zeros((2, 3)))        # all zeros
print(np.ones((2, 2)))         # all ones
print(np.full((2, 3), 9))      # filled with a chosen value
print(np.eye(3))               # identity matrix
print(np.diag([1, 2, 3]))      # diagonal matrix
```

**Output:**

```
[[0. 0. 0.]
 [0. 0. 0.]]
[[1. 1.]
 [1. 1.]]
[[9 9 9]
 [9 9 9]]
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
[[1 0 0]
 [0 2 0]
 [0 0 3]]
```

### 📌 Number Sequences

```python
print(np.arange(0, 10, 2))     # start, stop (excluded), step
print(np.linspace(0, 1, 5))    # 5 evenly spaced numbers (stop included)
print(np.logspace(0, 3, 4))    # 10^0 to 10^3, 4 numbers
```

**Output:**

```
[0 2 4 6 8]
[0.   0.25 0.5  0.75 1.  ]
[   1.   10.  100. 1000.]
```

### 📌 Arrays Shaped Like Another Array

```python
x = np.array([[1, 2], [3, 4]])
print(np.zeros_like(x))
print(np.ones_like(x))
print(np.full_like(x, 5))
```

**Output:**

```
[[0 0]
 [0 0]]
[[1 1]
 [1 1]]
[[5 5]
 [5 5]]
```

| Function | Purpose |
|---|---|
| `np.array(list)` | Convert a list to an array |
| `np.zeros(shape)` | Array of zeros |
| `np.ones(shape)` | Array of ones |
| `np.full(shape, v)` | Array filled with `v` |
| `np.empty(shape)` | Uninitialised array (random leftover values, fast) |
| `np.eye(n)` / `np.identity(n)` | Identity matrix |
| `np.diag(list)` | Diagonal matrix |
| `np.arange(start, stop, step)` | Like `range()`, returns an array |
| `np.linspace(start, stop, n)` | `n` evenly spaced values |
| `np.logspace(a, b, n)` | `n` values spaced on a log scale |
| `np.zeros_like(x)` | Zeros with the same shape/type as `x` |

---

## 🔍 3. Array Attributes

```python
m = np.array([[1, 2, 3], [4, 5, 6]])

print(m.ndim)        # number of dimensions
print(m.shape)       # (rows, columns)
print(m.size)        # total number of elements
print(m.dtype)       # data type of elements
print(m.itemsize)    # bytes per element
print(m.nbytes)      # total bytes
print(len(m))        # length of first dimension
```

**Output:**

```
2
(2, 3)
6
int64
8
48
2
```

| Attribute | Meaning |
|---|---|
| `ndim` | Number of dimensions (axes) |
| `shape` | Tuple of size along each axis — `(2, 3)` = 2 rows, 3 columns |
| `size` | Total number of elements |
| `dtype` | Data type of the elements |
| `itemsize` | Memory (bytes) used by one element |
| `nbytes` | Total memory used by the array |

---

## 🧬 4. Data Types

Every NumPy array holds **one data type**. Common ones: `int8, int16, int32, int64`, `float32, float64`, `bool`, `str_`.

```python
print(np.array([1, 2, 3], dtype=np.float32))     # choose type when creating
print(np.array([1, 0, 2]).astype(bool))          # int -> bool
print(np.array([1.9, 2.7]).astype(int))          # float -> int (cuts decimals)
print(np.array(["1", "2"]).astype(int))          # string -> int
print(np.array([1, "a", 2.5]))                   # mixed -> everything becomes text
```

**Output:**

```
[1. 2. 3.]
[ True False  True]
[1 2]
[1 2]
['1' 'a' '2.5']
```

- `astype()` returns a **new** array with the converted type.
- Converting float → int **truncates** (1.9 becomes 1, it does not round).
- If you mix types in one list, NumPy picks the type that can hold all of them.

---

## 🎯 5. Indexing & Slicing

### 📎 1D Arrays

```python
b = np.array([5, 10, 15, 20, 25, 30])

print(b[0])        # first element
print(b[-1])       # last element
print(b[1:4])      # index 1 up to (not including) 4
print(b[:3])       # first three
print(b[3:])       # from index 3 to the end
print(b[::2])      # every 2nd element
print(b[::-1])     # reversed
```

**Output:**

```
5
30
[10 15 20]
[ 5 10 15]
[20 25 30]
[ 5 15 25]
[30 25 20 15 10  5]
```

Slicing syntax: **`array[start : stop : step]`** — the `stop` index is **excluded**.

### 📎 2D Arrays — `[row, column]`

```python
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(m[1, 2])        # row 1, column 2
print(m[0])           # whole first row
print(m[:, 1])        # whole second column
print(m[0:2, 1:3])    # rows 0-1, columns 1-2
print(m[-1, -1])      # last row, last column
```

**Output:**

```
6
[1 2 3]
[2 5 8]
[[2 3]
 [5 6]]
9
```

A colon `:` on its own means **"all"**.

### 📎 3D Arrays — `[block, row, column]`

```python
t = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])

print(t[1, 0, 1])     # block 1, row 0, column 1
print(t[0])           # entire first block
```

**Output:**

```
6
[[1 2]
 [3 4]]
```

### 📎 Fancy Indexing (using lists of positions)

```python
b = np.array([5, 10, 15, 20, 25, 30])
print(b[[0, 2, 4]])             # pick specific positions

m = np.array([[1, 2, 3], [4, 5, 6]])
print(m[[0, 1], [2, 0]])        # picks m[0,2] and m[1,0]
```

**Output:**

```
[ 5 15 25]
[3 4]
```

---

## ✏️ 6. Modifying Arrays

```python
c = np.array([1, 2, 3, 4, 5])
c[0] = 100            # change one element
c[1:3] = 0            # change a slice
print(c)

grid = np.zeros((3, 3), dtype=int)
grid[1, :] = 5        # fill row 1
grid[:, 2] = 9        # fill column 2
print(grid)
```

**Output:**

```
[100   0   0   4   5]
[[0 0 9]
 [5 5 9]
 [0 0 9]]
```

---

## ➕ 7. Arithmetic Operations

NumPy applies operations **element by element** — no loops needed. This is called **vectorization**.

```python
x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])

print(x + y)       # addition
print(y - x)       # subtraction
print(x * y)       # multiplication
print(y / x)       # division
print(y // 3)      # floor division
print(y % 3)       # remainder
print(x ** 2)      # power
print(x + 100)     # scalar applies to every element
print(-x)          # negation
```

**Output:**

```
[11 22 33 44]
[ 9 18 27 36]
[ 10  40  90 160]
[10. 10. 10. 10.]
[ 3  6 10 13]
[1 2 0 1]
[ 1  4  9 16]
[101 102 103 104]
[-1 -2 -3 -4]
```

### 📌 Equivalent Functions

```python
print(np.add(x, y))
print(np.subtract(y, x))
print(np.multiply(x, y))
print(np.divide(y, x))
print(np.power(x, 3))
print(np.mod(y, 3))
```

**Output:**

```
[11 22 33 44]
[ 9 18 27 36]
[ 10  40  90 160]
[10. 10. 10. 10.]
[ 1  8 27 64]
[1 2 0 1]
```

### 📌 Comparison Operations

```python
print(x > 2)
print(x == np.array([1, 0, 3, 0]))
print(np.array_equal(x, np.array([1, 2, 3, 4])))   # are the arrays identical?
print(np.allclose(0.1 + 0.2, 0.3))                 # equal within tiny tolerance?
```

**Output:**

```
[False False  True  True]
[ True False  True False]
True
True
```

---

## 📐 8. Mathematical Functions

These are called **universal functions (ufuncs)** and work on every element.

```python
print(np.sqrt([1, 4, 9, 16]))          # square root
print(np.cbrt([8, 27]))                # cube root
print(np.abs([-3, 2, -1]))             # absolute value
print(np.exp(1))                       # e^1
print(np.log(10))                      # natural log
print(np.log2(8))                      # log base 2
print(np.log10(1000))                  # log base 10
print(np.sign([-5, 0, 7]))             # -1, 0, or 1
```

**Output:**

```
[1. 2. 3. 4.]
[2. 3.]
[3 2 1]
2.718281828459045
2.302585092994046
3.0
3.0
[-1  0  1]
```

### 📌 Trigonometry

```python
print(np.sin(np.pi / 2))
print(np.cos(0))
print(np.round(np.tan(np.pi / 4), 2))
print(np.degrees(np.pi))               # radians -> degrees
print(np.radians(180))                 # degrees -> radians
```

**Output:**

```
1.0
1.0
1.0
180.0
3.141592653589793
```

### 📌 Rounding

```python
vals = np.array([1.234, 5.678, -2.5, 3.5])

print(np.round(vals, 1))     # round to 1 decimal
print(np.floor(vals))        # round down
print(np.ceil(vals))         # round up
print(np.trunc(vals))        # cut off decimals
print(np.round([-2.5, 2.5, 3.5]))   # exact halves
```

**Output:**

```
[ 1.2  5.7 -2.5  3.5]
[ 1.  5. -3.  3.]
[ 2.  6. -2.  4.]
[ 1.  5. -2.  3.]
[-2.  2.  4.]
```

> 💡 `np.round` rounds exact halves to the **nearest even** number (`-2.5 → -2`, `2.5 → 2`, `3.5 → 4`). This is normal and called "banker's rounding".

---

## 📊 9. Statistics & Aggregations

```python
s = np.array([4, 8, 15, 16, 23, 42])

print(s.sum())            # total
print(s.prod())           # product of all
print(s.mean())           # average
print(np.median(s))       # middle value
print(s.min(), s.max())   # smallest, largest
print(np.ptp(s))          # range (max - min)
print(s.std())            # standard deviation
print(s.var())            # variance
print(s.argmax())         # POSITION of the maximum
print(s.argmin())         # POSITION of the minimum
print(s.cumsum())         # running total
print(np.diff(s))         # difference between neighbours
```

**Output:**

```
108
7418880
18.0
15.5
4 42
38
12.315302134607444
151.66666666666666
5
0
[  4  12  27  43  66 108]
[ 4  7  1  7 19]
```

### 📌 Percentiles & Weighted Average

```python
print(np.percentile(s, 50))             # 50th percentile = median
print(np.percentile(s, [25, 75]))       # quartiles
print(np.average([80, 90], weights=[1, 3]))   # weighted average
```

**Output:**

```
15.5
[ 9.75 21.25]
87.5
```

### 📌 The `axis` Parameter (very important)

```python
g = np.array([[1, 2, 3],
              [4, 5, 6]])

print(g.sum())               # whole array
print(g.sum(axis=0))         # down the columns -> one result per column
print(g.sum(axis=1))         # across the rows  -> one result per row
print(g.mean(axis=0))
print(g.max(axis=1))
print(g.sum(axis=1, keepdims=True))   # keep result as a column
```

**Output:**

```
21
[5 7 9]
[ 6 15]
[2.5 3.5 4.5]
[3 6]
[[ 6]
 [15]]
```

| `axis` | Direction | Result has one value per... |
|---|---|---|
| `None` (default) | Whole array | single number |
| `0` | Vertical (down rows) | column |
| `1` | Horizontal (across columns) | row |

---

## 🧪 10. Boolean Masking & Conditions

### 📌 Filtering with Conditions

```python
marks = np.array([45, 82, 67, 90, 33, 75])

print(marks > 50)                          # True/False for each element
print(marks[marks > 50])                   # keep only the True ones
print(marks[(marks > 50) & (marks < 80)])  # AND
print(marks[(marks < 40) | (marks > 85)])  # OR
print(marks[~(marks > 50)])                # NOT
```

**Output:**

```
[False  True  True  True False  True]
[82 67 90 75]
[67 75]
[90 33]
[45 33]
```

> ⚠️ Use `&`, `|`, `~` (with brackets around each condition) — **not** `and`, `or`, `not`.

### 📌 `np.where` — Vectorized if/else

```python
print(np.where(marks >= 50, "Pass", "Fail"))
print(np.where(marks >= 50, marks, 0))     # keep passing marks, zero the rest
print(np.where(marks > 80))                # positions where condition is True
```

**Output:**

```
['Fail' 'Pass' 'Pass' 'Pass' 'Fail' 'Pass']
[ 0 82 67 90  0 75]
(array([1, 3]),)
```

### 📌 Replacing Values Using a Mask

```python
marks2 = marks.copy()
marks2[marks2 < 40] = 40       # raise anything below 40 to 40
print(marks2)
```

**Output:**

```
[45 82 67 90 40 75]
```

### 📌 `any`, `all`, `count_nonzero`, `clip`, `select`

```python
print(np.any(marks > 80))              # is at least one True?
print(np.all(marks > 30))              # are all True?
print(np.count_nonzero(marks > 50))    # how many True?
print(np.clip(marks, 40, 80))          # limit values between 40 and 80

grade = np.select([marks >= 80, marks >= 50],   # conditions (checked in order)
                  ["A", "B"],                   # matching results
                  default="F")
print(grade)
```

**Output:**

```
True
True
4
[45 80 67 80 40 75]
['F' 'A' 'B' 'A' 'F' 'B']
```

---

## 🔄 11. Reshaping Arrays

```python
r = np.arange(1, 13)
print(r)

print(r.reshape(3, 4))        # 3 rows, 4 columns
print(r.reshape(2, -1))       # -1 = "figure out this size for me"
print(r.reshape(3, 4).T)      # transpose (swap rows and columns)
```

**Output:**

```
[ 1  2  3  4  5  6  7  8  9 10 11 12]
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]]
[[ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]]
```

> 💡 The total number of elements must stay the same: `12 = 3 × 4 = 2 × 6`.

### 📌 Flattening

```python
grid = r.reshape(3, 4)
print(grid.flatten())    # always returns a COPY
print(grid.ravel())      # returns a VIEW when possible (faster)
```

**Output:**

```
[ 1  2  3  4  5  6  7  8  9 10 11 12]
[ 1  2  3  4  5  6  7  8  9 10 11 12]
```

### 📌 Adding / Removing Dimensions

```python
v = np.array([1, 2, 3])
print(v.shape)

col = np.expand_dims(v, axis=1)     # shape (3,) -> (3, 1)
print(col.shape)

row = v[np.newaxis, :]              # shape (3,) -> (1, 3)
print(row.shape)

print(np.squeeze(col).shape)        # remove size-1 dimensions
```

**Output:**

```
(3,)
(3, 1)
(1, 3)
(3,)
```

---

## ➕ 12. Adding & Removing Elements

```python
a = np.array([1, 2, 3])

print(np.append(a, [4, 5]))          # add to the end
print(np.insert(a, 1, 99))           # insert 99 at index 1
print(np.delete(a, 0))               # delete the element at index 0
print(np.delete(a, [0, 2]))          # delete several positions
```

**Output:**

```
[1 2 3 4 5]
[ 1 99  2  3]
[2 3]
[2]
```

### 📌 In 2D (use `axis`)

```python
m = np.array([[1, 2], [3, 4]])

print(np.append(m, [[5, 6]], axis=0))     # add a new row
print(np.append(m, [[7], [8]], axis=1))   # add a new column
print(np.delete(m, 0, axis=0))            # delete row 0
```

**Output:**

```
[[1 2]
 [3 4]
 [5 6]]
[[1 2 7]
 [3 4 8]]
[[3 4]]
```

> 💡 NumPy arrays have a **fixed size**, so these functions return a **new array** — they do not change the original.

---

## 🔗 13. Joining & Splitting

### 📌 Joining

```python
p = np.array([1, 2, 3])
q = np.array([4, 5, 6])

print(np.concatenate([p, q]))     # one long 1D array
print(np.vstack([p, q]))          # stack vertically (new rows)
print(np.hstack([p, q]))          # stack horizontally
print(np.stack([p, q], axis=1))   # pair elements up as columns
```

**Output:**

```
[1 2 3 4 5 6]
[[1 2 3]
 [4 5 6]]
[1 2 3 4 5 6]
[[1 4]
 [2 5]
 [3 6]]
```

### 📌 Splitting

```python
n = np.arange(8)

print(np.split(n, 4))                 # 4 equal parts
print(np.split(n, [2, 5]))            # split at index 2 and 5
print(np.array_split(np.arange(7), 3))   # parts may be unequal

grid = np.arange(12).reshape(3, 4)
print(np.vsplit(grid, 3))             # split into rows
print(np.hsplit(grid, 2))             # split into column groups
```

**Output:**

```
[array([0, 1]), array([2, 3]), array([4, 5]), array([6, 7])]
[array([0, 1]), array([2, 3, 4]), array([5, 6, 7])]
[array([0, 1, 2]), array([3, 4]), array([5, 6])]
[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]
```

---

## 🔁 14. Repeating Arrays

```python
a = np.array([1, 2, 3])

print(np.repeat(a, 2))        # repeat each ELEMENT
print(np.tile(a, 2))          # repeat the WHOLE array
print(np.tile(a, (2, 2)))     # tile into a 2x2 pattern
```

**Output:**

```
[1 1 2 2 3 3]
[1 2 3 1 2 3]
[[1 2 3 1 2 3]
 [1 2 3 1 2 3]]
```

---

## 📡 15. Broadcasting

**Broadcasting** lets NumPy do math on arrays of **different shapes** by automatically "stretching" the smaller one.

```python
m = np.array([[1, 2, 3],
              [4, 5, 6]])

print(m + 10)                           # scalar to every element
print(m + np.array([10, 20, 30]))       # row added to EVERY row
print(m * np.array([[1], [2]]))         # column multiplies each row
```

**Output:**

```
[[11 12 13]
 [14 15 16]]
[[11 22 33]
 [14 25 36]]
[[ 1  2  3]
 [ 8 10 12]]
```

### 📌 A column plus a row makes a full grid

```python
col = np.array([[1], [2], [3]])    # shape (3, 1)
row = np.array([10, 20, 30])       # shape (3,)

print(col + row)                   # shape (3, 3)
```

**Output:**

```
[[11 21 31]
 [12 22 32]
 [13 23 33]]
```

### 📌 The Broadcasting Rule

Compare shapes **from the right**. Two dimensions are compatible if they are **equal** or **one of them is 1**.

```python
try:
    print(np.array([1, 2, 3]) + np.array([1, 2, 3, 4]))
except ValueError as e:
    print("Error:", e)
```

**Output:**

```
Error: operands could not be broadcast together with shapes (3,) (4,)
```

---

## 🔎 16. Sorting & Searching

### 📌 Sorting

```python
d = np.array([3, 1, 2, 3, 1])

print(np.sort(d))              # ascending (returns a new array)
print(np.sort(d)[::-1])        # descending
print(np.argsort(d))           # indexes that would sort the array

grid = np.array([[3, 1, 2], [9, 7, 8]])
print(np.sort(grid, axis=1))   # sort each row
```

**Output:**

```
[1 1 2 3 3]
[3 3 2 1 1]
[1 4 2 0 3]
[[1 2 3]
 [7 8 9]]
```

### 📌 Searching

```python
d = np.array([3, 1, 2, 3, 1])

print(np.argwhere(d == 3))             # positions where value is 3
print(np.nonzero(d == 3))              # same, as a tuple of arrays

sorted_arr = np.array([10, 20, 30, 40])
print(np.searchsorted(sorted_arr, 25)) # where would 25 be inserted?
```

**Output:**

```
[[0]
 [3]]
(array([0, 3]),)
2
```

### 📌 Unique Values

```python
print(np.unique(d))
values, counts = np.unique(d, return_counts=True)
print(values)
print(counts)
```

**Output:**

```
[1 2 3]
[1 2 3]
[2 1 2]
```

---

## 🧮 17. Set Operations

```python
a = np.array([1, 2, 3, 4])
b = np.array([3, 4, 5, 6])

print(np.intersect1d(a, b))     # common elements
print(np.union1d(a, b))         # all unique elements
print(np.setdiff1d(a, b))       # in a but not in b
print(np.isin(a, b))            # is each element of a found in b?
print(a[np.isin(a, b)])         # filter using it
```

**Output:**

```
[3 4]
[1 2 3 4 5 6]
[1 2]
[False False  True  True]
[3 4]
```

---

## 🎲 18. Random Numbers

```python
np.random.seed(42)                       # makes results repeatable

print(np.random.rand(3))                 # random floats between 0 and 1
print(np.random.randn(3))                # normal distribution (mean 0, std 1)
print(np.random.randint(1, 100, 5))      # random integers 1-99
print(np.random.uniform(5, 10, 3))       # random floats between 5 and 10
print(np.random.normal(50, 10, 3))       # mean 50, std 10
print(np.random.choice([10, 20, 30, 40], 2, replace=False))   # pick without repeats
```

**Output:**

```
[0.37454012 0.95071431 0.73199394]
[-1.11188012  0.31890218  0.27904129]
[24  3 22 53  2]
[8.60999386 9.69276355 5.00389383]
[60.10515285 50.22221827 45.72207086]
[10 40]
```

### 📌 Shuffling

```python
deck = np.arange(1, 6)
np.random.shuffle(deck)                  # shuffles IN PLACE
print(deck)
print(np.random.permutation(5))          # returns a new shuffled array
```

**Output:**

```
[1 2 3 5 4]
[0 1 4 3 2]
```

### 📌 The Modern Way — `default_rng`

```python
rng = np.random.default_rng(seed=1)
print(rng.integers(1, 10, 5))
print(rng.random(3))
```

**Output:**

```
[5 5 7 9 1]
[0.94864945 0.31183145 0.42332645]
```

> 💡 Use `seed` when teaching or testing so everyone gets the **same** "random" numbers. Exact values can differ between NumPy versions.

---

## 🧱 19. Linear Algebra

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A * B)                  # element-by-element
print(A @ B)                  # TRUE matrix multiplication
print(np.dot(A, B))           # same as @
print(np.matmul(A, B))        # same as @
```

**Output:**

```
[[ 5 12]
 [21 32]]
[[19 22]
 [43 50]]
[[19 22]
 [43 50]]
[[19 22]
 [43 50]]
```

> ⚠️ `*` is **not** matrix multiplication. Use `@`.

```python
print(A.T)                              # transpose
print(np.trace(A))                      # sum of the diagonal
print(np.linalg.det(A))                 # determinant
print(np.linalg.inv(A))                 # inverse
print(np.linalg.matrix_rank(A))         # rank
print(np.linalg.norm([3, 4]))           # length of a vector
```

**Output:**

```
[[1 3]
 [2 4]]
5
-2.0000000000000004
[[-2.   1. ]
 [ 1.5 -0.5]]
2
5.0
```

### 📌 Solving Equations

Solve:  `2x + y = 5`  and  `x + 3y = 10`

```python
coeff = np.array([[2, 1],
                  [1, 3]])
const = np.array([5, 10])

print(np.linalg.solve(coeff, const))    # [x, y]
```

**Output:**

```
[1. 3.]
```

### 📌 Eigenvalues & Eigenvectors

```python
M = np.array([[2, 0], [0, 3]])
vals, vecs = np.linalg.eig(M)
print(vals)
print(vecs)
```

**Output:**

```
[2. 3.]
[[1. 0.]
 [0. 1.]]
```

### 📌 Dot Product of Vectors

```python
u = np.array([1, 2, 3])
w = np.array([4, 5, 6])
print(np.dot(u, w))       # 1*4 + 2*5 + 3*6
print(np.cross(u, w))     # cross product
```

**Output:**

```
32
[-3  6 -3]
```

---

## ❓ 20. Missing Values (NaN & Inf)

```python
n = np.array([1.0, np.nan, 3.0, np.inf])

print(np.isnan(n))                 # which are NaN?
print(np.isinf(n))                 # which are infinity?
print(np.nan == np.nan)            # NaN is never equal to itself!

clean = np.array([1.0, np.nan, 3.0])
print(clean.mean())                # any NaN poisons the result
print(np.nanmean(clean))           # ignore NaN
print(np.nansum(clean))
print(np.nanmax(clean))
print(np.nan_to_num(clean))        # replace NaN with 0
print(clean[~np.isnan(clean)])     # remove NaN values
```

**Output:**

```
[False  True False False]
[False False False  True]
False
nan
2.0
4.0
3.0
[1. 0. 3.]
[1. 3.]
```

---

## 📋 21. Copy vs View

```python
v = np.array([1, 2, 3])
w = v              # NOT a copy — same array, two names
w[0] = 99
print(v)

v2 = np.array([1, 2, 3])
c = v2.copy()      # a real, independent copy
c[0] = 99
print(v2)
```

**Output:**

```
[99  2  3]
[1 2 3]
```

### 📌 Slices are Views Too

```python
base = np.array([1, 2, 3, 4, 5])
part = base[1:4]          # a VIEW of the same memory
part[0] = 100
print(base)

safe = base[1:4].copy()   # independent copy
safe[0] = -1
print(base)
print(np.shares_memory(base, part))
```

**Output:**

```
[  1 100   3   4   5]
[  1 100   3   4   5]
True
```

> ⚠️ Slicing gives a **view** (shared data). Use `.copy()` whenever you need independent data.

---

## 💾 22. Saving & Loading Data

```python
arr = np.array([[1.5, 2.5], [3.5, 4.5]])

np.save("arr.npy", arr)                 # binary format (fast, exact)
print(np.load("arr.npy"))

np.savez("multi.npz", first=arr, second=np.arange(3))   # several arrays in one file
data = np.load("multi.npz")
print(data["second"])

np.savetxt("arr.csv", arr, delimiter=",")               # text/CSV format
print(np.loadtxt("arr.csv", delimiter=","))
```

**Output:**

```
[[1.5 2.5]
 [3.5 4.5]]
[0 1 2]
[[1.5 2.5]
 [3.5 4.5]]
```

---

## 🔂 23. Iterating Over Arrays

```python
a = np.array([10, 20, 30])
for item in a:
    print(item)

grid = np.array([[1, 2], [3, 4]])
for row in grid:                       # loops over ROWS
    print(row)

for i, val in enumerate(a):            # with index
    print(i, val)

for x in np.nditer(grid):              # visit EVERY element in a 2D array
    print(x, end=" ")
```

**Output:**

```
10
20
30
[1 2]
[3 4]
0 10
1 20
2 30
1 2 3 4
```

> 💡 Loops are fine for learning, but vectorized operations (`a * 2`) are much faster on large data.

---

## 🧰 24. Other Handy Functions

```python
print(np.corrcoef([1, 2, 3, 4], [2, 4, 6, 8])[0, 1])   # correlation (1.0 = perfect)
print(np.cov([1, 2, 3, 4], [2, 4, 6, 8]))               # covariance matrix
print(np.bincount([0, 1, 1, 3, 3, 3]))                  # count of each integer
print(np.histogram([1, 2, 2, 3, 3, 3], bins=3))         # counts per bin and bin edges
```

**Output:**

```
1.0
[[1.66666667 3.33333333]
 [3.33333333 6.66666667]]
[1 2 0 3]
(array([1, 2, 3]), array([1.        , 1.66666667, 2.33333333, 3.        ]))
```

### 📌 `meshgrid` — coordinate grids

```python
xs, ys = np.meshgrid([1, 2, 3], [10, 20])
print(xs)
print(ys)
```

**Output:**

```
[[1 2 3]
 [1 2 3]]
[[10 10 10]
 [20 20 20]]
```

### 📌 `vectorize` — use your own function on arrays

```python
def grade(mark):
    return "Pass" if mark >= 50 else "Fail"

vgrade = np.vectorize(grade)
print(vgrade(np.array([45, 82, 50])))
```

**Output:**

```
['Fail' 'Pass' 'Pass']
```

### 📌 `apply_along_axis`

```python
g = np.array([[1, 2, 3], [4, 5, 6]])
print(np.apply_along_axis(np.sum, 1, g))     # apply a function to each row
```

**Output:**

```
[ 6 15]
```

---

## 🎓 25. Mini Project — Student Marks Analysis

Rows are **students**, columns are **subjects** (Maths, English, CS).

```python
students = np.array(["Ali", "Sara", "Ahmed", "Zoya", "Hina"])
subjects = np.array(["Maths", "English", "CS"])

marks = np.array([[78, 65, 90],
                  [88, 92, 85],
                  [45, 50, 38],
                  [67, 70, 95],
                  [55, 48, 60]])

print("Shape:", marks.shape)
print("Average per student:", marks.mean(axis=1).round(1))
print("Average per subject:", marks.mean(axis=0).round(1))

top = marks.sum(axis=1).argmax()
print("Top student:", students[top])

best_subject = marks.mean(axis=0).argmax()
print("Best subject:", subjects[best_subject])

print("Students who passed everything:", students[(marks >= 50).all(axis=1)])
print("Number of failed papers:", np.count_nonzero(marks < 50))

curved = np.clip(marks + 5, 0, 100)          # +5 bonus, capped at 100
print(curved)
```

**Output:**

```
Shape: (5, 3)
Average per student: [77.7 88.3 44.3 77.3 54.3]
Average per subject: [66.6 65.  73.6]
Top student: Sara
Best subject: CS
Students who passed everything: ['Ali' 'Sara' 'Zoya']
Number of failed papers: 3
[[ 83  70  95]
 [ 93  97  90]
 [ 50  55  43]
 [ 72  75 100]
 [ 60  53  65]]
```

---

## 📝 26. Practice Exercises

1. Create an array of numbers from **1 to 20**, then print only the **even** numbers.
2. Create a **3×3** array of numbers 1–9 and print its **diagonal sum** (`np.trace`).
3. Given `[12, 45, 7, 23, 56, 89, 34]`, find the **mean, median, max**, and the **position** of the max.
4. Replace every **negative** number in `[-3, 5, -1, 8, -9]` with `0`.
5. Create a **4×4** array of random integers (1–50, seed 0) and print the **sum of each column**.
6. Normalize `[10, 20, 30, 40]` so values range from 0 to 1: `(x - min) / (max - min)`.

### ✅ Solutions

```python
# 1
n = np.arange(1, 21)
print(n[n % 2 == 0])

# 2
print(np.trace(np.arange(1, 10).reshape(3, 3)))

# 3
z = np.array([12, 45, 7, 23, 56, 89, 34])
print(z.mean().round(2), np.median(z), z.max(), z.argmax())

# 4
q = np.array([-3, 5, -1, 8, -9])
q[q < 0] = 0
print(q)

# 5
np.random.seed(0)
print(np.random.randint(1, 51, (4, 4)).sum(axis=0))

# 6
k = np.array([10, 20, 30, 40])
print((k - k.min()) / (k.max() - k.min()))
```

**Output:**

```
[ 2  4  6  8 10 12 14 16 18 20]
15
38.0 34.0 89 5
[0 5 0 8 0]
[ 96 150  48  33]
[0.         0.33333333 0.66666667 1.        ]
```

---

## 🧾 27. Cheat Sheet

| Task | Code |
|---|---|
| Import | `import numpy as np` |
| Create array | `np.array([1, 2, 3])` |
| Zeros / ones | `np.zeros((2,3))`, `np.ones((2,3))` |
| Range / spaced | `np.arange(0,10,2)`, `np.linspace(0,1,5)` |
| Shape / size / type | `a.shape`, `a.size`, `a.dtype` |
| Convert type | `a.astype(float)` |
| Slice | `a[1:4]`, `m[:, 0]`, `m[0:2, 1:3]` |
| Filter | `a[a > 5]` |
| If / else | `np.where(a > 5, "yes", "no")` |
| Sum / mean | `a.sum()`, `a.mean()`, `a.mean(axis=0)` |
| Min / max position | `a.argmin()`, `a.argmax()` |
| Reshape | `a.reshape(3, 4)`, `a.T`, `a.flatten()` |
| Join | `np.concatenate`, `np.vstack`, `np.hstack` |
| Split | `np.split`, `np.array_split` |
| Add / remove | `np.append`, `np.insert`, `np.delete` |
| Sort | `np.sort(a)`, `np.argsort(a)` |
| Unique | `np.unique(a, return_counts=True)` |
| Random | `np.random.seed(1)`, `np.random.randint(1,10,5)` |
| Matrix multiply | `A @ B` |
| Inverse / det | `np.linalg.inv(A)`, `np.linalg.det(A)` |
| Solve equations | `np.linalg.solve(A, b)` |
| Missing values | `np.isnan(a)`, `np.nanmean(a)` |
| Copy | `a.copy()` |
| Save / load | `np.save("a.npy", a)`, `np.load("a.npy")` |

---

## 🐼 What's Next?

Once you are comfortable with NumPy, move on to **Pandas**, which is built on top of NumPy and adds labeled rows and columns for working with real-world tables (CSV, Excel, SQL).

Happy coding! 🚀
