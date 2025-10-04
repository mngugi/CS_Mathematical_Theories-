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

```markdown
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

