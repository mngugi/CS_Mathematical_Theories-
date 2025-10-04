# Computer Science Mathematical Theory

## Introduction

### 1.0 Set Theory

A **set** is an unordered collection of discrete objects (called *elements* or *members*).

Key properties of sets:
- Notation uses curly braces `{}`  
- Elements are separated by commas  
- Order does not matter  
- Duplicates are ignored  

#### Example  
A set of natural numbers:  

`A = {0, 1, 3, 6, 9}`  

#### Membership  
- `0 ∈ A` → 0 is an element of A  
- `2 ∉ A` → 2 is not an element of A

  ---
  ## Definition of Set Equality

Two sets A and B are equal if:  

`A = B ⟺ (∀x (x ∈ A ⟺ x ∈ B))`  

**In words:** every element of A is in B, and every element of B is in A.  

---

### Key Points

- **Order doesn’t matter:**  
  `{1,2,3} = {3,2,1}`  

- **Duplicates don’t matter:**  
  `{1,2,2,3} = {1,2,3}`  

- Only the contents (unique elements) matter.  

---

### Examples

- `{a,b,c} = {c,a,b}` ✅ (same elements, different order)  
- `{1,2,3} = {1,1,2,3,3}` ✅ (duplicates ignored)  
- `{1,2,3} ≠ {1,2,4}` ❌ (different contents)  

---
## Definition of the Empty Set

The **empty set** (also called the null set) is the set that contains **no elements**.  

- It is denoted by the symbol `∅` or by `{ }`.  
- By definition: `∀x (x ∉ ∅)` — no element belongs to the empty set.  

---

### Key Points

- `∅` has **zero elements**.  
- `∅` is a subset of **every set**.  
- The empty set is **unique** (there is only one).  

---

### Examples

- `A = { } = ∅`  
- `B = {1, 2, 3}`  
  - Here, `∅ ⊆ B` (empty set is a subset of B).  
- But: `∅ ≠ {∅}`  
  - `∅` has no elements.  
  - `{∅}` has one element (the empty set itself).  
---
### Summary
## Definition of a Subset

A set `A` is a **subset** of a set `B` if **every element of A is also an element of B**.  

Notation: `A ⊆ B`  

- This means: `∀x (x ∈ A ⟹ x ∈ B)`  
- If `A ⊆ B` and `A ≠ B`, then `A` is a **proper subset** of `B`.  

---

### Key Points

- Every set is a subset of itself: `A ⊆ A`  
- The empty set is a subset of every set: `∅ ⊆ A`  
- If `A ⊆ B` and `B ⊆ A`, then `A = B`  

---

### Examples

- `A = {1,2}` , `B = {1,2,3}` → `A ⊆ B` ✅  
- `A = {1,4}` , `B = {1,2,3}` → `A ⊆ B` ❌ (4 ∉ B)  
- `∅ ⊆ {1,2,3}` ✅  

---

### Visual Intuition

Think of sets as circles:

```markdown
     ┌───────────┐
     │     B     │
     │  ┌─────┐  │
     │  │  A  │  │
     │  └─────┘  │
     └───────────┘
```

---

Here, `A` is completely inside `B`, so `A ⊆ B`.  

If `A` is smaller but entirely inside `B`, then `A` is a **proper subset** of `B`.

---


## Definition of Membership

If an object `x` belongs to a set `A`, we say `x` is a **member** (or **element**) of `A`.  

Notation:  
- `x ∈ A` means *x is an element of A*  
- `x ∉ A` means *x is not an element of A*  

---

### Key Points

- Membership checks **whether an element is inside a set**.  
- Membership is about **elements**, not subsets.  

---

### Examples

- If `A = {1, 2, 3}`:  
  - `2 ∈ A` ✅ (2 is in the set)  
  - `4 ∉ A` ❌ (4 is not in the set)  

- If `B = {a, b, c}`:  
  - `a ∈ B` ✅  
  - `d ∉ B` ❌  

---

### Visual Intuition


Set A = {1, 2, 3}

   ┌─────────────┐
   │  ●  ●  ●    │
   │ 1  2  3     │
   └─────────────┘

Here:
- 2 ∈ A  (2 is inside the circle)  
- 4 ∉ A  (4 is outside the circle)  
---

Set Membership

- Set membership is the relationship that shows whether an element belongs to a set or not.

- Let A be a set and x an element.
- If x is one of the elements contained in A, we say x is a member of A, written as:

---
### Sets and Infinities

A **set** is a well-defined collection of distinct objects. These objects are called **elements** or **members** of the set.

Example:  
A = {1, 2, 3, 4, 5}

Here, 1 ∈ A means 1 is an element of A.  
6 ∉ A means 6 is not an element of A.

---

### Finite and Infinite Sets

A set is **finite** if it has a definite number of elements.  
Example:  
B = {2, 4, 6, 8, 10}  
The number of elements in B is 5, so B is finite.

A set is **infinite** if it has an endless number of elements.  
Example:  
N = {1, 2, 3, 4, 5, 6, 7, …}  
The ellipsis (…) means the set continues forever without an end.

---

### Types of Infinite Sets

1. **Countably Infinite Sets**  
   A set is countably infinite if its elements can be matched one-to-one with the natural numbers.  
   Example:  
   N = {1, 2, 3, 4, …}  
   Z = {…, -3, -2, -1, 0, 1, 2, 3, …}  
   Both can be counted even though they are infinite.

2. **Uncountably Infinite Sets**  
   A set is uncountably infinite if its elements cannot be listed or paired with natural numbers.  
   Example:  
   R = {x | x is a real number}  
   Between any two real numbers, there are infinitely many more real numbers.

---

### Visual Intuition

Finite set → ends  
Infinite set → never ends  

Think of counting:  
You can count 1, 2, 3, 4, 5 — that’s finite.  
But try counting all numbers forever — that’s infinite.

---

### Infinity (∞)

Infinity (∞) is not a number but a concept meaning “without end.”  
It represents a quantity larger than any finite number.

Examples:  
- The number of points on a line = ∞  
- The number of stars in the universe (approximately infinite)  

---

### Important Notes

- Finite sets can be measured or counted.  
- Infinite sets cannot be completed by counting.  
- Some infinite sets are larger than others (for example, real numbers are more numerous than natural numbers).  
- Infinity is a concept used in mathematics to represent limitless growth or size.

---
### Complex Sets

A **complex set** is a set that contains complex numbers as its elements.  
A **complex number** is any number that can be written in the form:

z = a + bi  

where:  
- a is the **real part**  
- b is the **imaginary part**  
- i is the **imaginary unit**, defined by i² = -1  

---

### Example of a Complex Set

Let  
C = {2 + 3i, 4 - i, -1 + 2i, 0 + i}

Here,  
Re(C) = {2, 4, -1, 0} → the set of real parts  
Im(C) = {3, -1, 2, 1} → the set of imaginary parts  

---

### Set Representation on the Complex Plane

Each complex number can be represented as a **point** on the **complex plane**,  
where:  
- The x-axis represents the real part (Re).  
- The y-axis represents the imaginary part (Im).

Example visualization (conceptually):  
(2, 3) → represents 2 + 3i  
(4, -1) → represents 4 - i  

So the set C can be visualized as a group of points on the plane.

---

### Operations on Complex Sets

1. **Union (C₁ ∪ C₂)**  
   Combines all unique complex numbers from both sets.

   Example:  
   C₁ = {1 + i, 2 + 2i}  
   C₂ = {2 + 2i, 3 + 3i}  
   C₁ ∪ C₂ = {1 + i, 2 + 2i, 3 + 3i}

2. **Intersection (C₁ ∩ C₂)**  
   Contains only complex numbers common to both sets.

   Example:  
   C₁ ∩ C₂ = {2 + 2i}

3. **Difference (C₁ − C₂)**  
   Contains complex numbers that belong to C₁ but not C₂.

   Example:  
   C₁ − C₂ = {1 + i}

---

### Infinite Complex Sets

Just like real numbers, complex numbers form an **infinite set**.  
The set of all complex numbers is denoted by:

ℂ = {a + bi | a, b ∈ ℝ}

Since both a and b can take any real value, ℂ is **uncountably infinite** —  
it’s as large as the set of real pairs (ℝ × ℝ).

---

### Important Notes

- Every real number is also a complex number (with b = 0).  
- Complex sets can describe geometric shapes (like circles or lines) in the complex plane.  
  Example:  
  {z ∈ ℂ | |z| = 1} → the set of all complex numbers on the **unit circle**.  
- Infinite complex sets have applications in advanced topics such as Fourier analysis, quantum mechanics, and fractals.

---

### Set Builder Notation

**Set builder notation** is a concise way of describing a set by stating the properties that its members must satisfy.  
It is written in the form:

{ x | condition on x }

which reads as “the set of all x such that the condition on x holds.”

---

### Basic Examples

1. **Finite Set Example**  
   A = {x | x is an integer and 1 ≤ x ≤ 5}  
   This means A = {1, 2, 3, 4, 5}.

2. **Even Numbers**  
   E = {x | x is an even number}  
   This can also be written as E = {x | x = 2n, n ∈ ℤ}.

3. **Multiples of 3**  
   M = {x | x = 3n, n ∈ ℕ}  
   This represents all positive multiples of 3.

---

### Set Builder with Complex Numbers

For complex numbers:

C = {z | z = a + bi, a, b ∈ ℝ}

This defines the set of all complex numbers, where “a” and “b” are real numbers.

Example of a restricted complex set:  
S = {z ∈ ℂ | |z| = 1}  
This means “the set of all complex numbers z such that the magnitude of z equals 1.”

---

### Set Builder for Geometric Shapes

1. **Real Interval**  
   A = {x ∈ ℝ | 0 < x ≤ 10}  
   The set of real numbers greater than 0 and up to 10.

2. **Circle in Complex Plane**  
   C = {z ∈ ℂ | |z − 2| = 3}  
   All complex numbers whose distance from 2 (on the real axis) is 3.

3. **Region Inside a Circle**  
   R = {z ∈ ℂ | |z| < 1}  
   The set of all complex numbers inside the unit circle.

---

### Nested Sets Example

Let  
A = {x | x ∈ ℕ and x ≤ 10}  
B = {x | x ∈ A and x is even}

Then  
B = {2, 4, 6, 8, 10}

---

### Important Notes

- “|” or “:” means “such that”.  
- Always specify the **domain** (e.g., x ∈ ℝ or x ∈ ℕ).  
- Set builder notation helps describe infinite or complex sets compactly.  
- Useful for mathematical proofs, functions, and defining domains precisely.

---
### Combining Sets

Combining sets means forming new sets from two or more existing sets using specific operations.  
The main set operations are **union**, **intersection**, **difference**, and **complement**.

---

### 1. Union of Sets (A ∪ B)

The **union** of two sets A and B is the set of all elements that are in A, or in B, or in both.

Notation:  
A ∪ B = {x | x ∈ A or x ∈ B}

Example:  
A = {1, 2, 3, 4}  
B = {3, 4, 5, 6}  
A ∪ B = {1, 2, 3, 4, 5, 6}

---

### 2. Intersection of Sets (A ∩ B)

The **intersection** of two sets A and B is the set of all elements that are common to both A and B.

Notation:  
A ∩ B = {x | x ∈ A and x ∈ B}

Example:  
A = {1, 2, 3, 4}  
B = {3, 4, 5, 6}  
A ∩ B = {3, 4}

---

### 3. Difference of Sets (A − B)

The **difference** of two sets A and B (also written A \ B) is the set of all elements that are in A but not in B.

Notation:  
A − B = {x | x ∈ A and x ∉ B}

Example:  
A = {1, 2, 3, 4}  
B = {3, 4, 5, 6}  
A − B = {1, 2}

---

### 4. Complement of a Set (A′)

The **complement** of a set A (relative to a universal set U) is the set of all elements in U that are not in A.

Notation:  
A′ = {x | x ∈ U and x ∉ A}

Example:  
U = {1, 2, 3, 4, 5, 6}  
A = {1, 3, 5}  
A′ = {2, 4, 6}

---

### 5. Symmetric Difference (A △ B)

The **symmetric difference** of two sets is the set of elements that are in either of the sets but not in both.

Notation:  
A △ B = (A − B) ∪ (B − A)

Example:  
A = {1, 2, 3}  
B = {3, 4, 5}  
A △ B = {1, 2, 4, 5}

---

### Visual Intuition (Venn Diagram Idea)

- **Union** → everything covered by both circles.  
- **Intersection** → only the overlapping region.  
- **Difference** → part of one circle excluding the overlap.  
- **Complement** → everything outside a given set.

---

### Important Notes

- All these operations follow **set laws** (like commutative and distributive laws).  
- For finite sets, results can be listed directly.  
- For infinite sets, operations are described symbolically.  
- Combining sets is a foundation for logic, probability, and database operations.

---

### Venn Diagrams

A **Venn Diagram** is a visual representation of sets and their relationships using overlapping circles.  
Each circle represents a set, and the regions where circles overlap show the relationships between the sets.

---

### 1. Single Set

For one set A inside a universal set U:

U = {1, 2, 3, 4, 5, 6, 7, 8}  
A = {2, 4, 6, 8}

Visual idea:  
A single circle (A) inside a rectangle (U).  
The shaded part inside the circle shows elements belonging to A.

---

### 2. Two Sets

Let:  
A = {1, 2, 3, 4}  
B = {3, 4, 5, 6}

#### Union (A ∪ B)
Elements in A or B or both.  
Shaded: both circles together.  
Result: {1, 2, 3, 4, 5, 6}

#### Intersection (A ∩ B)
Elements common to both A and B.  
Shaded: only the overlapping part.  
Result: {3, 4}

#### Difference (A − B)
Elements in A but not in B.  
Shaded: part of A’s circle not touching B.  
Result: {1, 2}

#### Symmetric Difference (A △ B)
Elements in A or B, but not in both.  
Shaded: both non-overlapping parts.  
Result: {1, 2, 5, 6}

---

### 3. Three Sets

Let sets A, B, and C overlap.  
Each circle represents one set.

#### Common Region
The central overlapping region (A ∩ B ∩ C) represents elements common to all three.

#### Example
A = {1, 2, 3, 4, 5}  
B = {4, 5, 6, 7}  
C = {5, 7, 8, 9}

- A ∩ B = {4, 5}  
- A ∩ C = {5}  
- B ∩ C = {5, 7}  
- A ∩ B ∩ C = {5}

---

### 4. Complement in Venn Diagram

Let U be the universal set.  
If A ⊆ U, then the **complement A′** includes everything outside circle A.

Example:  
U = {1, 2, 3, 4, 5, 6}  
A = {2, 4, 6}  
Then A′ = {1, 3, 5}

The shaded area outside the circle A represents A′.

---

### 5. Rules and Properties

1. **Commutative Laws**  
   A ∪ B = B ∪ A  
   A ∩ B = B ∩ A  

2. **Distributive Laws**  
   A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)  
   A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)  

3. **De Morgan’s Laws**  
   (A ∪ B)′ = A′ ∩ B′  
   (A ∩ B)′ = A′ ∪ B′  

---

### Important Notes

- Venn diagrams help visualize set relationships.  
- Shaded regions correspond to results of set operations.  
- They are commonly used in logic, statistics, and probability to simplify reasoning about groups.
