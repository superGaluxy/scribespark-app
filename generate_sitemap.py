import os
import datetime

# Configuration
BASE_URL = "https://scribespark.online"
TEMPLATE_DIR = r"c:\Users\SURYA\Desktop\scribespark-001\SCRIBESPARK\templates"
OUTPUT_DIR = r"c:\Users\SURYA\Desktop\scribespark-001\SCRIBESPARK\static"
EXCLUDED_FILES = ["layout.html", "404.html", "500.html", "base.html"]

def generate_sitemap():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    urls = []
    
    # Homepage first
    urls.append({
        "loc": f"{BASE_URL}/",
        "lastmod": datetime.date.today().isoformat(),
        "priority": "1.0"
    })

    for filename in os.listdir(TEMPLATE_DIR):
        if filename.endswith(".html") and filename not in EXCLUDED_FILES and filename != "index.html":
            # Convert filename to route (e.g., 'title-generator.html' -> 'title-generator')
            route = filename.replace(".html", "")
            
            # Priority logic
            priority = "0.8"
            if route in ["privacy", "terms", "contact", "about"]:
                priority = "0.5"

            urls.append({
                "loc": f"{BASE_URL}/{route}",
                "lastmod": datetime.date.today().isoformat(),
                "priority": priority
            })

    # Generate XML content
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for url in urls:
        sitemap_content += '  <url>\n'
        sitemap_content += f'    <loc>{url["loc"]}</loc>\n'
        sitemap_content += f'    <lastmod>{url["lastmod"]}</lastmod>\n'
        sitemap_content += f'    <priority>{url["priority"]}</priority>\n'
        sitemap_content += '  </url>\n'
    
    sitemap_content += '</urlset>'

    # Save sitemap.xml
    sitemap_path = os.path.join(OUTPUT_DIR, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print(f"Generated sitemap.xml at {sitemap_path}")

    # Generate robots.txt
    robots_content = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    robots_path = os.path.join(OUTPUT_DIR, "robots.txt")
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(robots_content)
    print(f"Generated robots.txt at {robots_path}")

if __name__ == "__main__":
    generate_sitemap()
