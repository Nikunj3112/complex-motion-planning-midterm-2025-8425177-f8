
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
        with open(fname,"r") as f:
            d = json.load(f)
    else:
        try:
            id = input("Student Id")
        except:
            id = "123456"

        try:
            name = input("Student Name")
        except:
            name = "Jane Doe"

        d["student_id"] = id
        d["student_name"] = name
        with open(fname,"w") as f:
            json.dump(d,f)
    return d

config=load_config("config.json")
print(config)    

# <div class="question_frame"> -- start of question_frame
t = """

        <h1>Sensor Timelines</h1>
        <div class="question_body">
             
<p>Given is a simple sensor that returns either "A" or "B" whether a work piece is correct or not. The sensors are not infallible and may return an incoorect classification.</p>
<p>A secondary examination of the sensor readings also returns the number of correct readings (i.e., the accuracy result). This secondary examination is always correct.</p>

<p>For example, given are the following sensor readings and accuracy results:


<table  class="exam_marks_table" "  id="exam_marks_table" > 

        <thead>
          <tr>
        
<th>
Sequence
</th>

<th>
Sensor Readings
</th>

<th>
Num. Correct
</th>

          </tr>
        </thead>
        
<tbody>

<tr>
<td>Sensor 0</td>
<td>
['B', 'B', 'A', 'A', 'A']
</td>

<td>
3
</td>

</tr>

<tr>
<td>Sensor 1</td>
<td>
['B', 'B', 'A', 'B', 'B']
</td>

<td>
1
</td>

</tr>

<tr>
<td>Sensor 2</td>
<td>
['B', 'B', 'B', 'A', 'A']
</td>

<td>
2
</td>

</tr>

</tbody>
</table>


<p>After careful analysis, you realize that given this information, you can infer the correct readings. The solution in this simple example is: [AAAAA]. Note that the sensors always return either
'A' or 'B'.</p>

        </div><!-- end of question_body -->
    
"""
display(HTML(t))
# <div class="question_marks"><span class="mark_num">12</span> marks</div>

# Implement a program that finds the correct readings for the following experiment
# 

sensor_seqs = [['A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B'],
    ['A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A'],
    ['B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B']]
num_correct = [9, 8, 6]

def find_solutions(sensor_seqs, num_correct):
   "Find a solution for the given sensor readings and accuracy results"
   pass

sol = find_solutions(sensor_seqs, num_correct)
print("Solution", sol)

# Show your work and explain your answer in this cell.
# </div> -- end of question_frame
# <div class="question_frame"> -- start of question_frame
t = """

        <h1>Runtime Complexity</h1>
        <div class="question_body">
             
<p>Each exam 
<p>You call the routine <code>find_solutions</code> with 89 different actors. 
Each sensor reading is a list of 12 elements.
Your program takes 729088.00 milliseconds to run.
</p>

        </div><!-- end of question_body -->
    
"""
display(HTML(t))
# <div class="question_marks"><span class="mark_num">5</span> marks</div>
# Estimate the runtime of the routine find_solutions with 91 sensor sequences, each 13 readings long.
# Show your work and explain your answer in this cell.
# </div> -- end of question_frame
# <div class="question_frame"> -- start of question_frame
t = """

        <h1>Sensor Timelines II</h1>
        <div class="question_body">
            
<p>Given is a simple sensor that returns either "A" or "B" whether a work piece is correct or not. The sensors are not infallible and may return an incoorect classification.</p>
<p>A secondary examination of the sensor readings also returns the number of correct readings (i.e., the accuracy result). This secondary examination is always correct.</p>

<p>For example, given are the following sensor readings and accuracy results:


<table  class="exam_marks_table" "  id="exam_marks_table" > 

        <thead>
          <tr>
        
<th>
Sequence
</th>

<th>
Sensor Readings
</th>

<th>
Num. Correct
</th>

          </tr>
        </thead>
        
<tbody>

<tr>
<td>Sensor 0</td>
<td>
['B', 'B', 'A', 'A', 'A']
</td>

<td>
3
</td>

</tr>

<tr>
<td>Sensor 1</td>
<td>
['B', 'B', 'A', 'B', 'B']
</td>

<td>
1
</td>

</tr>

<tr>
<td>Sensor 2</td>
<td>
['B', 'B', 'B', 'A', 'A']
</td>

<td>
2
</td>

</tr>

</tbody>
</table>


<p>After careful analysis, you realize that given this information, you can infer the correct readings. Note that the sensors always return either
'A' or 'B'.</p>

<p>Your colleague informs you that the sensor sequences that she showed you was just an example. 
The readings from the sensors are much longer.
Each experiment will produce about 162 readings, where each sequence is 81 readings long.</p>

<p>You had initially connsidered using a brute-force approach to find the correct readings, but now realize that this would approach would take far too long
to return a solution.</p>

<p>Further investigation of the accuracies (which are sorted by the number of correct readings) give you an idea of speeding up your program.</p>

        </div><!-- end of question_body -->
    
"""
display(HTML(t))
# <div class="question_marks"><span class="mark_num">15</span> marks</div>

# Implement a program that finds the correct readings for the following experiment
# 

sensor_seqs = [['A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B'],
    ['B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B'],
    ['A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A'],
    ['A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B'],
    ['B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B'],
    ['A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A'],
    ['B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B'],
    ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A'],
    ['B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A'],
    ['B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A'],
    ['A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B'],
    ['A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B'],
    ['A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A'],
    ['B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A'],
    ['B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A'],
    ['B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A'],
    ['B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B'],
    ['B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    ['A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ['B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B'],
    ['A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B'],
    ['A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A'],
    ['A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B'],
    ['B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B'],
    ['B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B'],
    ['A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B'],
    ['A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A'],
    ['B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
    ['B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B'],
    ['B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B'],
    ['A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B'],
    ['B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B'],
    ['A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B'],
    ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B'],
    ['B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ['A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B'],
    ['A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A'],
    ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A'],
    ['A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B'],
    ['A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A'],
    ['A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B'],
    ['B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B'],
    ['A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B'],
    ['A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A'],
    ['B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B'],
    ['A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A'],
    ['A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B'],
    ['A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B'],
    ['B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A'],
    ['B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B'],
    ['A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B'],
    ['B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A'],
    ['B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B'],
    ['A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A'],
    ['A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B'],
    ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B'],
    ['A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ['B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A'],
    ['B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B'],
    ['B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B'],
    ['A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B'],
    ['A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B'],
    ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A'],
    ['B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A'],
    ['B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B'],
    ['B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B'],
    ['B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B'],
    ['A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A'],
    ['A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A'],
    ['B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B'],
    ['B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A'],
    ['A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A'],
    ['B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B'],
    ['A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A'],
    ['B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B'],
    ['B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B'],
    ['A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A'],
    ['B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A'],
    ['B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B'],
    ['A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A'],
    ['B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A'],
    ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B'],
    ['A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B'],
    ['B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A'],
    ['A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
    ['A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B'],
    ['B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A'],
    ['B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A'],
    ['B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B'],
    ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A'],
    ['A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B'],
    ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A'],
    ['B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A'],
    ['A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A'],
    ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B'],
    ['B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A'],
    ['A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B'],
    ['B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A'],
    ['A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B'],
    ['B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A'],
    ['B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A'],
    ['A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B'],
    ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B'],
    ['B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B'],
    ['A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B'],
    ['A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A'],
    ['B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B'],
    ['B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A'],
    ['B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B'],
    ['B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B'],
    ['A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A'],
    ['B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
    ['A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A'],
    ['B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A'],
    ['B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A'],
    ['B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B'],
    ['A', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B'],
    ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B'],
    ['B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B'],
    ['B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A'],
    ['A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B'],
    ['A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A'],
    ['B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A'],
    ['B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A'],
    ['B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A'],
    ['B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B'],
    ['A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B'],
    ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B'],
    ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A'],
    ['B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
    ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A'],
    ['B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A'],
    ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A']]
num_correct = [79, 52, 51, 50, 50, 49, 49, 49, 49, 48, 48, 48, 47, 47, 47, 46, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 40, 40, 40, 40, 40, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 34, 34, 34, 34, 34, 33, 33, 33, 32, 32, 32, 32, 31, 30, 29, 29, 26]

def find_solutions_2(sensor_seqs, num_correct):
   "Find a solution for the given sensor readings and accuracy results"
   pass

sol = find_solutions_2(sensor_seqs, num_correct)
print("Solution", sol)

# Show your work and explain your answer in this cell.
# You can add additional markdown and code cells, if you want to after this cell.
# </div> -- end of question_frame