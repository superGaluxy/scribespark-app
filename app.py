# app.py
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify, send_from_directory
import base64
import os

app = Flask(__name__)

# ----------------- ENVIRONMENT VARIABLE SETUP -----------------
API_KEY = os.environ.get('GEMINI_API_KEY')

def get_best_model():
    if not API_KEY:
        print("CRITICAL: GEMINI_API_KEY missing!")
        return None
    
    genai.configure(api_key=API_KEY)
    
    print("--- SEARCHING FOR AVAILABLE MODELS ---")
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        print(f"Allowed Models: {available_models}")
        
        # Priority wise check: 1.5 flash -> 1.5 flash latest -> pro -> any available
        priority = ['models/gemini-1.5-flash', 'models/gemini-1.5-flash-latest', 'models/gemini-pro']
        
        for p in priority:
            if p in available_models:
                print(f"INFO: Selected model {p}")
                return genai.GenerativeModel(p)
        
        # Agar koi priority model nahi mila toh pehla allowed model utha lo
        if available_models:
            print(f"INFO: Using fallback model {available_models[0]}")
            return genai.GenerativeModel(available_models[0])
            
    except Exception as e:
        print(f"ERROR listing models: {e}")
        # Last resort fallback
        return genai.GenerativeModel('gemini-pro')

# Initialize model once
model = get_best_model()

# --- Static folder ensure ---
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
os.makedirs(static_dir, exist_ok=True)

# --- Routes (Pages) ---
@app.route('/')
def home(): return render_template('index.html')

@app.route('/title-generator')
def title_generator_page(): return render_template('title-generator.html')

@app.route('/hook-generator')
def hook_generator_page(): return render_template('hook-generator.html')

@app.route('/tag-generator')
def tag_generator_page(): return render_template('tag-generator.html')

@app.route('/description-writer')
def description_writer_page(): return render_template('description-writer.html')

@app.route('/script-writer')
def script_writer_page(): return render_template('script-writer.html')

@app.route('/video-idea-finder')
def video_idea_finder_page(): return render_template('video-idea-finder.html')

@app.route('/channel-name-generator')
def channel_name_generator_page(): return render_template('channel-name-generator.html')

@app.route('/thumbnail-analyzer')
def thumbnail_analyzer_page(): return render_template('thumbnail-analyzer.html')

@app.route('/about')
def about(): return render_template('about.html')

@app.route('/privacy')
def privacy(): return render_template('privacy.html')

@app.route('/contact')
def contact(): return render_template('contact.html')

@app.route('/blog')
def blog(): return render_template('blog.html')

@app.route('/terms')
def terms(): return render_template('terms.html')

@app.route('/comment-reply-generator')
def comment_reply_generator_page(): return render_template('comment-reply-generator.html')

@app.route('/competitor-analyzer')
def competitor_analyzer_page(): return render_template('competitor-analyzer.html')

@app.route('/content-calendar')
def content_calendar_page(): return render_template('content-calendar.html')

@app.route('/engagement-analyzer')
def engagement_analyzer_page(): return render_template('engagement-analyzer.html')

@app.route('/hashtag-generator')
def hashtag_generator_page(): return render_template('hashtag-generator.html')

@app.route('/revenue-calculator')
def revenue_calculator_page(): return render_template('revenue-calculator.html')

@app.route('/seo-score-checker')
def seo_score_checker_page(): return render_template('seo-score-checker.html')

@app.route('/shorts-script-writer')
def shorts_script_writer_page(): return render_template('shorts-script-writer.html')

@app.route('/sponsorship-email-generator')
def sponsorship_email_generator_page(): return render_template('sponsorship-email-generator.html')

@app.route('/thumbnail-downloader')
def thumbnail_downloader_page(): return render_template('thumbnail-downloader.html')

@app.route('/trending-topics')
def trending_topics_page(): return render_template('trending-topics.html')

@app.route('/video-length-optimizer')
def video_length_optimizer_page(): return render_template('video-length-optimizer.html')


# --- API Routes ---

@app.route('/generate_titles', methods=['POST'])
def generate_titles():
    if not model: return jsonify({'error': 'API key not set'}), 500
    try:
        data = request.get_json()
        topic = data['topic']
        prompt = f"Generate 5 viral YouTube titles for '{topic}'."
        response = model.generate_content(prompt)
        return jsonify({'titles': response.text.strip()})
    except Exception as e:
        print(f"Generation Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/generate_hooks', methods=['POST'])
def generate_hooks():
    if not model: return jsonify({'error': 'API key not set'}), 500
    try:
        data = request.get_json()
        topic = data['topic']
        prompt = f"Generate 5 viral YouTube hooks for '{topic}'."
        response = model.generate_content(prompt)
        return jsonify({'hooks': response.text.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/analyze_thumbnail', methods=['POST'])
def analyze_thumbnail():
    if not model: return jsonify({'error': 'API key not set'}), 500
    try:
        data = request.get_json()
        image_data = data.get('image')
        if not image_data: return jsonify({'error': 'No image'}), 400
            
        header, base64_str = image_data.split(',', 1)
        mime_type = header.split(':')[1].split(';')[0]
        image_bytes = base64.b64decode(base64_str)
        
        response = model.generate_content([
            "Analyze this YouTube thumbnail and give it a score out of 10. Give 3 improvement tips.",
            {'mime_type': mime_type, 'data': image_bytes}
        ])
        return jsonify({'analysis': response.text.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Server setup
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)