# Cyclic Cell Shift for Satellites in Orbit

## Overview
This project simulates how **cells** (resource assignments) shift for satellites as they move in orbit.  

Each satellite is assigned a fixed number of discrete cells. As the satellite travels along its orbital path, the cell assignments must advance in a synchronized, cyclic manner to maintain coverage or resource allocation.

This example uses:
- **3 satellites**
- **7 cells per satellite**

The shift is triggered by user input and applied identically to all satellites at the same time.

## How Cell Shifting Works
The mechanism uses a **+1 cyclic left shift**:

- Every cell moves one position to the left.
- The cell that was at the first position (index 0) wraps around to the last position (index 6).

**Example for one satellite:**
- Before shift: `[0, 1, 2, 3, 4, 5, 6]`
- After +1 shift: `[1, 2, 3, 4, 5, 6, 0]`

This represents the cell assignment "pushing forward" by one slot as the satellite moves in its orbit. The same operation is performed simultaneously on all three satellites so they stay phase-aligned.

## Why Save First and Last Values?
Before each shift, the original value at the **first index** and **last index** of every array is saved.  

These saved values are useful because:
- The first cell is the one being "pushed out" of the current window.
- The last cell is the position that receives the wrapped value.
- They can be used later for logging, special boundary logic, restoration, or custom manipulation.

## Program Behavior
The program runs in a continuous loop:
1. Shows the current state of all three satellites.
2. Asks for user input.
3. If the user enters **`1`**: performs the +1 cyclic left shift on all three arrays, then displays the new state and the saved pre-shift first/last values.
4. If the user enters **`0`**: the program exits cleanly.
5. Any other input: no shift occurs and the prompt repeats.

This design makes it easy to simulate multiple orbital cycles by repeatedly entering `1`.

## Example Satellite Configuration
```python
# Satellite 1
array1 = [0, 1, 2, 3, 4, 5, 6]

# Satellite 2
array2 = [10, 11, 12, 13, 14, 15, 16]

# Satellite 3
array3 = [20, 21, 22, 23, 24, 25, 26]
