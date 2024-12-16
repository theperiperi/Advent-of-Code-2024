import subprocess
import time
from datetime import datetime

def run_solution(day, part):
    path = f"day{day}/{part}/solution.py"
    print(f"\nRunning solution for Day {day}, {part}...")
    
    # Record start time
    start_time = time.time()
    
    # Run the solution and capture output
    try:
        # Run the solution and capture both stdout and stderr
        result = subprocess.run(['python', path], 
                              capture_output=True, 
                              text=True)
        
        # Print the output
        if result.stdout:
            print("\nOutput:")
            print(result.stdout)
        
        # Print any errors
        if result.stderr:
            print("\nErrors:")
            print(result.stderr)
            
        # Calculate timing
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Print timing information
        print("\nTiming Information:")
        print(f"Total execution: {execution_time:.3f} seconds")
        
    except FileNotFoundError:
        print(f"Error: Could not find solution file at {path}")
    except Exception as e:
        print(f"Error running solution: {str(e)}")

def main():
    while True:
        day = input("\nEnter the day number (1-25, or 'q' to quit): ")
        
        if day.lower() == 'q':
            break
            
        if not day.isdigit() or not (1 <= int(day) <= 25):
            print("Invalid input. Please enter a number between 1 and 25.")
            continue
            
        # Format day to two digits
        day = f"{int(day):02}"
        
        # Get part number
        part = input("Enter the part number (1-2): ")
        if not part in ['1', '2']:
            print("Invalid part number. Please enter 1 or 2.")
            continue
            
        part = f"part{part}"
        
        # Run the selected solution
        run_solution(day, part)

if __name__ == "__main__":
    main()