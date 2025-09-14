# app.py

import google.generativeai as genai
from flask import Flask, render_template, request, jsonify, send_from_directory
import base64

# Flask app ko initialize karte hain
app = Flask(__name__)

# ----------------- VERY IMPORTANT -----------------
# Yahan par aapki API key honi chahiye
API_KEY = 'AIzaSyBAQsdoLI9P14pKHfadFmPqd6YY3dgU6R8' # Please make sure your actual key is here

# Gemini API ko configure karte hain
genai.configure(api_key=API_KEY)

# AI model ko select karte hain (Updated Model Name)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

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
        return jsonify({'error': 'An error occurred. Please check your API key.'}), 500

@app.route('/generate_titles', methods=['POST'])
def generate_titles():
    try:
        data = request.get_json()
        video_topic = data['topic']
        prompt = f"You are a viral YouTube Title expert. Generate 5 highly click-worthy and SEO-friendly YouTube titles for a video about '{video_topic}'. Follow these rules: 1. Create a mix of styles: listicles, questions, and intriguing statements. 2. Keep titles concise and powerful. 3. Each title must be on a new line and nothing else."
        response = model.generate_content(prompt)
        return jsonify({'titles': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_titles: {e}")
        return jsonify({'error': 'An error occurred. Please check your API key.'}), 500

@app.route('/generate_description', methods=['POST'])
def generate_description():
    try:
        data = request.get_json()
        video_topic = data['topic']
        keywords = data.get('keywords', '')
        prompt = f"You are a YouTube SEO expert. Write a compelling and SEO-optimized YouTube video description for a video about '{video_topic}'. Instructions: 1. Start with an engaging summary paragraph (2-3 sentences). 2. If provided, include these keywords: {keywords}. 3. Create a \"What you'll learn:\" section with 3-4 bullet points. 4. Add a \"Connect with us\" section with social media placeholders. 5. End with 3-5 relevant hashtags."
        response = model.generate_content(prompt)
        return jsonify({'description': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_description: {e}")
        return jsonify({'error': 'An error occurred. Please check your API key.'}), 500

@app.route('/generate_script', methods=['POST'])
def generate_script():
    try:
        data = request.get_json()
        video_topic = data['topic']
        video_length = data.get('length', '5 minutes')
        prompt = f"You are an expert YouTube scriptwriter. Create a structured script outline for a video about '{video_topic}'. The target video length is approximately {video_length}. Structure the script as follows: **Introduction:** (Hook, summary), **Main Content:** (3-4 points with bullets), and **Conclusion:** (Summary, Call to Action)."
        response = model.generate_content(prompt)
        return jsonify({'script': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_script: {e}")
        return jsonify({'error': 'An error occurred. Please check your API key.'}), 500

@app.route('/generate_ideas', methods=['POST'])
def generate_ideas():
    try:
        data = request.get_json()
        niche = data.get('niche', '')
        prompt = f"You are a YouTube trend expert and content strategist. For a YouTube channel in the '{niche}' niche, generate 5 fresh and engaging video ideas. For each idea, provide: **1. A Viral Title:** Make it catchy and clickable. **2. A Brief Concept:** A 1-2 sentence summary of what the video would be about. Format each idea clearly."
        response = model.generate_content(prompt)
        return jsonify({'ideas': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_ideas: {e}")
        return jsonify({'error': 'An error occurred. Please check your API key.'}), 500
        
@app.route('/generate_tags', methods=['POST'])
def generate_tags():
    try:
        data = request.get_json()
        video_topic = data.get('topic', '')
        prompt = f"You are a YouTube SEO and keyword expert. For a video about '{video_topic}', generate a list of 15-20 highly relevant YouTube tags. Instructions: - Include a mix of broad, specific, and long-tail keywords. - Output the tags as a single, comma-separated string. - Do not add any extra text or titles. Just the comma-separated tags."
        response = model.generate_content(prompt)
        return jsonify({'tags': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_tags: {e}")
        return jsonify({'error': 'An error occurred. Please check your API key.'}), 500

@app.route('/generate_channel_name', methods=['POST'])
def generate_channel_name():
    try:
        data = request.get_json()
        niche = data.get('niche', '')
        prompt = f"You are a branding expert specializing in catchy YouTube channel names. For a channel focused on '{niche}', generate 10 unique and memorable name ideas. Instructions: - Provide a mix of styles: clever puns, direct names, and creative/abstract names. - Keep the names relatively short and easy to spell. - Each name should be on a new line and nothing else."
        response = model.generate_content(prompt)
        return jsonify({'names': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_channel_name: {e}")
        return jsonify({'error': 'An error occurred. Please check your API key.'}), 500

@app.route('/analyze_thumbnail', methods=['POST'])
def analyze_thumbnail():
    try:
        data = request.get_json()
        image_data = data.get('image')

        if not image_data:
            return jsonify({'error': 'No image data received.'}), 400
        
        mime_type, base64_str = image_data.split(',', 1)
        
        image_parts = [{"mime_type": mime_type.split(':')[1].split(';')[0], "data": base64_str}]
        
        prompt_parts = [
            "You are a YouTube thumbnail expert like MrBeast's designer. Analyze this thumbnail and provide feedback. Structure your response as follows:\n\n**Overall Score (out of 10):** [Your score]\n\n**What's Good:**\n- [Point 1]\n- [Point 2]\n\n**Areas for Improvement:**\n- [Suggestion 1]\n- [Suggestion 2]\n\nFocus on clarity, click-worthiness, text readability, color contrast, and emotional impact.",
            image_parts[0]
        ]
        
        response = model.generate_content(prompt_parts)
        return jsonify({'analysis': response.text.strip()})

    except Exception as e:
        print(f"Error in analyze_thumbnail: {e}")
        return jsonify({'error': 'An error occurred during analysis.'}), 500

# Server ko run karte hain
if __name__ == '__main__':
    app.run(debug=True, port=8080)

