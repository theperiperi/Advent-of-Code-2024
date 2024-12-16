import os
from flask import Flask, render_template
import markdown2

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__, template_folder=template_dir)

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
        # Look for readme file
        readme_path = f'day{day:02d}/part{part}/readme.md'
        
        if os.path.exists(readme_path):
            # Read and convert markdown to HTML
            with open(readme_path, 'r') as f:
                readme_content = f.read()
            html_content = markdown2.markdown(readme_content)
        else:
            html_content = "No readme available for this solution yet."
        
        return render_template('solution.html', 
                             day=day, 
                             part=part, 
                             readme=html_content)
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