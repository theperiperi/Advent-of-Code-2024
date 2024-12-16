import os
import subprocess
import time

def run_scripts_for_day(day_number):
    """
    Runs part1.py and part2.py for the specified day folder and measures execution time.

    Args:
        day_number (int): The day number (1 to 25).
    """
    # Validate the day number
    if not (1 <= day_number <= 25):
        print("Error: Please enter a number between 1 and 25.")
        return

    # Define the parent directory containing the day folders
    parent_directory = os.path.dirname(os.path.abspath(__file__))

    # Map the day number to the folder name with zero padding for single digits
    day_folder = f"day{day_number:02d}"  # This will create day01, day02, etc.
    day_folder_path = os.path.join(parent_directory, day_folder)

    # Check if the folder exists
    if not os.path.isdir(day_folder_path):
        print(f"Error: Folder {day_folder} does not exist.")
        return

    # Paths to part1.py and part2.py
    part1_script = os.path.join(day_folder_path, "part1.py")
    part2_script = os.path.join(day_folder_path, "part2.py")

    # Check if part1.py and part2.py exist
    if not os.path.isfile(part1_script):
        print(f"Error: {part1_script} does not exist.")
        return
    if not os.path.isfile(part2_script):
        print(f"Error: {part2_script} does not exist.")
        return

    # Execute and time part1.py
    print(f"\nRunning {part1_script}...")
    start_time = time.time()
    subprocess.run(["python3", part1_script], check=True)
    end_time = time.time()
    part1_duration = end_time - start_time
    print(f"Part 1 completed in {part1_duration:.3f} seconds")

    # Execute and time part2.py
    print(f"\nRunning {part2_script}...")
    start_time = time.time()
    subprocess.run(["python3", part2_script], check=True)
    end_time = time.time()
    part2_duration = end_time - start_time
    print(f"Part 2 completed in {part2_duration:.3f} seconds")

    # Print total execution time
    total_duration = part1_duration + part2_duration
    print(f"\nTotal execution time: {total_duration:.3f} seconds")


if __name__ == "__main__":
    # Get the day number input from the user
    try:
        day_number = int(input("Enter the day number to run (1-25): ").strip())
        run_scripts_for_day(day_number)
    except ValueError:
        print("Error: Please enter a valid number between 1 and 25.")