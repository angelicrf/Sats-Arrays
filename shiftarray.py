import time
import matplotlib.pyplot as plt
from collections import deque
from IPython.display import clear_output, display
import os

plt.style.use('seaborn-v0_8-darkgrid')
sat1 = deque([1, 2, 3])
sat2 = deque([4, 5, 6, 10, 11]) # Using different lengths to show flexibility
sat3 = deque([7, 8, 9, 12])

sats = [sat1, sat2, sat3]

fig, ax = plt.subplots(figsize=(12, 7))
cycle = 0

while True:
    ax.clear()

    for i, sat_deque in enumerate(sats):
        sat_num = i + 1
        cell_indices = range(len(sat_deque))
        cell_values = list(sat_deque) # The current values of the cells

        ax.plot(
            cell_indices,
            cell_values,
            marker='o',
            linestyle='--',
            linewidth=2,
            label=f'SAT-{sat_num}'
        )

    ax.set_title(
        f'Satellite Cell State - Cycle {cycle}',
        fontsize=18,
        pad=20
    )
    ax.set_xlabel('Cell Index', fontsize=12)
    ax.set_ylabel('Cell Value', fontsize=12)
    ax.legend(loc='upper right')
    ax.grid(True)

    clear_output(wait=True)
    display(fig)
    print(f"--- Cycle {cycle} State ---")
    for i, sat_deque in enumerate(sats):
        print(f"Satellite {i+1} state: {list(sat_deque)}")

    s1_first = sat1.popleft()
    s2_first = sat2.popleft()
    s3_first = sat3.popleft()

    sat1.append(s2_first)
    sat2.append(s3_first)
    sat3.append(s1_first)

    cycle += 1
    print(f"\nWaiting 90 seconds for next cycle...")
    time.sleep(90)