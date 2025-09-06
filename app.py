# app.py

import google.generativeai as genai
from flask import Flask, render_template, request, jsonify, send_from_directory

# Flask app ko initialize karte hain
app = Flask(__name__)

# ----------------- VERY IMPORTANT -----------------
# Yahan par aapki API key honi chahiye
API_KEY = 'AIzaSyBAQsdoLI9P14pKHfadFmPqd6YY3dgU6R8' # Please make sure your actual key is here

# Gemini API ko configure karte hain
genai.configure(api_key=API_KEY)

# AI model ko select karte hain (Updated Model Name)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# --- Naya code jo Google ko sitemap aur robots.txt dega ---
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, 'robots.txt')
# ---------------------------------------------------------

# Homepage ke liye route
@app.route('/')
def home():
    return render_template('index.html')

# About Us page ke liye route
@app.route('/about')
def about():
    return render_template('about.html')

# Privacy Policy page ke liye route
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

# Contact Us page ke liye route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# AI se hooks generate karne ke liye naya route
@app.route('/generate', methods=['POST'])
def generate_hooks():
    try:
        data = request.get_json()
        video_topic = data['topic']
        video_tone = data.get('tone', 'Engaging') # Default tone

        if not video_topic:
            return jsonify({'error': 'Please enter a video topic.'}), 400

        prompt = f"""
        Generate 5 viral YouTube hooks for a video about '{video_topic}'. 
        The tone should be: {video_tone}.
        Each hook must be on a new line and nothing else.
        """
        response = model.generate_content(prompt)
        return jsonify({'hooks': response.text.strip()})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'An error occurred. Please check your API key.'}), 500

# Server ko run karte hain
if __name__ == '__main__':
    app.run(debug=True, port=8080)

