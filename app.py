# app.py
from flask import Flask, render_template, request, jsonify, send_from_directory
from google import genai  # Naya Google AI SDK
import base64
import os

app = Flask(__name__)

# ----------------- ENVIRONMENT VARIABLE SETUP -----------------
API_KEY = os.environ.get('GEMINI_API_KEY')

# Naya Client initialize karein
if API_KEY:
    client = genai.Client(api_key=API_KEY)
    print("INFO: Naya Google GenAI Client configured successfully.")
else:
    print("WARNING: GEMINI_API_KEY not found!")

# Model ka naam
MODEL_ID = "gemini-1.5-flash"

# --- Static folder ensure ---
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
os.makedirs(static_dir, exist_ok=True)

# --- Routes (Pages) ---
@app.route('/')
def home(): return render_template('index.html')

@app.route('/title-generator')
def title_generator_page(): return render_template('title-generator.html')

@app.route('/tag-generator')
def tag_generator_page(): return render_template('tag-generator.html')

@app.route('/hook-generator')
def hook_generator_page(): return render_template('hook-generator.html')

# (Baki saare routes waise hi rakhein jaise aapne pehle likhe the...)

# --- API Routes (Update Logic) ---

@app.route('/generate_titles', methods=['POST'])
def generate_titles():
    try:
        data = request.get_json()
        video_topic = data['topic']
        prompt = f"Generate 5 viral YouTube titles for '{video_topic}'."
        
        # Naya SDK call syntax
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return jsonify({'titles': response.text.strip()})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/generate_hooks', methods=['POST'])
def generate_hooks():
    try:
        data = request.get_json()
        topic = data['topic']
        prompt = f"Generate 5 viral YouTube hooks for '{topic}'."
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return jsonify({'hooks': response.text.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/analyze_thumbnail', methods=['POST'])
def analyze_thumbnail():
    try:
        data = request.get_json()
        image_data = data.get('image')
        if not image_data: return jsonify({'error': 'No image'}), 400
            
        header, base64_str = image_data.split(',', 1)
        mime_type = header.split(':')[1].split(';')[0]
        
        # Naya SDK Image call logic
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[
                "Analyze this YouTube thumbnail and give it a score out of 10.",
                {'mime_type': mime_type, 'data': base64_str}
            ]
        )
        return jsonify({'analysis': response.text.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Server setup
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)