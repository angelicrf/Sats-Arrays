import time
import itertools
import os
from copy import deepcopy

SIMULATION_INTERVAL_SECONDS = 90

OWNERSHIP_STAGES = [
    (80, 20),
    (50, 50),
    (25, 75),
    (0, 100),
]


def initialize_system_state():
    all_cells = []
    num_cells = 7

    # initialize cells for each satellite
    for sat_id in range(1, 4):  # For sat1, sat2, sat3
        base_cell_id = sat_id * 100
        for i in range(1, num_cells + 1):
            cell_id = base_cell_id + i
            ownership = {"sat1": 0, "sat2": 0, "sat3": 0}
            ownership[f"sat{sat_id}"] = 100
            all_cells.append({"cell_id": cell_id, "ownership": ownership})

    return all_cells

def print_telemetry(all_cells, stage_info):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"--- Telemetry Report: {time.strftime('%Y-%m-%d %H:%M:%S')} ---")
    print(f"Current Stage: {stage_info}\n")

    # Header
    print(f"{'Cell ID':<10} | {'Status':<15} | {'Sat 1 Coverage':<16} | {'Sat 2 Coverage':<16} | {'Sat 3 Coverage':<16}")
    print("-" * 83)

    # Sort cells for consistent display order
    sorted_cells = sorted(all_cells, key=lambda c: c['cell_id'])

    for cell in sorted_cells:
        ownership = cell["ownership"]
        # Dynamically determine status by checking if ownership is mixed
        is_exclusive = ownership[f"sat{cell['cell_id'] // 100}"] == 100
        status = "Exclusive" if is_exclusive else "Handoff Active"

        s1_cov = f"{ownership['sat1']}%"
        s2_cov = f"{ownership['sat2']}%"
        s3_cov = f"{ownership['sat3']}%"
        print(f"{cell['cell_id']:<10} | {status:<15} | {s1_cov:<16} | {s2_cov:<16} | {s3_cov:<16}")

    print("\n" + "=" * 83 + "\n")

def main():
    print("Starting satellite ownership transfer simulation...")
    
    all_cells = initialize_system_state()
    initial_state = deepcopy(all_cells) # Keep a clean copy of the initial state
    current_cell_index_to_transfer = 0
    
    # Use itertools.cycle to loop through ownership percentages (20, 50, 75, 100)
    ownership_percentage_cycle = itertools.cycle(OWNERSHIP_STAGES)

    # Print the initial state
    print_telemetry(all_cells, "Initial State")

    try:
        while True:
            handoffs = [
                (101 + current_cell_index_to_transfer, "sat1", "sat2"),
                (201 + current_cell_index_to_transfer, "sat2", "sat3"),
                (301 + current_cell_index_to_transfer, "sat3", "sat1"),
            ]
            handoff_ids = [h[0] for h in handoffs]
            print(f"--- Preparing Next Handoff Step for Cells: {handoff_ids} ---")
            print(f"Waiting {SIMULATION_INTERVAL_SECONDS} seconds for next step...")
            time.sleep(SIMULATION_INTERVAL_SECONDS)

            # Get the next ownership stage from the cycle
            next_ownership_step = next(ownership_percentage_cycle)
            giver_percent, receiver_percent = next_ownership_step

            # Apply the ownership change to all three handoff cells simultaneously
            for handoff_cell_id, giver, receiver in handoffs:
                for cell in all_cells:
                    if cell["cell_id"] == handoff_cell_id:
                        # Apply new ownership to the correct giver and receiver
                        cell["ownership"][giver] = giver_percent
                        cell["ownership"][receiver] = receiver_percent
                        break

            # Print the new state
            stage_description = f"Transferring Cells {handoff_ids} -> {giver_percent}% Giver / {receiver_percent}% Receiver"
            print_telemetry(all_cells, stage_description)

            # If a handoff is complete (receiver has 100%), advance to the next cell index
            if receiver_percent == 100:
                print(f"\n*** Handoff for cells {handoff_ids} complete! ***")
                
                # Reset the system to its initial state before starting the next handoff
                all_cells = deepcopy(initial_state)
                
                # Advance to the next cell in the sequence, wrapping around after the last one
                current_cell_index_to_transfer = (current_cell_index_to_transfer + 1) % 7
                
                print(f"*** Preparing to transfer next set of cells (index {current_cell_index_to_transfer}). ***\n")

    except KeyboardInterrupt:
        print("\nSimulation stopped by user. Exiting.")

if __name__ == "__main__":
    main()