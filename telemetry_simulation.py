import time
import matplotlib.pyplot as plt
from collections import deque

NUM_SATELLITES = 3
NUM_CELLS = 7
SHIFT_INTERVAL_SECONDS = 90  # update interval
SATELLITE_TO_PLOT = 1  # The satellite number (1-indexed) we want to visualize

arrays = [
    deque(range(0, 7)),          # Satellite 1
    deque(range(10, 17)),        # Satellite 2
    deque(range(20, 27)),        # Satellite 3
]

# This will now store the complete array state at each timestamp for each satellite.
history = {f"sat_{i+1}": [] for i in range(NUM_SATELLITES)}
timestamps = []


def cyclic_shift_and_log():
    print(f"--- {time.strftime('%Y-%m-%d %H:%M:%S')} ---")
    print("Performing +1 cyclic left shift...")

    for i, arr in enumerate(arrays):
        # Perform the cyclic shift
        arr.rotate(-1)  # rotates left

        # Save a copy of the new array state after the shift
        history[f"sat_{i+1}"].append(list(arr))
        print(f"Satellite {i+1} new state: {list(arr)}")

    print("Shift complete.\n")


def create_and_show_plot():
    # A line plot requires at least two points to be meaningful.
    if len(timestamps) < 2:
        print("No data to plot yet.")
        return

    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(12, 7))

    start_time = timestamps[0]
    relative_times = [(t - start_time) for t in timestamps]

    # --- Plot all cells for a single, specified satellite ---
    sat_key = f"sat_{SATELLITE_TO_PLOT}"
    if sat_key not in history:
        print(f"Error: Satellite {SATELLITE_TO_PLOT} not found in history.")
        return

    # Loop through each cell index (0 to 6)
    for cell_index in range(NUM_CELLS):
        # For the current cell_index, extract its value from every historical state
        cell_history = [state[cell_index] for state in history[sat_key]]
        ax.plot(relative_times, cell_history, marker='o', linestyle='--', label=f'Cell {cell_index}')

    ax.set_title(f'All Cell Values Over Time for Satellite {SATELLITE_TO_PLOT}', fontsize=16)
    ax.set_xlabel(f'Time (seconds) - Updates every {SHIFT_INTERVAL_SECONDS}s', fontsize=12)
    ax.set_ylabel('Cell Value', fontsize=12)
    ax.legend()
    ax.grid(True)
    
    plt.show()


def main():
    print("Starting satellite telemetry simulation...")
    print(f"A cyclic shift will occur every {SHIFT_INTERVAL_SECONDS} seconds.")

    # --- Pre-populate the initial state before the first shift ---
    print("\nLogging initial state at t=0...")
    for i, arr in enumerate(arrays):
        history[f"sat_{i+1}"].append(list(arr))
    timestamps.append(time.time())

    try:
        while True:
            cyclic_shift_and_log()
            create_and_show_plot()
            print(f"Waiting for {SHIFT_INTERVAL_SECONDS} seconds until the next shift...")
            time.sleep(SHIFT_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        timestamps.append(time.time()) # Log the final timestamp
        print("\nSimulation stopped by user. Final plot is being generated.")
        create_and_show_plot()
        print("Program exited.")

if __name__ == "__main__":
    main()