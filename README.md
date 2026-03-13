# Complex Motion Planning Midterm

This repository contains Python scripts for the Complex Motion Planning midterm exam.

## Prerequisites

- Python 3.8 or higher

## Setup Instructions (VS Code)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nikunj3112/complex-motion-planning-midterm-2025-8425177-f8.git
   cd complex-motion-planning-midterm-2025-8425177-f8
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - **Windows**: `venv\Scripts\activate`
   - **macOS/Linux**: `source venv/bin/activate`

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Open in VS Code**:
   ```bash
   code .
   ```

6. **Select the Python interpreter** in VS Code:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS)
   - Type "Python: Select Interpreter"
   - Choose the interpreter from your `venv` folder

## Running the Scripts

Run any question file directly from the terminal or VS Code:

```bash
python question1.py
python question2.py
python question3.py
python question4.py
python question5.py
```

On first run, you will be prompted to enter your Student ID and Name. This is saved to `config.json` for subsequent runs.

## Files

| File | Topic |
|------|-------|
| `question1.py` | CMAC (Cerebellar Model Articulation Controller) |
| `question2.py` | Mystery Program Solver |
| `question3.py` | Graph Algorithms (Floyd-Warshall & Adjacency Matrices) |
| `question4.py` | Quadtree Decomposition |
| `question5.py` | Sensor Timelines & Data Reconciliation |
