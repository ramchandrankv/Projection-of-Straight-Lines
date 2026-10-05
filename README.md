# Projection-of-Straight-Lines

This is a Python-based engineering drawing and geometry visualization tool for solving and visualizing the **orthographic projection of a straight line inclined to both the Horizontal Plane (HP) and Vertical Plane (VP)**.

The program accepts the true length, true inclinations, and position of the first point, then calculates the corresponding projections, apparent angles, position of the second point, and distance between end projectors.

It also generates a graphical representation of the construction using **Matplotlib**.

---

## Features

* Calculate **Front View (FV)** length.
* Calculate **Top View (TV)** length.
* Calculate the **true inclinations** with HP and VP.
* Calculate **apparent angles**:

  * `α` — apparent angle in Front View.
  * `β` — apparent angle in Top View.
* Calculate the position of point **B**:

  * Height above HP.
  * Distance in front of VP.
* Calculate **Distance Between End Projectors (DEP)**.
* Validate user inputs and detect geometrically invalid cases.
* Generate a visual engineering projection diagram.
* Display:

  * True Length
  * Front View
  * Top View
  * Locus lines
  * Projectors
  * True and apparent angles
  * Points `A`, `B`, `a'`, `b'`
  * Construction arcs

---

## Technologies Used

* **Python 3**
* **Matplotlib** — for graphical visualization
* **Math module** — for trigonometric and geometric calculations

---

## Project Structure

```text
GeoProjector/
│
├── projection.py
└── README.md
```

---


### Input Parameters

| Input                              | Description                                       |
| ---------------------------------- | ------------------------------------------------- |
| `True Length (TL)`                 | Actual length of the line                         |
| `True angle with HP (θ)`           | Inclination of the line with the Horizontal Plane |
| `True angle with VP (φ)`           | Inclination of the line with the Vertical Plane   |
| `Height of A above HP (a')`        | Height of point A above HP                        |
| `Distance of A in-front of VP (a)` | Distance of point A in front of VP                |

Example:

```text
True Length (TL): 100
True angle with HP (θ): 30
True angle with VP (φ): 40
Height of A above HP (a'): 20
Distance of A in-front of VP (a): 30
```

---

## Calculated Results

The program calculates the following values:

1. **True Length (TL)**
2. **True angle with HP (θ)**
3. **True angle with VP (φ)**
4. **Height of A above HP (a')**
5. **Distance of A in-front of VP (a)**
6. **Front View Length (FV)**
7. **Top View Length (TV)**
8. **Apparent angle with HP (α)**
9. **Apparent angle with VP (β)**
10. **Height of B above HP (b')**
11. **Distance of B in-front of VP (b)**
12. **Distance Between End Projectors (DEP)**

---

## Mathematical Calculations

### Front View Length

The Front View is calculated using:

```text
FV = TL × cos(φ)
```

### Top View Length

The Top View is calculated using:

```text
TV = TL × cos(θ)
```

### Height of Point B

```text
b' = a' + TL × sin(θ)
```

### Distance of Point B from VP

```text
b = a + TL × sin(φ)
```

### Apparent Angle α

```text
α = tan⁻¹(tan(θ) / cos(φ))
```

### Apparent Angle β

```text
β = tan⁻¹(tan(φ) / cos(θ))
```

The program uses Python's `math` module to perform these calculations in radians and converts the resulting angles back to degrees for display.

---

## Input Validation

The program checks for several invalid conditions before performing the projection.

### 1. Invalid Angle Combination

The program rejects cases where:

```text
θ + φ > 90°
```

and displays:

```text
INSOLVABLE
In orthographic projection, θ + φ must be <= 90° for a single line.
```

### 2. Invalid Angle Range

Both true angles must satisfy:

```text
0° ≤ θ ≤ 90°
0° ≤ φ ≤ 90°
```

### 3. Invalid True Length

The True Length must be greater than zero:

```text
TL > 0
```

### 4. Invalid User Input

Non-numeric input is rejected with an appropriate error message.

---

## Visualization

After successful input validation, GeoProjector generates a Matplotlib diagram showing the projection construction.

The diagram includes:

* **XY reference line**
* HP and VP reference positions
* Front View
* Top View
* True Length construction
* Locus lines
* End projectors
* Construction arcs
* True angles `θ` and `φ`
* Apparent angles `α` and `β`
* Points `A`, `B`, `a'`, and `b'`

The visualization is intended to make the geometric relationship between the **true line, its projections, and apparent inclinations** easier to understand.

---

## Engineering Concept

The project is based on the principles of **orthographic projection** used in engineering graphics.

A line that is inclined to both HP and VP does not generally appear at its true length in either projection.

Instead:

* The **Top View** represents the projection of the line on HP.
* The **Front View** represents the projection of the line on VP.
* The true length exists in three-dimensional space.
* The projected views have shorter apparent lengths.
* The apparent angles differ from the true inclinations.

GeoProjector combines these geometric relationships with a graphical construction to demonstrate the projection process.

---

## Future Improvements

Possible improvements for future versions include:

* Add a graphical user interface using **Tkinter** or **PyQt**.
* Allow the user to select different projection cases.
* Add support for lines parallel to HP or VP.
* Add automatic dimension annotations.
* Export projection diagrams as PNG/PDF files.
* Add 3D visualization of the actual line.
* Add interactive input controls.
* Improve geometric validation and edge-case handling.
* Add unit selection such as mm, cm, and inches.
* Separate the calculation engine from the visualization module.
* Add automated unit tests for geometric calculations.

---

## Applications

GeoProjector can be useful for:

* Engineering Graphics
* Engineering Drawing
* Technical Drawing
* Orthographic Projection
* CAD fundamentals
* Engineering education
* Geometry visualization
* Learning projection of lines inclined to HP and VP

---

## Author
Ramachandran K V

## Acknowledgements

This project uses fundamental concepts from engineering graphics and orthographic projection, implemented computationally using Python and Matplotlib.
