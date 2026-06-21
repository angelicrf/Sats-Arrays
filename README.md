# Cyclic Cell Shift for Satellites in Orbit

## Overview
This project simulates how **cells** (resource assignments) shift for satellites as they move in orbit.  
This project provides an automated simulation of satellite telemetry data. It models how **cells** (representing resource assignments or sensor readings) for a group of satellites shift in a synchronized, cyclic manner over time.

Each satellite is assigned a fixed number of discrete cells. As the satellite travels along its orbital path, the cell assignments must advance in a synchronized, cyclic manner to maintain coverage or resource allocation.
The simulation runs continuously, performing a shift at a regular interval and generating a plot to visualize the data changes over time. The entire application is containerized with Docker for easy setup and execution.

This example uses:
- **3 satellites**
- **7 cells per satellite**

The shift is triggered by user input and applied identically to all satellites at the same time.
The simulation automatically performs a shift every **90 seconds**.

## How Cell Shifting Works
## How It Works
The mechanism uses a **+1 cyclic left shift**:

- Every cell moves one position to the left.
- The cell that was at the first position (index 0) wraps around to the last position (index 6).

**Example for one satellite:**
- Before shift: `[0, 1, 2, 3, 4, 5, 6]`
- After +1 shift: `[1, 2, 3, 4, 5, 6, 0]`
- **Before shift:** `[0, 1, 2, 3, 4, 5, 6]`
- **After +1 shift:** `[1, 2, 3, 4, 5, 6, 0]`

This represents the cell assignment "pushing forward" by one slot as the satellite moves in its orbit. The same operation is performed simultaneously on all three satellites so they stay phase-aligned.
This operation is performed simultaneously on all three satellites to keep them synchronized.

## Why Save First and Last Values?
Before each shift, the original value at the **first index** and **last index** of every array is saved.  
### Telemetry Visualization
After each shift, the simulation generates a plot named `telemetry_plot.png` inside the `output` directory. This plot tracks the value of the first cell (index 0) for each satellite over time, providing a visual representation of the telemetry data.

These saved values are useful because:
- The first cell is the one being "pushed out" of the current window.
- The last cell is the position that receives the wrapped value.
- They can be used later for logging, special boundary logic, restoration, or custom manipulation.
## How to Run the Project
The project is designed to be run with Docker and Docker Compose, which handles all dependencies and setup.

## Program Behavior
The program runs in a continuous loop:
1. Shows the current state of all three satellites.
2. Asks for user input.
3. If the user enters **`1`**: performs the +1 cyclic left shift on all three arrays, then displays the new state and the saved pre-shift first/last values.
4. If the user enters **`0`**: the program exits cleanly.
5. Any other input: no shift occurs and the prompt repeats.
### Prerequisites
- Docker
- Docker Compose (usually included with Docker Desktop)

This design makes it easy to simulate multiple orbital cycles by repeatedly entering `1`.
### Steps
1.  Open a terminal or command prompt in the root directory of this project.
2.  Run the following command to build the Docker image and start the simulation container:
    ```bash
    docker-compose up --build
    ```
3.  The simulation will start, and you will see log output in your terminal every 90 seconds as a shift occurs.
4.  After the first shift, an `output` directory will be created in the project folder. Inside it, you will find `telemetry_plot.png`. This image is updated automatically after every shift.
5.  To stop the simulation, press `Ctrl+C` in the terminal.

## Example Satellite Configuration
```python
# Satellite 1
array1 = [0, 1, 2, 3, 4, 5, 6]

# Satellite 2
array2 = [10, 11, 12, 13, 14, 15, 16]

# Satellite 3
array3 = [20, 21, 22, 23, 24, 25, 26]
```
## Configuration
You can modify the simulation's parameters, such as the number of satellites or the shift interval, by editing the configuration variables at the top of the `telemetry_simulation.py` file.