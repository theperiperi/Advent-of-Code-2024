import os

# Define the base directory where the day folders are located
base_dir = '/Users/periperi/Desktop/Advent-of-Code-2024'  # Update this to your actual path

# Iterate through each day folder
for day in range(1, 21):  # Assuming you have folders from day 1 to day 20
    day_folder = f'day{day:02d}'
    for part in ['part1', 'part2']:
        # Construct the full path to the writeup file
        old_file_path = os.path.join(base_dir, day_folder, part, 'writeup.md')
        new_file_path = os.path.join(base_dir, day_folder, part, 'README.md')
        
        # Check if the old file exists before renaming
        if os.path.exists(old_file_path):
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {old_file_path} to {new_file_path}')
        else:
            print(f'File not found: {old_file_path}')