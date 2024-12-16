# Advent of Code 2024 ⭐

## Introduction
This repository contains solutions for **Advent of Code 2024**, an annual coding event featuring 25 daily programming challenges. Each day consists of two parts with detailed solutions and explanations. The project includes both a solution runner (`run_script.py`) and a web server (`main.py`) for accessing detailed writeups.

## Folder Structure
The project is organized as follows:

```
/parent_directory/
├── day01/
│   ├── part1/
│   │   ├── solution.py
│   │   ├── README.md
│   │   ├── writeup.txt
│   ├── part2/
│   │   ├── solution.py
│   │   ├── README.md
│   │   ├── writeup.txt
│   ├── input.txt
├── day02/
│   ├── part1/
│   │   ├── solution.py
│   │   ├── README.md
│   │   ├── writeup.txt
│   ├── part2/
│   │   ├── solution.py
│   │   ├── README.md
│   │   ├── writeup.txt
│   ├── input.txt
...
├── templates/
│   ├── solution.html
├── run_script.py
├── requirements.txt
```

### Day Folders
Each day contains:
- `input.txt`: The puzzle input.
- Part folders with:
  - `solution.py`: Implementation of the solution.
  - `README.md`: Detailed explanation of the approach.
  - `writeup.txt`: Plain text version of the solution explanation.

### Usage Instructions

#### Running Solutions

1. **Setup**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Viewing Solutions**:
   ```bash
   python run_script.py
   ```
   
   You'll be prompted to:
   - Enter the day number (1-25), or 'q' to quit.
   - Enter the part number (1 or 2).
   
   The script will:
   - Run the selected solution.
   - Display the solution output.
   - Show any error messages if they occur.
   - Display the total execution time.

#### Web Interface

1. **Starting the Server**:
   ```bash
   python main.py
   ```

2. **Accessing Writeups**:
   - Open your browser and navigate to `http://localhost:8000`.
   - Browse through days and parts.
   - Read detailed solution explanations from `writeup.txt`.
   - View implementation code.

## Example Outputs

Running a solution:
```bash
$ python run_script.py

Enter the day number (1-25, or 'q' to quit): 3
Enter the part number (1-2): 1

Running solution for Day 03, part1...

Output:
[Solution output here]

Timing Information:
Total execution: 0.123 seconds
```

## Solution Documentation

Each solution includes:
- Problem description.
- Approach explanation.
- Implementation details.

## Contributing

Feel free to:
- Submit improvements to existing solutions.
- Add alternative approaches.
- Enhance documentation.
- Report issues.

## License

This project is distributed under the MIT License. See `LICENSE` for details.
