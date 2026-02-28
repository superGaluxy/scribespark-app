# app.py
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify, send_from_directory
import base64
import os
import smtplib
from email.mime.text import MIMEText
from blog_data import BLOG_POSTS

app = Flask(__name__)

# ----------------- ENVIRONMENT VARIABLE SETUP -----------------
API_KEY = os.environ.get('GEMINI_API_KEY')

def get_best_model():
    if not API_KEY:
        print("CRITICAL: GEMINI_API_KEY missing!")
        return None
    genai.configure(api_key=API_KEY)
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        priority = ['models/gemini-1.5-flash', 'models/gemini-1.5-flash-latest', 'models/gemini-pro']
        for p in priority:
            if p in available_models:
                return genai.GenerativeModel(p)
        if available_models:
            return genai.GenerativeModel(available_models[0])
    except Exception as e:
        print(f"Error listing models: {e}")
    return genai.GenerativeModel('gemini-pro')

model = get_best_model()

# --- Static folder ensure ---
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
os.makedirs(static_dir, exist_ok=True)

# ----------------- SEO & STATIC ROUTES -----------------
# Ye do routes aapke Not Found (404) error ko theek karenge
@app.route('/robots.txt')
def serve_robots():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/sitemap.xml')
def serve_sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml')

# ----------------- PAGE ROUTES (GET) -----------------
@app.route('/')
def home(): return render_template('index.html')

@app.route('/title-generator')
def title_generator_page(): return render_template('title-generator.html')

@app.route('/description-writer')
def description_writer_page(): return render_template('description-writer.html')

@app.route('/script-writer')
def script_writer_page(): return render_template('script-writer.html')

@app.route('/video-idea-finder')
def video_idea_finder_page(): return render_template('video-idea-finder.html')

@app.route('/hook-generator')
def hook_generator_page(): return render_template('hook-generator.html')

@app.route('/tag-generator')
def tag_generator_page(): return render_template('tag-generator.html')

@app.route('/hashtag-generator')
def hashtag_generator_page(): return render_template('hashtag-generator.html')

@app.route('/shorts-script-writer')
def shorts_script_writer_page(): return render_template('shorts-script-writer.html')

@app.route('/comment-reply-generator')
def comment_reply_generator_page(): return render_template('comment-reply-generator.html')

@app.route('/channel-name-generator')
def channel_name_generator_page(): return render_template('channel-name-generator.html')

@app.route('/competitor-analyzer')
def competitor_analyzer_page(): return render_template('competitor-analyzer.html')

@app.route('/trending-topics')
def trending_topics_page(): return render_template('trending-topics.html')

@app.route('/content-calendar')
def content_calendar_page(): return render_template('content-calendar.html')

@app.route('/seo-score-checker')
def seo_score_checker_page(): return render_template('seo-score-checker.html')

@app.route('/thumbnail-analyzer')
def thumbnail_analyzer_page(): return render_template('thumbnail-analyzer.html')

@app.route('/thumbnail-downloader')
def thumbnail_downloader_page(): return render_template('thumbnail-downloader.html')

@app.route('/revenue-calculator')
def revenue_calculator_page(): return render_template('revenue-calculator.html')

@app.route('/engagement-analyzer')
def engagement_analyzer_page(): return render_template('engagement-analyzer.html')

@app.route('/video-length-optimizer')
def video_length_optimizer_page(): return render_template('video-length-optimizer.html')

@app.route('/sponsorship-email-generator')
def sponsorship_email_generator_page(): return render_template('sponsorship-email-generator.html')

@app.route('/about')
def about(): return render_template('about.html')

@app.route('/blog')
def blog_page(): return render_template('blog.html')

@app.route('/privacy')
def privacy(): 
    # Check karein ki file ka naam 'privacy.html' hi hai templates folder mein
    return render_template('privacy.html')

@app.route('/terms')
def terms(): return render_template('terms.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        sender_email = os.environ.get('ZOHO_EMAIL')
        sender_password = os.environ.get('ZOHO_PASSWORD')
        receiver_email = "support@scribespark.online"
        
        if sender_email and sender_password:
            try:
                msg = MIMEText(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")
                msg['Subject'] = f"Contact Form: {name}"
                msg['From'] = sender_email
                msg['To'] = receiver_email
                
                try:
                    server = smtplib.SMTP_SSL('smtp.zoho.in', 465, timeout=10)
                except Exception:
                    server = smtplib.SMTP_SSL('smtp.zoho.com', 465, timeout=10)
                
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, [receiver_email], msg.as_string())
                server.quit()
                return render_template('contact.html', success=True)
            except Exception as e:
                print(f"Error sending email: {e}")
                return render_template('contact.html', error=True)
        else:
            print("ZOHO credentials missing.")
            return render_template('contact.html', error=True)
            
    return render_template('contact.html')

@app.route('/blog')
def blog(): 
    return render_template('blog.html', blogs=BLOG_POSTS)

@app.route('/blog/<slug>')
def blog_post(slug):
    post = BLOG_POSTS.get(slug)
    if not post:
        return "Blog post not found.", 404
    return render_template('blog_post.html', post=post, slug=slug)

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


@app.route('/robots.txt')
def robots():
    return send_from_directory(static_dir, 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(static_dir, 'sitemap.xml')

# ----------------- AI API ROUTES (POST) -----------------
def ai_call(prompt):
    if not model: return "API Key not set."
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/generate_titles', methods=['POST'])
def generate_titles():
    data = request.json or {}
    topic = data.get('topic', '')
    return jsonify({'titles': ai_call(f"Generate 5 viral YouTube titles for '{topic}'.")})

@app.route('/generate_description', methods=['POST'])
def generate_description():
    data = request.json or {}
    return jsonify({'description': ai_call(f"Write a YouTube description for '{data.get('topic','')}' using keywords: {data.get('keywords','')}")})

@app.route('/generate_script', methods=['POST'])
def generate_script():
    data = request.json or {}
    return jsonify({'script': ai_call(f"Write a YouTube script for '{data.get('topic','')}' with length {data.get('length','5 mins')}")})

@app.route('/generate_hooks', methods=['POST'])
def generate_hooks():
    data = request.json or {}
    return jsonify({'hooks': ai_call(f"Generate 5 viral YouTube hooks for '{data.get('topic','')}' with tone {data.get('tone','Engaging')}")})

@app.route('/generate_ideas', methods=['POST'])
def generate_ideas():
    data = request.json or {}
    niche = data.get('niche', '')
    return jsonify({'ideas': ai_call(f"Generate 5 YouTube video ideas for {niche} niche.")})

@app.route('/generate_tags', methods=['POST'])
def generate_tags():
    data = request.json or {}
    topic = data.get('topic', '')
    return jsonify({'tags': ai_call(f"Generate 15 YouTube tags for '{topic}' as comma separated list.")})

@app.route('/generate_hashtags', methods=['POST'])
def generate_hashtags():
    data = request.json or {}
    topic = data.get('topic', '')
    return jsonify({'hashtags': ai_call(f"Generate 10 trending YouTube hashtags for '{topic}'.")})

@app.route('/generate_shorts_script', methods=['POST'])
def generate_shorts_script():
    data = request.json or {}
    return jsonify({'script': ai_call(f"Write a 60-second YouTube Shorts script for '{data.get('topic','')}' in {data.get('style','Fast-paced')} style.")})

@app.route('/generate_comment_reply', methods=['POST'])
def generate_comment_reply():
    data = request.json or {}
    return jsonify({'replies': ai_call(f"Generate 3 polite replies to this YouTube comment: '{data.get('comment','')}' with tone {data.get('tone','Professional')}")})

@app.route('/generate_channel_name', methods=['POST'])
def generate_channel_name():
    data = request.json or {}
    niche = data.get('niche', '')
    return jsonify({'names': ai_call(f"Generate 10 catchy YouTube channel names for {niche} niche.")})

@app.route('/analyze_competitor', methods=['POST'])
def analyze_competitor():
    data = request.json or {}
    return jsonify({'analysis': ai_call(f"Analyze the YouTube competitor channel '{data.get('channel','')}' in niche '{data.get('niche','')}'. Give strengths and content tips.")})

@app.route('/generate_trending', methods=['POST'])
def generate_trending():
    data = request.json or {}
    niche = data.get('niche', '')
    return jsonify({'trends': ai_call(f"What are the top 5 trending topics on YouTube right now for '{niche}' niche?")})

@app.route('/generate_calendar', methods=['POST'])
def generate_calendar():
    data = request.json or {}
    return jsonify({'calendar': ai_call(f"Create a 2-week YouTube content calendar for '{data.get('niche','')}' niche with frequency '{data.get('frequency','2 times a week')}'.")})

@app.route('/check_seo_score', methods=['POST'])
def check_seo_score():
    data = request.json or {}
    prompt = f"Analyze YouTube SEO for Title: {data.get('title','')}, Desc: {data.get('description','')}, Tags: {data.get('tags','')}. Give a score out of 100 and tips."
    return jsonify({'seo_result': ai_call(prompt)})

@app.route('/optimize_video_length', methods=['POST'])
def optimize_video_length():
    data = request.json or {}
    return jsonify({'optimization': ai_call(f"Suggest the ideal YouTube video length for topic '{data.get('topic','')}' in '{data.get('niche','')}' niche to maximize retention.")})

@app.route('/generate_sponsorship_email', methods=['POST'])
def generate_sponsorship_email():
    data = request.json or {}
    return jsonify({'email': ai_call(f"Write a professional sponsorship pitch email to '{data.get('brand_name','')}' for my YouTube channel in '{data.get('niche','')}' niche.")})

@app.route('/analyze_engagement', methods=['POST'])
def analyze_engagement():
    d = request.json or {}
    prompt = f"Calculate engagement for a video with {d.get('views',0)} views, {d.get('likes',0)} likes, {d.get('comments',0)} comments, {d.get('subscribers',0)} subs. Is it good? Give growth tips."
    return jsonify({'analysis': ai_call(prompt)})

@app.route('/analyze_thumbnail', methods=['POST'])
def analyze_thumbnail():
    try:
        data = request.json or {}
        image_data = data.get('image')
        if not image_data:
            return jsonify({'error': 'No image provided'}), 400
        header, base64_str = image_data.split(',', 1)
        mime_type = header.split(':')[1].split(';')[0]
        image_bytes = base64.b64decode(base64_str)
        response = model.generate_content(["Analyze this YouTube thumbnail. Give a score out of 10 and 3 tips.", {'mime_type': mime_type, 'data': image_bytes}])
        return jsonify({'analysis': response.text.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)