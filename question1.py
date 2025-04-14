import matplotlib.pyplot as plt
import numpy as np
import random
import math
from IPython.display import display, HTML
import json
import pathlib

def load_config(fname):
    d = {}
    if pathlib.Path(fname).is_file():
        with open(fname, "r") as f:
            d = json.load(f)
    else:
        id = input("Student Id: ")
        name = input("Student Name: ")
        d["student_id"] = id
        d["student_name"] = name
        with open(fname, "w") as f:
            json.dump(d, f)
    return d

# Load config
config = load_config("config.json")
print(config)

# Define CMAC cell structure
cells = [
    {"name": "A", "value": 1.0, "min": 0.00, "max": 2.00},
    {"name": "B", "value": 1.0, "min": 2.00, "max": 4.00},
    {"name": "C", "value": 1.0, "min": 4.00, "max": 6.00},
    {"name": "D", "value": 0.0, "min": 6.00, "max": 8.00},
    {"name": "E", "value": 1.0, "min": 8.00, "max": 10.00},
    {"name": "F", "value": 0.0, "min": 0.00, "max": 0.67},
    {"name": "G", "value": 1.0, "min": 0.67, "max": 2.67},
    {"name": "H", "value": 1.0, "min": 2.67, "max": 4.67},
    {"name": "I", "value": 1.0, "min": 4.67, "max": 6.67},
    {"name": "J", "value": 0.0, "min": 6.67, "max": 8.67},
    {"name": "K", "value": 0.0, "min": 8.67, "max": 10.00},
    {"name": "L", "value": 1.0, "min": 0.00, "max": 1.33},
    {"name": "M", "value": 1.0, "min": 1.33, "max": 3.33},
    {"name": "N", "value": 0.0, "min": 3.33, "max": 5.33},
    {"name": "O", "value": 1.0, "min": 5.33, "max": 7.33},
    {"name": "P", "value": 0.0, "min": 7.33, "max": 9.33},
    {"name": "Q", "value": 1.0, "min": 9.33, "max": 10.00}
]

# Function to calculate CMAC output
def cmac_output(p, cell_table):
    active = [cell for cell in cell_table if cell["min"] <= p < cell["max"]]
    total_output = sum(cell["value"] for cell in active)
    return total_output, active

# Input and parameters
p = 6.22
alpha = 1.10
desired_output = 0.47

# Original output and active cells
output, active_cells = cmac_output(p, cells)
print(f"\nOriginal CMAC output for p = {p}: {output}")
print("Active cells:", [c["name"] for c in active_cells])

# Error and weight update
error = desired_output - output
delta = alpha * error / len(active_cells)

# Apply update
for cell in active_cells:
    cell["value"] += delta

# Updated output
updated_output, _ = cmac_output(p, cells)
print(f"\nUpdated CMAC output for p = {p}: {updated_output:.3f}")
print("\nUpdated cells:")
for cell in active_cells: