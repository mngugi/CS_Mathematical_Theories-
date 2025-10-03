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

