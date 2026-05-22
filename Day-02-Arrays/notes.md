Day 2 - Array Insertion

Topics Covered:
- Insertion at Beginning
- Insertion at End
- Insertion at Specific Position

What I Learned:
- Array insertion means adding a new element into an existing array.
- Since arrays have fixed positions (index-based), inserting an element requires adjusting other elements.
- Insertion at the beginning requires shifting all elements one position to the right.
- Insertion at the end is the simplest case, as the element is added after the last index.
- Insertion at a specific position requires shifting elements from that position onwards.
- Proper index handling is important to avoid errors.

Key Concepts:
- Arrays use 0-based indexing.
- If user gives position (1-based), convert it using: index = position - 1
- Shifting is required to create space for the new element.
- For insertion:
  - Beginning → shift all elements right
  - End → no shifting required
  - Middle → shift elements from that position to the right
- Boundary conditions are important:
  - Position should be between 1 and n+1
- Invalid positions can cause index errors.

Types of Insertion:

1. Insertion at Beginning:
- New element is added at index 0
- All existing elements are shifted one step to the right
- Time complexity: O(n)

2. Insertion at End:
- Element is added at the last position
- No shifting required
- Time complexity: O(1)

3. Insertion at Specific Position:
- Element is inserted at a given index
- Elements from that index are shifted right
- Time complexity: O(n)

Key Insight:
Insertion operations show how arrays manage data internally.
Shifting elements is the core idea behind insertion, which impacts performance.

Why This Matters:
- Helps in understanding memory management in arrays
- Forms the base for solving array manipulation problems
- Important for coding interviews and real-world applications
- Used in building more complex data structures