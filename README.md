# Advent of Code 2024 ⭐

## Introduction
This repository contains solutions for **Advent of Code 2024**, an annual coding event featuring 25 daily programming challenges. Each day consists of two parts (`part1.py` and `part2.py`) that incrementally build on the same problem. This project provides a script (`main.py`) to efficiently run the solutions for any specific day.

## Folder Structure
The project is organized as follows:
```
/parent_directory/
├── day1/
│   ├── input.txt
│   ├── part1.py
│   ├── part2.py
├── day2/
│   ├── input.txt
│   ├── part1.py
│   ├── part2.py
...
├── day25/
│   ├── input.txt
│   ├── part1.py
│   ├── part2.py
├── main.py
```

1. **Day Folders (`day1`, `day2`, ..., `day25`)**:
   - Each folder contains:
     - `input.txt`: The puzzle input for that day.
     - `part1.py`: Solution for the first part of the puzzle.
     - `part2.py`: Solution for the second part of the puzzle.

2. **`main.py`**:
   - The script to run solutions for a specific day by selecting the day number.

## Usage Instructions

1. **Pre-requisites**:
   - Ensure Python 3.x is installed on your system.
   - Navigate to the root directory of the project (where `main.py` is located).

2. **Running Solutions**:
   - Run the `main.py` script:
     ```bash
     python main.py
     ```
   - Enter the day number (1 to 25) when prompted:
     ```
     Enter the day number to run (1-25): 3
     ```
   - The script will:
     - Locate the corresponding day folder (`day3/` in this example).
     - Execute `part1.py` and print its output.
     - Execute `part2.py` and print its output.

3. **Error Handling**:
   - If an invalid day number (not between 1 and 25) is entered, an error message will prompt you to try again.
   - The script checks for the existence of the `day{n}` folder and the required `part1.py` and `part2.py` files.

## Example Output

For day 3:
```bash
python main.py
Enter the day number to run (1-25): 3
Running day3/part1.py...
[Output of part1]
Running day3/part2.py...
[Output of part2]
```

## Contribution

Feel free to:
- Add solutions for any missing days.
- Optimize existing solutions.
- Submit pull requests or issues for improvements.

## License

This project is distributed under the MIT License. See `LICENSE` for details.
