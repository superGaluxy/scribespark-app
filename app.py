# app.py

import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import os

# --- (Optional) Add this to check library version in logs ---
# This is for debugging, you can remove it later.
try:
    print("--- LIBRARY VERSION CHECK ---")
    print(f"Google AI Library Version: {genai.__version__}")
    print("---------------------------")
except Exception as e:
    print(f"Could not check library version: {e}")
# -----------------------------------------------------------


# Flask app ko initialize karte hain
app = Flask(__name__)

# API Key ko Render ke "Environment Variables" se lete hain
API_KEY = os.environ.get('GEMINI_API_KEY')

# Gemini API ko configure karte hain
if API_KEY:
    genai.configure(api_key=API_KEY)
    print("INFO: Gemini API key configured successfully.")
else:
    print("WARNING: GEMINI_API_KEY environment variable is not set.")

# AI model ko select karte hain
# 'gemini-pro' is a stable and reliable choice.
model = genai.GenerativeModel('gemini-pro')

# --- Page Routes ---
# Inmein koi badlav nahi hai
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
# Sabhi API routes ab poore kar diye gaye hain

@app.route('/generate_hooks', methods=['POST'])
def generate_hooks():
    if not API_KEY:
        return jsonify({'error': 'API key not configured.'}), 500
    try:
        data = request.get_json()
        video_topic = data['topic']
        prompt = f"Generate 5 viral YouTube hooks for a video about '{video_topic}'. Each hook must be on a new line and nothing else."
        response = model.generate_content(prompt)
        return jsonify({'hooks': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_hooks: {e}")
        return jsonify({'error': 'An error occurred while generating hooks.'}), 500

@app.route('/generate_titles', methods=['POST'])
def generate_titles():
    if not API_KEY:
        return jsonify({'error': 'API key not configured.'}), 500
    try:
        data = request.get_json()
        video_topic = data['topic']
        prompt = f"Generate 10 viral and SEO-friendly YouTube titles for a video about '{video_topic}'. Each title must be on a new line and nothing else."
        response = model.generate_content(prompt)
        return jsonify({'titles': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_titles: {e}")
        return jsonify({'error': 'An error occurred while generating titles.'}), 500

@app.route('/generate_description', methods=['POST'])
def generate_description():
    if not API_KEY:
        return jsonify({'error': 'API key not configured.'}), 500
    try:
        data = request.get_json()
        video_topic = data['topic']
        prompt = f"Write a compelling and SEO-optimized YouTube video description for a video titled '{video_topic}'. Include relevant keywords, a strong opening, and a call to action. Format it with paragraphs."
        response = model.generate_content(prompt)
        return jsonify({'description': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_description: {e}")
        return jsonify({'error': 'An error occurred while generating the description.'}), 500

@app.route('/generate_script', methods=['POST'])
def generate_script():
    if not API_KEY:
        return jsonify({'error': 'API key not configured.'}), 500
    try:
        data = request.get_json()
        video_topic = data['topic']
        script_length = data.get('length', '5-minute')
        prompt = f"Write a detailed, engaging YouTube video script for a '{script_length}' video about '{video_topic}'. The script should have sections for intro, main content points, and an outro. Include suggestions for visuals where appropriate."
        response = model.generate_content(prompt)
        return jsonify({'script': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_script: {e}")
        return jsonify({'error': 'An error occurred while generating the script.'}), 500

@app.route('/generate_ideas', methods=['POST'])
def generate_ideas():
    if not API_KEY:
        return jsonify({'error': 'API key not configured.'}), 500
    try:
        data = request.get_json()
        niche = data['niche']
        prompt = f"Generate 10 fresh and unique YouTube video ideas for a channel in the '{niche}' niche. For each idea, provide a catchy title and a one-sentence concept."
        response = model.generate_content(prompt)
        return jsonify({'ideas': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_ideas: {e}")
        return jsonify({'error': 'An error occurred while generating ideas.'}), 500

@app.route('/generate_tags', methods=['POST'])
def generate_tags():
    if not API_KEY:
        return jsonify({'error': 'API key not configured.'}), 500
    try:
        data = request.get_json()
        video_topic = data['topic']
        prompt = f"Generate a list of 20 relevant, high-traffic SEO tags for a YouTube video about '{video_topic}'. Provide the tags as a single, comma-separated list."
        response = model.generate_content(prompt)
        return jsonify({'tags': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_tags: {e}")
        return jsonify({'error': 'An error occurred while generating tags.'}), 500

@app.route('/generate_channel_name', methods=['POST'])
def generate_channel_name():
    if not API_KEY:
        return jsonify({'error': 'API key not configured.'}), 500
    try:
        data = request.get_json()
        niche = data['niche']
        prompt = f"Generate 20 creative and brandable YouTube channel name ideas for a channel about '{niche}'. List each name on a new line."
        response = model.generate_content(prompt)
        return jsonify({'names': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_channel_name: {e}")
        return jsonify({'error': 'An error occurred while generating channel names.'}), 500

@app.route('/analyze_thumbnail', methods=['POST'])
def analyze_thumbnail():
    # Note: This function analyzes a *description* of a thumbnail, as handling image uploads is more complex.
    if not API_KEY:
        return jsonify({'error': 'API key not configured.'}), 500
    try:
        data = request.get_json()
        video_topic = data['topic']
        prompt = f"I'm making a YouTube video about '{video_topic}'. Give me 5 actionable tips to create a high-click-through-rate (CTR) thumbnail for this video. Focus on color, text, emotion, and composition."
        response = model.generate_content(prompt)
        return jsonify({'analysis': response.text.strip()})
    except Exception as e:
        print(f"Error in analyze_thumbnail: {e}")
        return jsonify({'error': 'An error occurred while analyzing the thumbnail idea.'}), 500

# Server ko run karte hain
# Yeh block sirf local testing ke liye chalta hai, Render isey use nahi karta.
if __name__ == '__main__':
    app.run(debug=True, port=8080)