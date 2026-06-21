# Satellite Telemetry Simulation

This project provides a simulation environment for satellite telemetry data, specifically modeling a cyclic handoff or state change within cellular arrays of multiple satellites. It includes several methods for running and visualizing the simulation data.

## Live Demo

Explore a live, interactive version of this project on Google Colab:

[<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>](https://colab.research.google.com/drive/1oO4PaPrfZVrxoy5wmVjOtoPREKtJszkG#scrollTo=udvD53g_LvWp)

## Features

- **Multi-Satellite Simulation**: Simulates a configurable number of satellites, each with its own cellular data array.
- **Cyclic Data Shift**: Performs a `+1` cyclic left shift on the data arrays at a regular interval to simulate state changes or telemetry handoffs.
- **Multiple Visualization Scripts**:
  - `telemetry_simulation.py`: A command-line script that plots the historical values of all cells for a single, specified satellite.
  - `telemetry_notebook.ipynb`: An interactive Jupyter Notebook that provides a live-updating plot of the first cell's value from all satellites.
  - `shiftarray.py`: An IPython/Jupyter script that visualizes the current state of all cells for all satellites at a specific moment in time.
- **Containerized Environment**: Uses Docker and Docker Compose to provide a consistent, portable environment with all dependencies included, accessible via Jupyter Lab.

---

## Project Components

- `telemetry_simulation.py`:
  A standalone Python script that runs the simulation in the terminal. After each cycle, it generates and displays a plot showing the value history of all cells for a single satellite (`SATELLITE_TO_PLOT`). The simulation pauses until the plot window is closed.

- `telemetry_notebook.ipynb`:
  An interactive Jupyter Notebook designed for live visualization. It runs the simulation and continuously updates a plot within the notebook cell, showing the value history of the first cell from each satellite.

- `shiftarray.py`:
  A script designed for use in an IPython environment (like a Jupyter cell). It visualizes a snapshot of the current state of all satellites on a single graph, with cell indices on the x-axis and cell values on the y-axis.

- `docker-compose.yml` & `Dockerfile`:
  These files define the containerized environment. They build a Docker image with Python and all necessary libraries (`matplotlib`, `jupyterlab`, etc.) and run a Jupyter Lab server.

- `requirements.txt`:
  A list of all Python dependencies required to run the project locally.

---

## Getting Started

There are two primary ways to run the simulations: using Docker (recommended for ease of setup) or running locally on your machine.

### Method 1: Using Docker (Recommended)

This method uses the provided Docker setup to run a Jupyter Lab instance where you can interact with the notebooks and scripts.

1.  **Prerequisites**:
    - Docker
    - Docker Compose

2.  **Build and Run the Container**:
    Open a terminal in the project's root directory and run:

    ```bash
    docker-compose up --build
    ```

3.  **Access Jupyter Lab**:
    Open your web browser and navigate to `http://localhost:8888`.

4.  **Run a Simulation**:
    - From the file browser on the left, double-click `telemetry_notebook.ipynb` or `shiftarray.py` to open it.
    - Run the cells in the notebook to start the interactive simulation.

### Method 2: Running Locally

This method involves setting up a local Python environment and running the scripts directly.

1.  **Prerequisites**:
    - Python 3.9+

2.  **Create a Virtual Environment**:
    From the project root directory, create and activate a virtual environment.

    ```bash
    # Create the environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    # source venv/bin/activate
    ```

3.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run a Simulation**:
    - **To run the command-line script**:
      ```bash
      python telemetry_simulation.py
      ```
    - **To run the Jupyter Notebook**:
      ```bash
      jupyter lab
      ```
      Then, open `telemetry_notebook.ipynb` in the browser window that appears.
