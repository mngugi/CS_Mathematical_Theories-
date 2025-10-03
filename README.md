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

---

Here, `A` is completely inside `B`, so `A ⊆ B`.  

If `A` is smaller but entirely inside `B`, then `A` is a **proper subset** of `B`.  

