# app.py

import google.generativeai as genai
from flask import Flask, render_template, request, jsonify, send_from_directory
import base64
import os

# Flask app ko initialize karte hain
app = Flask(__name__)

# ----------------- VERY IMPORTANT -----------------
# Yahan par aapki API key honi chahiye
API_KEY = os.environ.get('API_KEY')

# Gemini API ko configure karte hain
genai.configure(api_key=API_KEY)

# AI model ko select karte hain
model = genai.GenerativeModel('gemini-1.5-flash-latest')

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

# --- NEW TOOL API Routes ---

@app.route('/generate_trending', methods=['POST'])
def generate_trending():
    try:
        data = request.get_json()
        niche = data.get('niche', '')
        prompt = f"You are a YouTube trend analyst with access to the latest content trends. For the '{niche}' niche, identify 7 currently trending or breakout topics that creators should make videos about RIGHT NOW. For each topic provide: **Topic Title:** A catchy name. **Why It's Trending:** 1 sentence explanation. **Video Angle:** How a creator should approach this topic. Format each clearly with numbers."
        response = model.generate_content(prompt)
        return jsonify({'trends': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_trending: {e}")
        return jsonify({'error': 'An error occurred.'}), 500

@app.route('/generate_calendar', methods=['POST'])
def generate_calendar():
    try:
        data = request.get_json()
        niche = data.get('niche', '')
        frequency = data.get('frequency', '3 videos per week')
        prompt = f"You are a YouTube content strategist. Create a 2-week content calendar for a '{niche}' channel posting {frequency}. For each video provide: **Day & Date**, **Video Title** (catchy and clickable), **Content Type** (Tutorial/Vlog/List/Review/etc), and **Brief Description** (1 sentence). Make the schedule balanced and strategic. Use upcoming dates starting from today."
        response = model.generate_content(prompt)
        return jsonify({'calendar': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_calendar: {e}")
        return jsonify({'error': 'An error occurred.'}), 500

@app.route('/check_seo_score', methods=['POST'])
def check_seo_score():
    try:
        data = request.get_json()
        title = data.get('title', '')
        description = data.get('description', '')
        tags = data.get('tags', '')
        prompt = f"""You are a YouTube SEO scoring expert. Analyze the following YouTube video metadata and give a detailed SEO score:

**Title:** {title}
**Description:** {description}
**Tags:** {tags}

Provide your analysis in this format:
**Overall SEO Score: X/100**

**Title Analysis (Score: X/25):**
- Strengths and weaknesses

**Description Analysis (Score: X/25):**
- Strengths and weaknesses

**Tags Analysis (Score: X/25):**
- Strengths and weaknesses

**Click-Through Potential (Score: X/25):**
- Assessment

**Top 3 Recommendations:**
1. ...
2. ...
3. ..."""
        response = model.generate_content(prompt)
        return jsonify({'seo_result': response.text.strip()})
    except Exception as e:
        print(f"Error in check_seo_score: {e}")
        return jsonify({'error': 'An error occurred.'}), 500

@app.route('/optimize_video_length', methods=['POST'])
def optimize_video_length():
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        niche = data.get('niche', '')
        prompt = f"You are a YouTube analytics expert. For a video about '{topic}' in the '{niche}' niche, recommend the optimal video length. Provide: **Recommended Length:** X-Y minutes. **Why This Length:** Explanation based on audience behavior. **Retention Tips:** 3-4 tips to keep viewers watching. **Structure Suggestion:** How to divide the content across the video duration. Be specific with data-driven reasoning."
        response = model.generate_content(prompt)
        return jsonify({'optimization': response.text.strip()})
    except Exception as e:
        print(f"Error in optimize_video_length: {e}")
        return jsonify({'error': 'An error occurred.'}), 500

@app.route('/analyze_engagement', methods=['POST'])
def analyze_engagement():
    try:
        data = request.get_json()
        views = data.get('views', 0)
        likes = data.get('likes', 0)
        comments = data.get('comments', 0)
        subscribers = data.get('subscribers', 0)
        prompt = f"""You are a YouTube analytics expert. Analyze these video metrics:
- Views: {views}
- Likes: {likes}
- Comments: {comments}
- Channel Subscribers: {subscribers}

Calculate and provide:
**Engagement Rate:** (likes + comments) / views * 100
**Like-to-View Ratio:** likes / views * 100
**Comment-to-View Ratio:** comments / views * 100
**View-to-Subscriber Ratio:** views / subscribers * 100

**Performance Rating:** (Excellent/Good/Average/Below Average)
**Detailed Analysis:** What these numbers mean for the channel
**3 Actionable Tips:** To improve engagement

Use actual calculations with the numbers provided."""
        response = model.generate_content(prompt)
        return jsonify({'analysis': response.text.strip()})
    except Exception as e:
        print(f"Error in analyze_engagement: {e}")
        return jsonify({'error': 'An error occurred.'}), 500

@app.route('/generate_hashtags', methods=['POST'])
def generate_hashtags():
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        prompt = f"You are a YouTube hashtag expert. For a video about '{topic}', generate 20 trending and relevant YouTube hashtags. Instructions: - Include a mix of broad, specific, and trending hashtags. - Each hashtag should start with #. - Output them as a comma-separated string. - Do not add any extra text. Just the comma-separated hashtags."
        response = model.generate_content(prompt)
        return jsonify({'hashtags': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_hashtags: {e}")
        return jsonify({'error': 'An error occurred.'}), 500

@app.route('/generate_comment_reply', methods=['POST'])
def generate_comment_reply():
    try:
        data = request.get_json()
        comment = data.get('comment', '')
        tone = data.get('tone', 'Friendly & Appreciative')
        prompt = f"You are a YouTube creator who is great at engaging with their community. Generate 3 different reply options for this YouTube comment: '{comment}'. The tone should be: {tone}. Each reply should be on a new line, numbered 1-3. Keep replies concise (1-2 sentences each). Do not add any extra text."
        response = model.generate_content(prompt)
        return jsonify({'replies': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_comment_reply: {e}")
        return jsonify({'error': 'An error occurred.'}), 500

@app.route('/generate_shorts_script', methods=['POST'])
def generate_shorts_script():
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        style = data.get('style', 'Fast-paced informational')
        prompt = f"You are a viral YouTube Shorts scriptwriter. Write a complete 60-second YouTube Shorts script about '{topic}'. Style: {style}. Structure: **HOOK (0-3 sec):** An attention-grabbing opening line. **SETUP (3-10 sec):** Build context quickly. **MAIN CONTENT (10-45 sec):** Core value with 3-4 punchy points. **CTA (45-60 sec):** Strong call to action. Keep it punchy, conversational, and optimized for vertical video."
        response = model.generate_content(prompt)
        return jsonify({'script': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_shorts_script: {e}")
        return jsonify({'error': 'An error occurred.'}), 500

@app.route('/analyze_competitor', methods=['POST'])
def analyze_competitor():
    try:
        data = request.get_json()
        channel = data.get('channel', '')
        niche = data.get('niche', 'General')
        prompt = f"""You are a YouTube strategy consultant. Analyze the YouTube channel '{channel}' in the '{niche}' niche. Provide:

**Channel Overview:** Brief summary of what they do
**Content Strategy:** Types of videos they make, posting frequency
**Strengths:** 3-4 key strengths
**Weaknesses:** 2-3 areas of improvement  
**Why They Succeed:** Key factors behind their growth
**Lessons for You:** 3-4 actionable takeaways you can apply
**How to Differentiate:** 2-3 ways to stand out from this competitor

Be specific and provide actionable insights."""
        response = model.generate_content(prompt)
        return jsonify({'analysis': response.text.strip()})
    except Exception as e:
        print(f"Error in analyze_competitor: {e}")
        return jsonify({'error': 'An error occurred.'}), 500

# Server ko run karte hain
@app.route('/sponsorship-email-generator')
def sponsorship_email_generator_page():
    return render_template('sponsorship-email-generator.html')

@app.route('/generate_sponsorship_email', methods=['POST'])
def generate_sponsorship_email():
    try:
        data = request.get_json()
        brand_name = data.get('brand_name', '')
        channel_niche = data.get('niche', '')
        
        prompt = f"""You are a professional brand deal negotiator. Write a cold outreach email to a brand named '{brand_name}'. 
My channel niche is: '{channel_niche}'.

Structure the email as follows:
**Subject:** [Catchy Subject Line]

**Email Body:**
[Professional Greeting]
[Introduction: Who I am and why I love their brand]
[Value Proposition: Why my audience is a perfect fit]
[Proposal: Open to collaboration/sponsorship]
[Call to Action: Request for a call or media kit review]
[Professional Sign-off]

Keep it concise, professional, and persuasive."""

        response = model.generate_content(prompt)
        return jsonify({'email': response.text.strip()})
    except Exception as e:
        print(f"Error in generate_sponsorship_email: {e}")
        return jsonify({'error': 'An error occurred.'}), 500

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
