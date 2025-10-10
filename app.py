# app.py

import google.generativeai as genai
from flask import Flask, render_template, request, jsonify, send_from_directory
import os # API Key ko safely manage karne ke liye

# Flask app ko initialize karte hain
app = Flask(__name__)

# ----------------- VERY IMPORTANT -----------------
# Ab hum API key ko seedha yahan nahi likhenge.
# Hum Render ke "Environment Variables" se isey lenge.
API_KEY = os.environ.get('GEMINI_API_KEY')
# ----------------------------------------------------

# Gemini API ko configure karte hain
if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    print("WARNING: GEMINI_API_KEY is not set.")

# AI model ko select karte hain
model = genai.GenerativeModel('gemini-pro')

# --- Page Routes (No changes here) ---
@app.route('/')
def home():
    return render_template('index.html')
# ... baaki saare page routes bilkul waise hi rahenge ...
@app.route('/title-generator')
def title_generator_page():
    return render_template('title-generator.html')

@app.route('/thumbnail-downloader')
def thumbnail_downloader_page():
    return render_template('thumbnail-downloader.html')

@app.route('/description-writer')
def description_writer_page():
    return render_template('description-writer.html')
    
@app.route('/script-writer')
def script_writer_page():
    return render_template('script-writer.html')

@app.route('/video-idea-finder')
def video_idea_finder_page():
    return render_template('video-idea-finder.html')

@app.route('/tag-generator')
def tag_generator_page():
    return render_template('tag-generator.html')

@app.route('/channel-name-generator')
def channel_name_generator_page():
    return render_template('channel-name-generator.html')

@app.route('/thumbnail-analyzer')
def thumbnail_analyzer_page():
    return render_template('thumbnail-analyzer.html')
    
@app.route('/blog')
def blog_page():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# --- API Routes (No changes here) ---
@app.route('/generate_hooks', methods=['POST'])
def generate_hooks():
    if not API_KEY:
        return jsonify({'error': 'API key not configured on the server.'}), 500
    try:
        data = request.get_json()
        video_topic = data['topic']
        video_tone = data.get('tone', 'Engaging')
        prompt = f"Generate 5 viral YouTube hooks for a video about '{video_topic}'. The tone should be: {video_tone}. Each hook must be on a new line and nothing else."
        response = model.generate_content(prompt)
        return jsonify({'hooks': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_hooks: {e}")
        return jsonify({'error': 'An error occurred. Please check your API key.'}), 500

# ... baaki saare API routes bilkul waise hi rahenge ...
@app.route('/generate_titles', methods=['POST'])
def generate_titles():
    # ... code ...
    pass
@app.route('/generate_description', methods=['POST'])
def generate_description():
    # ... code ...
    pass
@app.route('/generate_script', methods=['POST'])
def generate_script():
    # ... code ...
    pass
@app.route('/generate_ideas', methods=['POST'])
def generate_ideas():
    # ... code ...
    pass
@app.route('/generate_tags', methods=['POST'])
def generate_tags():
    # ... code ...
    pass
@app.route('/generate_channel_name', methods=['POST'])
def generate_channel_name():
    # ... code ...
    pass
@app.route('/analyze_thumbnail', methods=['POST'])
def analyze_thumbnail():
    # ... code ...
    pass
@app.route('/generate_hashtags', methods=['POST'])
def generate_hashtags():
    # ... code ...
    pass


# Server ko run karte hain
if __name__ == '__main__':
    app.run(debug=True, port=8080)

