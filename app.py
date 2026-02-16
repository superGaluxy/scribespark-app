
```python
# app.py
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify, send_from_directory
import base64
import os

# Flask app ko initialize karte hain
app = Flask(__name__)

# ----------------- ENVIRONMENT VARIABLE SETUP -----------------
# Render Dashboard mein 'GEMINI_API_KEY' set hona chahiye
API_KEY = os.environ.get('GEMINI_API_KEY')

if not API_KEY:
    print("WARNING: API_KEY not found in environment variables!")
else:
    # Gemini API ko configure karte hain
    genai.configure(api_key=API_KEY)
    print("INFO: Gemini API configured successfully.")

# AI model ko select karte hain (Latest stable model: gemini-1.5-flash)
# Note: 'gemini-pro' purana ho gaya hai aur 404 error de sakta hai.
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Static folder ensure ---
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
os.makedirs(static_dir, exist_ok=True)

# --- SEO Routes ---
@app.route('/robots.txt')
def serve_robots():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/sitemap.xml')
def serve_sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml')

# --- Page Routes ---
@app.route('/')
def home():
    return render_template('index.html')

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

@app.route('/trending-topics')
def trending_topics_page():
    return render_template('trending-topics.html')

@app.route('/content-calendar')
def content_calendar_page():
    return render_template('content-calendar.html')

@app.route('/seo-score-checker')
def seo_score_checker_page():
    return render_template('seo-score-checker.html')

@app.route('/revenue-calculator')
def revenue_calculator_page():
    return render_template('revenue-calculator.html')

@app.route('/video-length-optimizer')
def video_length_optimizer_page():
    return render_template('video-length-optimizer.html')

@app.route('/engagement-analyzer')
def engagement_analyzer_page():
    return render_template('engagement-analyzer.html')

@app.route('/hook-generator')
def hook_generator_page():
    return render_template('hook-generator.html')

@app.route('/hashtag-generator')
def hashtag_generator_page():
    return render_template('hashtag-generator.html')

@app.route('/comment-reply-generator')
def comment_reply_generator_page():
    return render_template('comment-reply-generator.html')

@app.route('/shorts-script-writer')
def shorts_script_writer_page():
    return render_template('shorts-script-writer.html')

@app.route('/competitor-analyzer')
def competitor_analyzer_page():
    return render_template('competitor-analyzer.html')

@app.route('/blog')
def blog_page():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# --- API Routes ---

@app.route('/generate_hooks', methods=['POST'])
def generate_hooks():
    try:
        data = request.get_json()
        video_topic = data['topic']
        video_tone = data.get('tone', 'Engaging')
        prompt = f"Generate 5 viral YouTube hooks for a video about '{video_topic}'. The tone should be: {video_tone}. Each hook must be on a new line and nothing else."
        response = model.generate_content(prompt)
        return jsonify({'hooks': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_hooks: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/generate_titles', methods=['POST'])
def generate_titles():
    try:
        data = request.get_json()
        video_topic = data['topic']
        prompt = f"You are a viral YouTube Title expert. Generate 5 click-worthy YouTube titles for '{video_topic}'."
        response = model.generate_content(prompt)
        return jsonify({'titles': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_titles: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/generate_description', methods=['POST'])
def generate_description():
    try:
        data = request.get_json()
        video_topic = data['topic']
        keywords = data.get('keywords', '')
        prompt = f"Write a YouTube description for '{video_topic}' using keywords: {keywords}."
        response = model.generate_content(prompt)
        return jsonify({'description': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_description: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/generate_script', methods=['POST'])
def generate_script():
    try:
        data = request.get_json()
        video_topic = data['topic']
        video_length = data.get('length', '5 minutes')
        prompt = f"Create a script outline for a YouTube video about '{video_topic}' ({video_length})."
        response = model.generate_content(prompt)
        return jsonify({'script': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_script: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/generate_ideas', methods=['POST'])
def generate_ideas():
    try:
        data = request.get_json()
        niche = data.get('niche', '')
        prompt = f"Generate 5 video ideas for the '{niche}' niche."
        response = model.generate_content(prompt)
        return jsonify({'ideas': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_ideas: {e}")
        return jsonify({'error': str(e)}), 500
        
@app.route('/generate_tags', methods=['POST'])
def generate_tags():
    try:
        data = request.get_json()
        video_topic = data.get('topic', '')
        prompt = f"Generate 15 relevant YouTube tags for '{video_topic}' as a comma-separated list."
        response = model.generate_content(prompt)
        return jsonify({'tags': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_tags: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/generate_channel_name', methods=['POST'])
def generate_channel_name():
    try:
        data = request.get_json()
        niche = data.get('niche', '')
        prompt = f"Generate 10 channel names for a '{niche}' niche."
        response = model.generate_content(prompt)
        return jsonify({'names': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_channel_name: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/analyze_thumbnail', methods=['POST'])
def analyze_thumbnail():
    try:
        data = request.get_json()
        image_data = data.get('image')
        if not image_data:
            return jsonify({'error': 'No image data.'}), 400
            
        # Image process karna (base64 to image bytes)
        header, base64_str = image_data.split(',', 1)
        mime_type = header.split(':')[1].split(';')[0]
        image_bytes = base64.b64decode(base64_str)
        
        image_parts = [{"mime_type": mime_type, "data": image_bytes}]
        prompt = "Analyze this YouTube thumbnail and give an overall score out of 10. Give tips to improve it."
        
        # Gemini 1.5 Flash supports both image and text
        response = model.generate_content([prompt, image_parts[0]])
        return jsonify({'analysis': response.text.strip()})
    except Exception as e:
        print(f"Error in analyze_thumbnail: {e}")
        return jsonify({'error': str(e)}), 500

# Server ko run karte hain
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
```