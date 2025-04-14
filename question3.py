import matplotlib.pyplot as plt
import numpy as np
import json
import pathlib
from IPython.display import display, HTML

def load_config(fname="config.json"):
    """
    Load student configuration from file, or prompt for input if file doesn't exist.
    """
    config_data = {}
    config_path = pathlib.Path(fname)

    if config_path.is_file():
        with open(fname, "r") as f:
            config_data = json.load(f)
    else:
        try:
            student_id = input("Student ID: ")
        except:
            student_id = "123456"

        try:
            student_name = input("Student Name: ")
        except:
            student_name = "Jane Doe"

        config_data["student_id"] = student_id
        config_data["student_name"] = student_name

        with open(fname, "w") as f:
            json.dump(config_data, f)

    return config_data



config = load_config()
print("Loaded configuration:", config)


html_turtle = """
<h2>Tim - the Turtle - Adjacency Matrix</h2>
<p>
The grid world is a simple environment. Agents can move in either the "up", "down", "left", or "right" direction.
The agent cannot move diagonally. Some cells are occupied by obstacles as shown in the figure below.
</p>
<p>
Tim, the turtle, can move one step in any of the four directions.
</p>
<pre>
maze = [[1, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
</pre>
"""
display(HTML(html_turtle))
print("Answer: 42") 

html_fw = """
<h2>Tim - the Turtle - Floyd Warshall Algorithm</h2>
<p>
The Floyd Warshall algorithm is an elegant application of dynamic programming to the problem of finding
the shortest path between any two points in a graph.
</p>
<p>
Show the output of the Floyd Warshall algorithm for the domain above.
</p>
"""
display(HTML(html_fw))
print("Answer: 42")  

html_freddy = """
<h2>Freddy - the Frog - Adjacency Matrix</h2>
<p>
Freddy, the frog, can jump either 2 or 3 squares in any of the four directions. Freddy can jump over obstacles, 
but cannot land on a cell with an obstacle. Jumping 2 or 3 squares counts as one move.
</p>
<pre>
maze = [[1, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
</pre>
"""
display(HTML(html_freddy))
print("Answer: 42")  

html_runtime = """
<h2>Floyd Warshall Algorithm Complexity</h2>
<p>
Given is a grid world domain with a size of 19 rows and 38 columns. There are 525 obstacles in the domain.
Your implementation of the Floyd Warshall takes 37636.65 seconds to complete.
Estimate the runtime if the grid increases to 38 rows and 43 columns.
</p>
"""
display(HTML(html_runtime))
print("Answer: 42") 

html_memory = """
<h2>Memory Complexity of the Floyd Warshall Algorithm</h2>
<p>
Estimate memory requirements for a grid world with 19 rows, 38 columns, and 525 obstacles.
Each cell uses 4 bytes. Obstacle cells are not represented in the table.
</p>
"""
display(HTML(html_memory))
print("Answer: 3") 

html_obstacles = """
<h2>Impact of the Number of Obstacles</h2>
<p>
Given a grid of 19 rows and 38 columns, and a runtime of 37636.65 seconds with 525 obstacles,
estimate the runtime when the number of obstacles increases to 540.
</p>
"""
display(HTML(html_obstacles))
print("Answer: 42")  
