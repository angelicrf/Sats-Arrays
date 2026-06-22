import time
import itertools
import os

# --- Configuration ---
SIMULATION_INTERVAL_SECONDS = 90

OWNERSHIP_STAGES = [
    (80, 20),
    (50, 50),
    (25, 75),
    (0, 100),
]

# Define the simultaneous handoffs: (Cell_ID, Giver, Receiver)
SIMULTANEOUS_HANDOFFS = [
    (101, "sat1", "sat2"),  # Sat 1 gives its Cell 101 to Sat 2
    (201, "sat2", "sat3"),  # Sat 2 gives its Cell 201 to Sat 3
    (301, "sat3", "sat1"),  # Sat 3 gives its Cell 301 to Sat 1
]

def initialize_system_state():
    """
    Initializes a list of all cells in the system.
    - Each satellite gets a block of exclusive cells (e.g., 101-107 for sat1).
    """
    all_cells = []
    num_cells = 7

    # Create exclusive cells for each satellite
    for sat_id in range(1, 4):  # For sat1, sat2, sat3
        base_cell_id = sat_id * 100
        for i in range(1, num_cells + 1):
            cell_id = base_cell_id + i
            ownership = {"sat1": 0, "sat2": 0, "sat3": 0}
            ownership[f"sat{sat_id}"] = 100
            all_cells.append({"cell_id": cell_id, "ownership": ownership})

    return all_cells

def print_telemetry(all_cells, stage_info):
    """Prints a formatted telemetry report for the current system state."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"--- Telemetry Report: {time.strftime('%Y-%m-%d %H:%M:%S')} ---")
    print(f"Current Stage: {stage_info}\n")

    # Header
    print(f"{'Cell ID':<10} | {'Status':<12} | {'Sat 1 Coverage':<16} | {'Sat 2 Coverage':<16} | {'Sat 3 Coverage':<16}")
    print("-" * 80)

    # Sort cells for consistent display order
    sorted_cells = sorted(all_cells, key=lambda c: c['cell_id'])
    handoff_cell_ids = [h[0] for h in SIMULTANEOUS_HANDOFFS]

    for cell in sorted_cells:
        ownership = cell["ownership"]
        status = "Handoff" if cell['cell_id'] in handoff_cell_ids else "Exclusive"
        s1_cov = f"{ownership['sat1']}%"
        s2_cov = f"{ownership['sat2']}%"
        s3_cov = f"{ownership['sat3']}%"
        print(f"{cell['cell_id']:<10} | {status:<12} | {s1_cov:<16} | {s2_cov:<16} | {s3_cov:<16}")

    print("\n" + "=" * 80 + "\n")

def main():
    """Main simulation loop."""
    print("Starting satellite ownership transfer simulation...")
    
    # --- State Initialization ---
    all_cells = initialize_system_state()
    
    # Use itertools.cycle to loop through ownership percentages (20, 50, 75, 100)
    # We will also cycle back to the initial state (100, 0)
    ownership_percentage_cycle = itertools.cycle(OWNERSHIP_STAGES)

    # Print the initial state (100% ownership by sat1)
    print_telemetry(all_cells, "Initial State")

    try:
        while True:
            print(f"Waiting {SIMULATION_INTERVAL_SECONDS} seconds for next step...")
            time.sleep(SIMULATION_INTERVAL_SECONDS)

            # Get the next ownership stage from the cycle
            next_ownership_step = next(ownership_percentage_cycle)
            giver_percent, receiver_percent = next_ownership_step

            # Apply the ownership change to all three handoff cells simultaneously
            for handoff_cell_id, giver, receiver in SIMULTANEOUS_HANDOFFS:
                for cell in all_cells:
                    if cell["cell_id"] == handoff_cell_id:
                        # Reset ownership before applying new percentages
                        cell["ownership"] = {"sat1": 0, "sat2": 0, "sat3": 0}
                        # Apply new ownership to the correct giver and receiver
                        cell["ownership"][giver] = giver_percent
                        cell["ownership"][receiver] = receiver_percent
                        break

            # Print the new state
            stage_description = f"Applying {giver_percent}% Giver / {receiver_percent}% Receiver Ownership"
            print_telemetry(all_cells, stage_description)

            # When the cycle resets to the initial state, print a message
            if giver_percent == 100 and receiver_percent == 0:
                print(f"\n*** HANDOFF CYCLE COMPLETE! Resetting to initial state. ***\n")

    except KeyboardInterrupt:
        print("\nSimulation stopped by user. Exiting.")

if __name__ == "__main__":
    main()