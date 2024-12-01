import os
import subprocess

def run_scripts_for_day(day_number):
    """
    Runs part1.py and part2.py for the specified day folder.

    Args:
        day_number (int): The day number (1 to 25).
    """
    # Validate the day number
    if not (1 <= day_number <= 25):
        print("Error: Please enter a number between 1 and 25.")
        return

    # Define the parent directory containing the day folders
    parent_directory = os.path.dirname(os.path.abspath(__file__))

    # Map the day number to the folder name (e.g., day1, day2, ..., day25)
    day_folder = f"day{day_number}"
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

    # Execute part1.py
    print(f"Running {part1_script}...")
    subprocess.run(["python", part1_script], check=True)

    # Execute part2.py
    print(f"Running {part2_script}...")
    subprocess.run(["python", part2_script], check=True)


if __name__ == "__main__":
    # Get the day number input from the user
    try:
        day_number = int(input("Enter the day number to run (1-25): ").strip())
        run_scripts_for_day(day_number)
    except ValueError:
        print("Error: Please enter a valid number between 1 and 25.")