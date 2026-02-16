import os
import re

TEMPLATE_DIR = r'c:\Users\SURYA\Desktop\scribespark-001\SCRIBESPARK\templates'

def check_meta_tags():
    missing_meta = []
    present_meta = []

    for filename in os.listdir(TEMPLATE_DIR):
        if filename.endswith('.html') and filename != 'layout.html':
            filepath = os.path.join(TEMPLATE_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for block meta
            meta_match = re.search(r'{%\s*block\s+meta\s*%}(.*?){%\s*endblock\s*%}', content, re.DOTALL)
            
            if meta_match:
                meta_content = meta_match.group(1).strip()
                if meta_content:
                    present_meta.append(filename)
                else:
                    missing_meta.append(filename)
            else:
                missing_meta.append(filename)

    print("Files with META tags:")
    for f in present_meta:
        print(f" - {f}")

    print("\nFiles MISSING META tags:")
    for f in missing_meta:
        print(f" - {f}")

if __name__ == '__main__':
    check_meta_tags()
