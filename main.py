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
        # Look for writeup file instead of README.md
        writeup_path = f'day{day:02d}/part{part}/writeup.txt'
        
        if os.path.exists(writeup_path):
            # Read the content of writeup.txt
            with open(writeup_path, 'r') as f:
                writeup_content = f.read()
            
            # Replace line breaks with Markdown line breaks
            # This ensures that paragraphs are separated correctly
            writeup_content = writeup_content.replace('\n\n', '\n\n')  # Double line breaks for paragraphs
            writeup_content = writeup_content.replace('\n', '  \n')  # Single line breaks for line breaks in Markdown
            
            # Convert the modified content to HTML
            writeup_html = markdown2.markdown(writeup_content)
        else:
            writeup_html = "No writeup available for this solution yet."
        
        return render_template('solution.html', 
                               day=day, 
                               part=part, 
                               readme=writeup_html)  # Pass the HTML content
    except Exception as e:
        print(f"Error: {str(e)}")  # Add debug output
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    print("Starting Flask server...")  # Add debug output
    app.run(
        host='0.0.0.0',  # Allow all incoming connections
        port=5000,       # Use port 5000
        threaded=True    # Enable threading
    )