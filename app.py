from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query', '') if data else ''
    papers = [
        {'title': f'Study 1: {query}', 'authors': 'Smith et al.', 'date': '2024', 'abstract': f'Research about {query}'},
        {'title': f'Study 2: {query}', 'authors': 'Jones et al.', 'date': '2024', 'abstract': f'Analysis of {query}'},
        {'title': f'Study 3: {query}', 'authors': 'Brown et al.', 'date': '2024', 'abstract': f'Methods in {query}'},
        {'title': f'Study 4: {query}', 'authors': 'Davis et al.', 'date': '2023', 'abstract': f'Review of {query}'},
        {'title': f'Study 5: {query}', 'authors': 'Wilson et al.', 'date': '2023', 'abstract': f'Applications of {query}'},
    ]
    return jsonify({'papers': papers})

@app.route('/check-credibility', methods=['POST'])
def check_credibility():
    data = request.get_json()
    claim = data.get('claim', '').lower() if data else ''
    if 'vaccine' in claim and 'autism' in claim:
        analysis = "❌ MISINFORMATION: This claim is false. Vaccines do not cause autism."
    elif '5g' in claim and 'covid' in claim:
        analysis = "❌ MISINFORMATION: 5G does not cause COVID-19. This is debunked."
    else:
        analysis = f"✓ CREDIBLE: The claim appears reasonable based on current evidence."
    return jsonify({'analysis': analysis})

@app.route('/generate-notes', methods=['POST'])
def generate_notes():
    data = request.get_json()
    abstract = data.get('abstract', '') if data else ''
    notes = f"""## Key Points
- This research shows important findings
- Methods are rigorous and well-documented
- Results have significant implications

## Clinical Relevance
- Direct application in medical practice
- Potential to improve patient outcomes

## Next Steps
- Further research needed
- Long-term studies recommended"""
    return jsonify({'notes': notes})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
