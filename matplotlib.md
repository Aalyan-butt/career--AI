# 📈 Matplotlib 101 — Beginner to Advanced Tutorial

This guide walks you through **Matplotlib**, Python's most popular data-visualization library — from your first line chart to subplots, 3D plots, heatmaps, styling, and a complete dashboard project. **Every example below was executed, and the picture under each one is the real output.**

---

## 📦 What Is Matplotlib?

**Matplotlib** is an open-source Python library for creating **static, animated, and interactive visualizations**. It is the foundation that **Pandas plotting, Seaborn, and many scientific/ML tools** are built on.

### ✅ Key Features
- Line, bar, scatter, pie, histogram, box, heatmap, 3D, polar and many more chart types
- Full control over every element (colors, fonts, ticks, legends, layout)
- Works in scripts, Jupyter notebooks, and GUI apps
- Saves to PNG, JPG, PDF, SVG
- Works hand-in-hand with **NumPy** and **Pandas**

---

## 📚 Table of Contents

1. Anatomy of a Matplotlib Figure
2. Installing & Importing
3. Your First Plot
4. Title, Labels, Legend & Grid
5. Styling Lines
6. Plotting Functions with NumPy
7. Bar Charts
8. Scatter Plots
9. Histograms
10. Pie & Donut Charts
11. Box & Violin Plots
12. Area Charts
13. Step & Stem Plots
14. Error Bars
15. Heatmaps & Images
16. Contour Plots
17. 2D Histograms & Hexbin
18. Polar Plots
19. 3D Plots
20. Subplots & Layouts
21. Customizing Axes
22. Text, Annotations & Shapes
23. Legends in Detail
24. Colors & Colormaps
25. Twin Axes
26. Dates on Axes
27. Styles & rcParams
28. Saving Figures
29. Plotting from Pandas
30. Animation, Interactive Mode & Backends
31. Mini Project — Class Dashboard
32. Practice Exercises
33. Cheat Sheet & Common Mistakes

---

## 🧬 1. Anatomy of a Matplotlib Figure

| Object | What it is |
|---|---|
| **Figure** | The whole canvas/window. It can hold one or many plots. |
| **Axes** | One individual plot (with its own x-axis, y-axis, title, data). |
| **Axis** | The x-axis or y-axis (ticks, tick labels, scale). |
| **Artist** | Everything you can see: lines, text, ticks, legends, patches. |

### 🧱 Two Ways to Code

| Style | Looks like | Best for |
|---|---|---|
| **pyplot (quick)** | `plt.plot()`, `plt.title()` | Quick single charts |
| **Object-oriented (OO)** | `fig, ax = plt.subplots()` then `ax.plot()`, `ax.set_title()` | Multiple plots, full control (**recommended**) |

> ⚠️ With an `ax` object the setters are named `set_title()`, `set_xlabel()`, `set_ylabel()`, `set_xlim()`, `set_ylim()` — not `title()`, `xlabel()`, etc.

---

## 💻 2. Installing & Importing

```bash
pip install matplotlib
```

```python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
```

**Output:**

```
3.11.2
```

`plt` is the universal nickname for `matplotlib.pyplot`.

---

## 📉 3. Your First Plot

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.show()
```

**Output:**

![Output](images/plot_01.png)

- `plt.plot(x, y)` draws a line through the points.
- `plt.show()` displays the figure. Call it **last**.

---

## 🏷️ 4. Title, Labels, Legend & Grid

```python
plt.plot(x, y, label="Double")
plt.title("Number Doubling")
plt.xlabel("Number")
plt.ylabel("Result")
plt.legend()
plt.grid(True)
plt.show()
```

**Output:**

![Output](images/plot_02.png)

| Function | Purpose |
|---|---|
| `plt.title("...")` | Chart title |
| `plt.xlabel("...")`, `plt.ylabel("...")` | Axis labels |
| `plt.legend()` | Shows the `label=` names |
| `plt.grid(True)` | Background grid |
| `plt.figure(figsize=(w, h))` | Set size in inches (call **before** plotting) |

---

## 🎨 5. Styling Lines

```python
plt.plot(x, y, color="red", linestyle="--", marker="o",
         linewidth=2, markersize=8, label="Line A")

plt.plot(x, [v ** 1.2 for v in x], "g^:", label="Line B")   # shortcut style
plt.legend()
plt.show()
```

**Output:**

![Output](images/plot_03.png)

### 📌 Line Options

| Option | Examples |
|---|---|
| `color` / `c` | `"red"`, `"r"`, `"#ff9999"`, `"skyblue"`, `"0.5"` (gray) |
| `linestyle` / `ls` | `"-"` solid, `"--"` dashed, `":"` dotted, `"-."` dash-dot |
| `marker` | `"o"` circle, `"s"` square, `"^"` triangle, `"*"` star, `"x"` cross, `"D"` diamond |
| `linewidth` / `lw` | Thickness, e.g. `2` |
| `markersize` / `ms` | Marker size |
| `markerfacecolor` | Fill color of markers |
| `alpha` | Transparency (0 = invisible, 1 = solid) |
| `label` | Name used by the legend |

### 📌 Format String Shortcut: `"[marker][line][color]"`

| Code | Meaning |
|---|---|
| `"ro--"` | red, circles, dashed |
| `"g^:"` | green, triangles, dotted |
| `"b-"` | blue, solid |

---

## 🌊 6. Plotting Functions with NumPy

```python
xs = np.linspace(0, 2 * np.pi, 100)     # 100 points from 0 to 2π

plt.plot(xs, np.sin(xs), label="sin(x)")
plt.plot(xs, np.cos(xs), label="cos(x)")
plt.title("Sine and Cosine")
plt.xlabel("x (radians)")
plt.legend()
plt.grid(True)
plt.show()
```

**Output:**

![Output](images/plot_04.png)

> 💡 `np.linspace(start, stop, n)` is the easiest way to make smooth curves.

---

## 📊 7. Bar Charts

### 📌 Vertical Bars

```python
subjects = ["Maths", "English", "CS"]
marks = [78, 65, 90]

plt.bar(subjects, marks, color=["red", "green", "blue"], width=0.5)
plt.title("Marks of Ali")
plt.ylabel("Marks")
plt.show()
```

**Output:**

![Output](images/plot_05.png)

### 📌 Horizontal Bars

```python
plt.barh(subjects, marks, color="teal")
plt.title("Horizontal Bar Chart")
plt.show()
```

**Output:**

![Output](images/plot_06.png)

### 📌 Grouped Bars (comparing students)

```python
w = 0.35
i = np.arange(3)

plt.bar(i - w/2, [78, 65, 90], w, label="Ali")
plt.bar(i + w/2, [88, 92, 85], w, label="Sara")
plt.xticks(i, subjects)             # put subject names under the groups
plt.legend()
plt.title("Grouped Bars")
plt.show()
```

**Output:**

![Output](images/plot_07.png)

Shift one set of bars left and the other right by half the bar width so they sit side by side.

### 📌 Stacked Bars

```python
ali = np.array([78, 65, 90])
sara = np.array([88, 92, 85])

plt.bar(subjects, ali, label="Ali")
plt.bar(subjects, sara, bottom=ali, label="Sara")   # start where Ali's bar ends
plt.legend()
plt.title("Stacked Bars")
plt.show()
```

**Output:**

![Output](images/plot_08.png)

### 📌 Value Labels on Bars

```python
fig, ax = plt.subplots()
bars = ax.bar(subjects, marks, color="skyblue")
ax.bar_label(bars)                      # prints each value on top of its bar
ax.set_ylim(0, 100)
ax.set_title("Bars with Labels")
plt.show()
```

**Output:**

![Output](images/plot_09.png)

---

## 🔵 8. Scatter Plots

Show the **relationship between two variables** as separate dots.

```python
np.random.seed(0)
a = np.random.rand(30)
b = np.random.rand(30)

sc = plt.scatter(a, b, s=a * 300, c=b, cmap="viridis", alpha=0.7)
plt.colorbar(sc, label="b value")
plt.title("Scatter Plot")
plt.show()
```

**Output:**

![Output](images/plot_10.png)

| Parameter | Meaning |
|---|---|
| `s` | Dot size (one number, or one per point) |
| `c` | Color (one color, or numbers mapped through `cmap`) |
| `cmap` | Color map: `"viridis"`, `"plasma"`, `"coolwarm"`, `"Blues"` |
| `alpha` | Transparency (helps when dots overlap) |
| `marker` | Dot shape |
| `edgecolors` | Outline color of dots |

### 📌 Scatter by Category

```python
group1 = np.random.normal(2, 0.5, (30, 2))
group2 = np.random.normal(4, 0.5, (30, 2))

plt.scatter(group1[:, 0], group1[:, 1], label="Group 1", color="tomato")
plt.scatter(group2[:, 0], group2[:, 1], label="Group 2", color="steelblue", marker="s")
plt.legend()
plt.title("Two Groups")
plt.show()
```

**Output:**

![Output](images/plot_11.png)

### 📌 Scatter + Trend Line

```python
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
score = np.array([35, 42, 50, 58, 62, 71, 78, 85])

slope, intercept = np.polyfit(hours, score, 1)      # best-fit straight line
plt.scatter(hours, score, color="black", label="Students")
plt.plot(hours, slope * hours + intercept, "r--", label="Trend")
plt.xlabel("Study hours")
plt.ylabel("Score")
plt.legend()
plt.show()
print("slope:", round(slope, 2), "intercept:", round(intercept, 2))
```

**Output:**

```
slope: 7.11 intercept: 28.14
```

![Output](images/plot_12.png)

---

## 📶 9. Histograms

Show the **distribution** of numbers by counting how many fall in each range (bin).

```python
data = np.random.normal(50, 10, 300)     # 300 values around 50

plt.hist(data, bins=12, color="skyblue", edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
```

**Output:**

![Output](images/plot_13.png)

`bins` is the number of bars — more bins gives finer detail.

> 💡 **Bar chart vs histogram:** a bar chart compares *categories*; a histogram shows the spread of *numbers*.

### 📌 Comparing Two Datasets

```python
d1 = np.random.normal(50, 10, 300)
d2 = np.random.normal(65, 8, 300)

plt.hist(d1, bins=15, alpha=0.6, label="Class A")
plt.hist(d2, bins=15, alpha=0.6, label="Class B")
plt.legend()
plt.show()
```

**Output:**

![Output](images/plot_14.png)

### 📌 Density & Cumulative

```python
fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
ax[0].hist(data, bins=15, density=True, color="orange")      # area adds up to 1
ax[0].set_title("density=True")
ax[1].hist(data, bins=15, cumulative=True, color="green")    # running total
ax[1].set_title("cumulative=True")
plt.show()
```

**Output:**

![Output](images/plot_15.png)

---

## 🥧 10. Pie & Donut Charts

```python
sizes = [40, 30, 20, 10]
labels = ["A", "B", "C", "D"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%",
        explode=[0.1, 0, 0, 0], startangle=90,
        colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"])
plt.title("Pie Chart")
plt.show()
```

**Output:**

![Output](images/plot_16.png)

| Parameter | Meaning |
|---|---|
| `labels` | Names of slices |
| `autopct="%1.1f%%"` | Show percentages with 1 decimal |
| `explode` | Pull a slice out (0 = stays in) |
| `startangle` | Rotate where the first slice starts |
| `colors` | Slice colors |
| `shadow=True` | Add a shadow |

### 📌 Donut Chart

```python
plt.pie(sizes, labels=labels, autopct="%1.0f%%",
        wedgeprops=dict(width=0.4))          # a hole in the middle
plt.title("Donut Chart")
plt.show()
```

**Output:**

![Output](images/plot_17.png)

---

## 📦 11. Box & Violin Plots

### 📌 Box Plot

Shows the **median, quartiles, spread and outliers** at a glance.

```python
g1 = np.random.normal(50, 10, 200)
g2 = np.random.normal(58, 15, 200)

plt.boxplot([g1, g2], tick_labels=["Class A", "Class B"])
plt.title("Box Plot")
plt.show()
```

**Output:**

![Output](images/plot_18.png)

The box covers the middle 50% of data, the line inside is the median, whiskers show the range, and dots beyond them are outliers. *(In Matplotlib older than 3.9 use `labels=` instead of `tick_labels=`.)*

### 📌 Violin Plot

Like a box plot, but also shows the **shape of the distribution**.

```python
plt.violinplot([g1, g2], showmedians=True)
plt.xticks([1, 2], ["Class A", "Class B"])
plt.title("Violin Plot")
plt.show()
```

**Output:**

![Output](images/plot_19.png)

---

## 🏔️ 12. Area Charts

```python
xs = np.linspace(0, 10, 100)

plt.plot(xs, np.sin(xs), color="navy")
plt.fill_between(xs, np.sin(xs), alpha=0.3)            # shade under the curve
plt.title("fill_between")
plt.show()
```

**Output:**

![Output](images/plot_20.png)

### 📌 Shade Between Two Curves

```python
plt.plot(xs, np.sin(xs), label="sin")
plt.plot(xs, np.cos(xs), label="cos")
plt.fill_between(xs, np.sin(xs), np.cos(xs), alpha=0.25, color="orange")
plt.legend()
plt.show()
```

**Output:**

![Output](images/plot_21.png)

### 📌 Stacked Area

```python
days = [1, 2, 3, 4, 5]
plt.stackplot(days, [1, 2, 3, 4, 5], [2, 2, 2, 2, 2], [1, 1, 2, 3, 3],
              labels=["Food", "Rent", "Fun"])
plt.legend(loc="upper left")
plt.title("Stacked Area")
plt.show()
```

**Output:**

![Output](images/plot_22.png)

---

## 🪜 13. Step & Stem Plots

```python
fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))

ax[0].step([1, 2, 3, 4, 5], [1, 3, 2, 5, 4], where="mid")
ax[0].set_title("step()")

ax[1].stem([1, 2, 3, 4, 5], [1, 3, 2, 5, 4])
ax[1].set_title("stem()")

plt.show()
```

**Output:**

![Output](images/plot_23.png)

---

## 📏 14. Error Bars

```python
vals = np.array([5, 7, 6, 9, 8])
errors = np.array([0.5, 1.0, 0.8, 1.2, 0.6])

plt.errorbar(range(5), vals, yerr=errors, fmt="o-", capsize=5, color="purple")
plt.title("Error Bars")
plt.show()
```

**Output:**

![Output](images/plot_24.png)

`yerr` is the +/- uncertainty for each point. Use `xerr` for horizontal error bars.

---

## 🔥 15. Heatmaps & Images

### 📌 Heatmap with `imshow`

```python
students = ["Ali", "Sara", "Ahmed"]
grid = np.array([[78, 65, 90],
                 [88, 92, 85],
                 [45, 50, 38]])

fig, ax = plt.subplots()
im = ax.imshow(grid, cmap="YlGn")
ax.set_xticks(range(3), labels=subjects)
ax.set_yticks(range(3), labels=students)

for r in range(3):                       # write the value inside each cell
    for c in range(3):
        ax.text(c, r, grid[r, c], ha="center", va="center")

plt.colorbar(im, label="Marks")
ax.set_title("Marks Heatmap")
plt.show()
```

**Output:**

![Output](images/plot_25.png)

### 📌 Showing & Saving Images

```python
img = np.random.rand(8, 8, 3)            # 8x8 random RGB image
plt.imsave("noise.png", img)             # save array as an image file
loaded = plt.imread("noise.png")         # read it back
print(loaded.shape)                      # height, width, RGBA channels

plt.imshow(loaded)
plt.axis("off")                          # hide axes
plt.title("Random Pixels")
plt.show()
```

**Output:**

```
(8, 8, 4)
```

![Output](images/plot_26.png)

---

## 🗺️ 16. Contour Plots

```python
X, Y = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
Z = np.sin(X) * np.cos(Y)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

cf = ax[0].contourf(X, Y, Z, levels=15, cmap="coolwarm")   # filled
fig.colorbar(cf, ax=ax[0])
ax[0].set_title("contourf()")

cs = ax[1].contour(X, Y, Z, levels=10, colors="black")      # lines only
ax[1].clabel(cs)                                            # label the lines
ax[1].set_title("contour()")

plt.show()
```

**Output:**

![Output](images/plot_27.png)

`np.meshgrid` creates a grid of x and y coordinates so a value `Z` can be computed at every point.

---

## ⬢ 17. 2D Histograms & Hexbin

```python
px = np.random.randn(2000)
py = np.random.randn(2000)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
h = ax[0].hist2d(px, py, bins=25, cmap="Blues")
fig.colorbar(h[3], ax=ax[0])
ax[0].set_title("hist2d()")

hb = ax[1].hexbin(px, py, gridsize=20, cmap="Oranges")
fig.colorbar(hb, ax=ax[1])
ax[1].set_title("hexbin()")
plt.show()
```

**Output:**

![Output](images/plot_28.png)

Great for scatter plots with **too many points** — they show where the data is dense.

---

## 🎯 18. Polar Plots

```python
theta = np.linspace(0, 2 * np.pi, 200)
r = 1 + np.sin(4 * theta)

fig = plt.figure()
ax = fig.add_subplot(projection="polar")
ax.plot(theta, r, color="crimson")
ax.set_title("Polar Plot")
plt.show()
```

**Output:**

![Output](images/plot_29.png)

---

## 🧊 19. 3D Plots

```python
X, Y = np.meshgrid(np.linspace(-3, 3, 60), np.linspace(-3, 3, 60))
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(projection="3d")
ax.plot_surface(X, Y, Z, cmap="viridis")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Surface")
plt.show()
```

**Output:**

![Output](images/plot_30.png)

### 📌 3D Scatter & Line

```python
t = np.linspace(0, 10, 100)

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(projection="3d")
ax.plot(np.cos(t), np.sin(t), t, color="navy")                       # 3D line
ax.scatter(np.cos(t[::10]), np.sin(t[::10]), t[::10], color="red")   # 3D dots
ax.set_title("3D Helix")
plt.show()
```

**Output:**

![Output](images/plot_31.png)

---

## 🧩 20. Subplots & Layouts

### 📌 Method 1: `plt.subplots()` (recommended)

```python
fig, ax = plt.subplots(2, 2, figsize=(9, 6))        # 2 rows, 2 columns

ax[0, 0].plot([1, 2, 3], [1, 4, 9])
ax[0, 0].set_title("Line")

ax[0, 1].bar(subjects, marks)
ax[0, 1].set_title("Bar")

ax[1, 0].scatter(a, b)
ax[1, 0].set_title("Scatter")

ax[1, 1].hist(data)
ax[1, 1].set_title("Histogram")

fig.tight_layout()           # stop labels overlapping
plt.show()
```

**Output:**

![Output](images/plot_32.png)

### 📌 Method 2: `plt.subplot(rows, cols, position)`

```python
plt.figure(figsize=(9, 3.5))

plt.subplot(1, 2, 1)         # 1 row, 2 columns, first plot
plt.plot(x, y)
plt.title("Left")

plt.subplot(1, 2, 2)         # second plot
plt.bar(subjects, marks)
plt.title("Right")

plt.tight_layout()
plt.show()
```

**Output:**

![Output](images/plot_33.png)

### 📌 Shared Axes

```python
fig, ax = plt.subplots(2, 1, sharex=True, figsize=(7, 5))
ax[0].plot(xs, np.sin(xs))
ax[1].plot(xs, np.cos(xs), color="orange")
fig.suptitle("Shared X-axis")
plt.show()
```

**Output:**

![Output](images/plot_34.png)

### 📌 Uneven Layouts with `GridSpec`

```python
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(9, 5))
gs = GridSpec(2, 3, figure=fig)

ax1 = fig.add_subplot(gs[0, :])         # top row, all columns
ax2 = fig.add_subplot(gs[1, 0:2])       # bottom row, first two columns
ax3 = fig.add_subplot(gs[1, 2])         # bottom right

ax1.plot(xs, np.sin(xs)); ax1.set_title("Wide")
ax2.bar(subjects, marks); ax2.set_title("Medium")
ax3.hist(data, bins=8);   ax3.set_title("Small")

fig.tight_layout()
plt.show()
```

**Output:**

![Output](images/plot_35.png)

### 📌 `subplot_mosaic` — draw the layout as text

```python
fig, axd = plt.subplot_mosaic("AAB;CDB", figsize=(8, 5))   # ';' separates rows
axd["A"].plot(xs, np.sin(xs)); axd["A"].set_title("A")
axd["B"].hist(data);           axd["B"].set_title("B (tall)")
axd["C"].scatter(a, b);        axd["C"].set_title("C")
axd["D"].bar(subjects, marks); axd["D"].set_title("D")
fig.tight_layout()
plt.show()
```

**Output:**

![Output](images/plot_36.png)

---

## 📐 21. Customizing Axes

### 📌 Limits, Ticks & Rotation

```python
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, "o-")
ax.set_xlim(0, 6)                  # x-axis range
ax.set_ylim(0, 12)                 # y-axis range
ax.set_xticks([1, 3, 5])           # choose tick positions
ax.set_yticks(range(0, 13, 4))
ax.set_title("Custom Limits & Ticks")
plt.show()
```

**Output:**

![Output](images/plot_37.png)



```python
cities = ["Faisalabad", "Lahore", "Karachi", "Islamabad"]
temp = [34, 33, 31, 28]

plt.bar(cities, temp)
plt.xticks(rotation=45, ha="right")     # rotate long labels
plt.title("Rotated Tick Labels")
plt.tight_layout()
plt.show()
```

**Output:**

![Output](images/plot_38.png)

### 📌 Formatting Tick Labels

```python
from matplotlib.ticker import FuncFormatter, MultipleLocator

fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3], [10, 40, 70, 100], "o-")
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f}%"))   # 40 -> 40%
ax.xaxis.set_major_locator(MultipleLocator(1))                          # tick every 1
ax.set_title("Formatted Ticks")
plt.show()
```

**Output:**

![Output](images/plot_39.png)

### 📌 Spines (the box around the plot)

```python
fig, ax = plt.subplots()
ax.plot(x, y, "o-")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_title("Clean Look: top & right spines hidden")
plt.show()
```

**Output:**

![Output](images/plot_40.png)

### 📌 Scales, Aspect & Inversion

```python
fig, ax = plt.subplots(1, 3, figsize=(11, 3.5))

ax[0].plot([1, 10, 100, 1000], [1, 2, 3, 4], "o-")
ax[0].set_xscale("log")                  # logarithmic x-axis
ax[0].set_title("Log scale")

ax[1].add_patch(plt.Circle((0, 0), 1, color="salmon"))
ax[1].set_xlim(-2, 2); ax[1].set_ylim(-2, 2)
ax[1].set_aspect("equal")                # circle stays round
ax[1].set_title("Equal aspect")

ax[2].barh(subjects, marks)
ax[2].invert_yaxis()                     # first item on top
ax[2].set_title("Inverted y-axis")

plt.show()
```

**Output:**

![Output](images/plot_41.png)

| Method | Purpose |
|---|---|
| `set_xlim(a, b)` / `set_ylim(a, b)` | Axis range |
| `set_xticks()` / `set_yticks()` | Tick positions |
| `set_xticklabels()` | Tick text |
| `tick_params(labelsize=10)` | Tick appearance |
| `set_xscale("log")` | Log scale (also `"symlog"`) |
| `set_aspect("equal")` | Same scale on both axes |
| `invert_xaxis()` / `invert_yaxis()` | Flip direction |
| `axis("off")` | Hide the axes completely |

---

## ✍️ 22. Text, Annotations & Shapes

### 📌 Text, Arrows and Reference Lines

```python
plt.plot(x, y, "o-")
plt.text(1.2, 8, "Hello!", fontsize=14, color="purple")       # text at (x, y)
plt.annotate("Peak", xy=(5, 10), xytext=(3, 9.5),
             arrowprops=dict(arrowstyle="->", color="red"))   # text with arrow
plt.axhline(6, color="gray", linestyle="--")                  # horizontal line at y=6
plt.axvline(3, color="green", linestyle=":")                  # vertical line at x=3
plt.axvspan(1, 2, color="yellow", alpha=0.3)                  # shaded vertical band
plt.show()
```

**Output:**

![Output](images/plot_42.png)

### 📌 Shapes (patches)

```python
from matplotlib.patches import Rectangle, Circle

fig, ax = plt.subplots()
ax.add_patch(Rectangle((1, 1), 3, 2, color="skyblue"))        # (x, y), width, height
ax.add_patch(Circle((6, 2), 1, color="salmon"))               # (x, y), radius
ax.set_xlim(0, 8)
ax.set_ylim(0, 5)
ax.set_aspect("equal")
ax.set_title("Patches")
plt.show()
```

**Output:**

![Output](images/plot_43.png)

### 📌 Math Text (LaTeX-style)

Wrap text in `$...$` and use a raw string `r"..."`.

```python
xv = np.linspace(-3, 3, 100)
plt.plot(xv, xv**2)
plt.title(r"$y = x^2$", fontsize=16)
plt.xlabel(r"$x$ value")
plt.ylabel(r"$\alpha = x^2$")
plt.text(-1, 6, r"$\sqrt{x^2} = |x|$", fontsize=14)
plt.show()
```

**Output:**

![Output](images/plot_44.png)

### 📌 Font Options

| Option | Examples |
|---|---|
| `fontsize` | `12`, `"large"`, `"x-large"` |
| `fontweight` | `"bold"`, `"light"` |
| `fontstyle` | `"italic"` |
| `color` | any color |
| `family` | `"serif"`, `"monospace"` |
| `rotation` | `45` |
| `ha`, `va` | `"center"`, `"left"`, `"top"`, ... |

---

## 🏷️ 23. Legends in Detail

```python
fig, ax = plt.subplots(figsize=(7, 4))
for k in range(1, 5):
    ax.plot(xs, np.sin(xs) * k, label=f"k = {k}")

ax.legend(title="Amplitude", loc="upper left",
          bbox_to_anchor=(1.02, 1),      # put legend OUTSIDE the plot
          frameon=False)
fig.tight_layout()
plt.show()
```

**Output:**

![Output](images/plot_45.png)

| Option | Purpose |
|---|---|
| `loc` | `"best"`, `"upper left"`, `"lower right"`, `"center"`, ... |
| `ncol` | Number of columns |
| `title` | Legend title |
| `frameon=False` | Remove the box |
| `fontsize` | Text size |
| `bbox_to_anchor` | Exact position (e.g. outside the axes) |

> 💡 Lines with a name starting with `_` or without `label=` are not shown in the legend.

---

## 🌈 24. Colors & Colormaps

### 📌 Ways to Specify a Color

| Style | Example |
|---|---|
| Name | `"red"`, `"skyblue"`, `"tomato"` |
| Short code | `"r"`, `"g"`, `"b"`, `"k"` (black), `"w"`, `"c"`, `"m"`, `"y"` |
| Hex | `"#ff9999"` |
| RGB tuple (0–1) | `(0.2, 0.5, 0.8)` |
| Gray level | `"0.5"` |
| Default cycle | `"C0"`, `"C1"`, `"C2"`, ... |

### 📌 Popular Colormaps

```python
gradient = np.linspace(0, 1, 256).reshape(1, -1)
names = ["viridis", "plasma", "coolwarm", "Blues", "YlGn", "gray"]

fig, ax = plt.subplots(len(names), 1, figsize=(7, 3))
for axis, name in zip(ax, names):
    axis.imshow(gradient, aspect="auto", cmap=name)
    axis.set_axis_off()
    axis.set_title(name, fontsize=9, loc="left")
fig.tight_layout()
plt.show()
```

**Output:**

![Output](images/plot_46.png)

| Type | Colormaps | Use for |
|---|---|---|
| Sequential | `viridis`, `plasma`, `Blues`, `YlGn` | Ordered data (low → high) |
| Diverging | `coolwarm`, `RdBu`, `seismic` | Data with a meaningful center (e.g. 0) |
| Qualitative | `tab10`, `Set2`, `Pastel1` | Categories |

Add `_r` to reverse any colormap, e.g. `"viridis_r"`.

---

## 🔀 25. Twin Axes (Two Y-Axes)

```python
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()                         # second y-axis sharing the same x

ax1.plot(x, y, "b-o")
ax1.set_ylabel("Sales", color="blue")

ax2.plot(x, [5, 4, 3, 2, 1], "r-s")
ax2.set_ylabel("Returns", color="red")

plt.title("Two Y-Axes")
plt.show()
```

**Output:**

![Output](images/plot_47.png)

---

## 📅 26. Dates on Axes

```python
import pandas as pd
import matplotlib.dates as mdates

dates = pd.date_range("2026-01-01", periods=10)
values = np.cumsum(np.random.randn(10))

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(dates, values, "o-")
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))   # 05 Jan
fig.autofmt_xdate()                                           # rotate nicely
ax.set_title("Dates on the X-axis")
plt.show()
```

**Output:**

![Output](images/plot_48.png)

---

## 🎭 27. Styles & rcParams

```python
print(plt.style.available[:8])
```

**Output:**

```
['Solarize_Light2', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale']
```



```python
with plt.style.context("ggplot"):              # temporary style
    plt.plot(xs, np.sin(xs))
    plt.title("ggplot style")
    plt.show()

with plt.style.context("dark_background"):
    plt.plot(xs, np.sin(xs), color="cyan")
    plt.title("dark_background style")
    plt.show()
```

**Output:**

![Output](images/plot_49.png)

![Output](images/plot_50.png)

- `plt.style.use("ggplot")` applies a style to **everything after it**.
- `plt.style.use("default")` goes back to normal.
- Popular styles: `ggplot`, `seaborn-v0_8`, `bmh`, `fivethirtyeight`, `dark_background`, `classic`.

### 📌 Global Settings with `rcParams`

```python
plt.rcParams["font.size"] = 12
plt.rcParams["figure.figsize"] = (8, 5)
plt.rcParams["axes.grid"] = True
plt.rcParams["lines.linewidth"] = 2
```

---

## 💾 28. Saving Figures

```python
fig.savefig("chart.png", dpi=200, bbox_inches="tight")
plt.savefig("chart.pdf")                      # PDF (vector)
plt.savefig("chart.svg")                      # SVG (vector)
plt.savefig("chart.png", transparent=True)    # transparent background
```

| Option | Meaning |
|---|---|
| `dpi` | Quality (dots per inch) — 100 screen, 300 print |
| `bbox_inches="tight"` | Trim extra white space |
| `transparent=True` | Transparent background |
| `facecolor` | Background color |

> ⚠️ Call `savefig()` **before** `plt.show()`, otherwise you may save a blank image.

---

## 🐼 29. Plotting from Pandas

```python
df = pd.DataFrame({
    "Subject": subjects,
    "Ali": [78, 65, 90],
    "Sara": [88, 92, 85],
})

df.plot(x="Subject", kind="bar", figsize=(6, 4), rot=0)    # bar chart for both columns
plt.title("Pandas plot()")
plt.show()
```

**Output:**

![Output](images/plot_51.png)

`kind` can be `"line"`, `"bar"`, `"barh"`, `"hist"`, `"box"`, `"pie"`, `"scatter"`, `"area"`. Pandas uses Matplotlib behind the scenes, so everything above still works.

---

## 🎬 30. Animation, Interactive Mode & Backends

### 📌 Simple Animation (run this in a script or notebook)

```python
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xs = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(xs, np.sin(xs))

def update(frame):
    line.set_ydata(np.sin(xs + frame / 10))   # shift the wave
    return line,

ani = FuncAnimation(fig, update, frames=100, interval=50)
plt.show()
# ani.save("wave.gif", writer="pillow")        # save as GIF
```

### 📌 Interactive Mode & Backends

| Topic | Command |
|---|---|
| Notebook, static images | `%matplotlib inline` |
| Notebook, interactive zoom/pan | `%matplotlib widget` (needs `ipympl`) |
| Update plots while code runs | `plt.ion()` ... `plt.pause(0.5)` ... `plt.ioff()` |
| Servers / no display | `matplotlib.use("Agg")` (save only) |
| Close figures to free memory | `plt.close()` / `plt.close("all")` |

---

## 🎓 31. Mini Project — Class Dashboard

Rows are **students**, columns are **subjects**.

```python
students = ["Ali", "Sara", "Ahmed", "Zoya", "Hina"]
subjects = ["Maths", "English", "CS"]
marks = np.array([[78, 65, 90],
                  [88, 92, 85],
                  [45, 50, 38],
                  [67, 70, 95],
                  [55, 48, 60]])

fig, ax = plt.subplots(2, 2, figsize=(11, 8))

# 1. Average per student (bar, colored by pass/fail)
avg = marks.mean(axis=1)
colors = ["seagreen" if v >= 50 else "tomato" for v in avg]
bars = ax[0, 0].bar(students, avg, color=colors)
ax[0, 0].bar_label(bars, fmt="%.1f")
ax[0, 0].axhline(50, color="gray", linestyle="--")
ax[0, 0].set_title("Average per Student")
ax[0, 0].set_ylim(0, 100)

# 2. Average per subject
ax[0, 1].bar(subjects, marks.mean(axis=0), color="orange")
ax[0, 1].set_title("Average per Subject")
ax[0, 1].set_ylim(0, 100)

# 3. Each student across subjects
for i, name in enumerate(students):
    ax[1, 0].plot(subjects, marks[i], marker="o", label=name)
ax[1, 0].set_title("Marks by Subject")
ax[1, 0].legend(fontsize=8, ncol=5, loc="upper center", bbox_to_anchor=(0.5, -0.1))

# 4. Heatmap of all marks
im = ax[1, 1].imshow(marks, cmap="RdYlGn", vmin=30, vmax=100)
ax[1, 1].set_xticks(range(3), labels=subjects)
ax[1, 1].set_yticks(range(5), labels=students)
for r in range(5):
    for c in range(3):
        ax[1, 1].text(c, r, marks[r, c], ha="center", va="center")
fig.colorbar(im, ax=ax[1, 1])
ax[1, 1].set_title("Marks Heatmap")

fig.suptitle("Class Dashboard", fontsize=16, fontweight="bold")
fig.tight_layout()
plt.show()
```

**Output:**

![Output](images/plot_52.png)

---

## 📝 32. Practice Exercises

1. Plot `y = x²` for x from −10 to 10 with a title, labels and grid.
2. Draw a bar chart of 5 cities and their temperatures, each bar a different color.
3. Make a pie chart of how you spend a 24-hour day.
4. Plot `sin(x)` and `cos(x)` on the same axes with a legend.
5. Generate 100 random marks and show a histogram with 8 bins.
6. Create a 1×2 subplot: a line chart on the left and a scatter plot on the right.

### ✅ Solutions

```python
fig, ax = plt.subplots(2, 3, figsize=(13, 7))

# 1
v = np.linspace(-10, 10, 100)
ax[0, 0].plot(v, v**2)
ax[0, 0].set(title="1) y = x²", xlabel="x", ylabel="y")
ax[0, 0].grid(True)

# 2
ax[0, 1].bar(["A", "B", "C", "D", "E"], [30, 35, 28, 33, 25],
             color=["red", "green", "blue", "orange", "purple"])
ax[0, 1].set_title("2) Temperatures")

# 3
ax[0, 2].pie([8, 8, 4, 2, 2], labels=["Sleep", "Work", "Study", "Food", "Play"], autopct="%1.0f%%")
ax[0, 2].set_title("3) My 24 Hours")

# 4
t = np.linspace(0, 2 * np.pi, 100)
ax[1, 0].plot(t, np.sin(t), label="sin")
ax[1, 0].plot(t, np.cos(t), label="cos")
ax[1, 0].legend()
ax[1, 0].set_title("4) sin & cos")

# 5
np.random.seed(1)
ax[1, 1].hist(np.random.randint(30, 100, 100), bins=8, edgecolor="black")
ax[1, 1].set_title("5) Histogram")

ax[1, 2].set_axis_off()       # exercise 6 is in the next cell

fig.tight_layout()
plt.show()
```

**Output:**

![Output](images/plot_53.png)

**Exercise 6** — a 1×2 subplot:

```python
fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
ax[0].plot([1, 2, 3, 4], [1, 4, 9, 16], "o-")
ax[0].set_title("Line")
ax[1].scatter([1, 2, 3, 4], [2, 3, 8, 12], color="red")
ax[1].set_title("Scatter")
fig.tight_layout()
plt.show()
```

**Output:**

![Output](images/plot_54.png)

---

## 🧾 33. Cheat Sheet & Common Mistakes

### 📋 Cheat Sheet

| Task | Code |
|---|---|
| Import | `import matplotlib.pyplot as plt` |
| Line | `plt.plot(x, y)` |
| Bar / horizontal bar | `plt.bar(x, h)` / `plt.barh(y, w)` |
| Scatter | `plt.scatter(x, y, s=, c=)` |
| Histogram | `plt.hist(data, bins=10)` |
| Pie | `plt.pie(sizes, labels=, autopct=)` |
| Box / violin | `plt.boxplot(data)` / `plt.violinplot(data)` |
| Heatmap | `plt.imshow(grid, cmap=)` |
| Contour | `plt.contourf(X, Y, Z)` |
| Fill area | `plt.fill_between(x, y1, y2)` |
| Error bars | `plt.errorbar(x, y, yerr=)` |
| Title / labels | `plt.title()`, `plt.xlabel()`, `plt.ylabel()` |
| Legend / grid | `plt.legend()`, `plt.grid(True)` |
| Figure size | `plt.figure(figsize=(8, 5))` |
| Limits | `plt.xlim(a, b)`, `plt.ylim(a, b)` |
| Ticks | `plt.xticks(pos, labels, rotation=45)` |
| Reference lines | `plt.axhline(y)`, `plt.axvline(x)` |
| Text / arrow | `plt.text()`, `plt.annotate()` |
| Subplots | `fig, ax = plt.subplots(r, c)` |
| Fix layout | `fig.tight_layout()` |
| Style | `plt.style.use("ggplot")` |
| Save | `plt.savefig("a.png", dpi=200)` |
| Show / close | `plt.show()` / `plt.close()` |

### ⚠️ Common Beginner Mistakes

- Forgetting `plt.show()` — in some environments the plot never appears.
- Mixing `plt.title()` with `ax.set_title()` — with an `ax`, use the `set_...` versions.
- Data lists of different lengths (`x` has 5 values, `y` has 4) → `ValueError`.
- Calling `savefig()` **after** `show()` → blank image.
- Overlapping labels → use `fig.tight_layout()` or `plt.xticks(rotation=45)`.
- Plotting in a loop without closing figures → memory warnings; use `plt.close()`.
- Using `plt.figure(figsize=...)` **after** the plot call → size is ignored.

---

## 🚀 What's Next?

- **Seaborn** — prettier statistical charts built on Matplotlib
- **Plotly** — interactive, web-based charts
- **Pandas** — load real data and plot it directly with `df.plot()`

Happy plotting! 🎨
