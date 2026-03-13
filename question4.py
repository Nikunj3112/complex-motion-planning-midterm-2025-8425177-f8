import matplotlib.pyplot as plt
import numpy as np
import math
import json
import pathlib
from IPython.display import display, HTML

def load_config(fname="config.json"):
    """
    Load or create a config file containing student name and ID.
    """
    config_data = {}
    path = pathlib.Path(fname)

    if path.is_file():
        with open(fname, "r") as f:
            config_data = json.load(f)
    else:
        try:
            student_id = input("Student Id: ")
        except:
            student_id = "123456"

        try:
            student_name = input("Student Name: ")
        except:
            student_name = "Jane Doe"

        config_data = {"student_id": student_id, "student_name": student_name}
        with open(fname, "w") as f:
            json.dump(config_data, f)

    return config_data


# Load student info
config = load_config()
print("Loaded config:", config)


# Quadtree task description
t = """
<h2>Quadtree Decomposition</h2>
<p>
The grid world is a simple environment. Agents can move in either the "up", "down", "left", or 
"right" direction. The agent cannot move diagonally. Some cells are occupied by obstacles.
</p>
<p>
The Quadtree decomposition of the environment splits the grid recursively into 4 quadrants until
all cells in a region are the same, or the region size is 1x1. Count the number of leaf cells of
each size (1x1, 2x2, 4x4, etc.).
</p>
"""
display(HTML(t))


# The given 8x8 maze
maze = [[0, 0, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1, 1]]

def is_homogeneous(grid):
    flat = [cell for row in grid for cell in row]
    return all(val == flat[0] for val in flat)

def quadtree(grid, counts):
    size = len(grid)
    if size == 1 or is_homogeneous(grid):
        log_size = int(math.log2(size))
        counts[log_size] += 1
        return

    mid = size // 2
    quadrants = [
        [row[:mid] for row in grid[:mid]],  # Top-left
        [row[mid:] for row in grid[:mid]],  # Top-right
        [row[:mid] for row in grid[mid:]],  # Bottom-left
        [row[mid:] for row in grid[mid:]],  # Bottom-right
    ]

    for quad in quadrants:
        quadtree(quad, counts)

def calc_quadtree_sizes(maze):
    size = len(maze)
    max_power = int(math.log2(size))
    counts = [0] * (max_power + 1)  # counts[0] = 1x1, counts[1] = 2x2, etc.
    quadtree(maze, counts)
    return counts

# Calculate solution
sol = calc_quadtree_sizes(maze)

# Print results
for i, n in enumerate(sol):
    print(f"{2**i}x{2**i} cells: {n}")
