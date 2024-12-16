from flask import Flask, render_template
import os
import markdown2

app = Flask(__name__, 
           static_folder='static',  # Add static folder support
           template_folder='templates')  # Explicitly set template folder

def get_available_days():
    days = []
    for folder in os.listdir('.'):
        if folder.startswith('day') and os.path.isdir(folder):
            day_num = int(folder[3:])
            days.append(day_num)
    return sorted(days)

@app.route('/')
def index():
    days = get_available_days()
    return render_template('index.html', days=days)

@app.route('/day/<int:day>/part/<int:part>')
def run_solution(day, part):
    try:
        # Look for writeup file
        writeup_path = f'day{day:02d}/part{part}/writeup.md'
        
        if os.path.exists(writeup_path):
            # Read and convert markdown to HTML
            with open(writeup_path, 'r') as f:
                writeup_content = f.read()
            html_content = markdown2.markdown(writeup_content)
        else:
            html_content = "No writeup available for this solution yet."
        
        return render_template('solution.html', 
                             day=day, 
                             part=part, 
                             writeup=html_content)
    except Exception as e:
        print(f"Error: {str(e)}")  # Add debug output
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    print("Starting Flask server...")  # Add debug output
    app.run(
        debug=True,
        host='0.0.0.0',  # Allow all incoming connections
        port=5000,       # Use port 5000
        threaded=True    # Enable threading
    )