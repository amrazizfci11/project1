"""
Local Web Application for Interactive Data Display
Run this to deploy the data display webpage locally
"""

from flask import Flask, render_template, request, jsonify
import json
from typing import Any, Dict, List

app = Flask(__name__)


class DataDisplayGenerator:
    """Standalone version of the data display generator"""

    def __init__(self):
        self.title = "LLM Data Display"
        self.theme_color = "#4F46E5"
        self.auto_parse_json = True
        self.collapsed_by_default = False

    def parse_data(self, data: str) -> List[Dict[str, Any]]:
        """Parse input data into structured sections."""
        sections = []

        if self.auto_parse_json:
            try:
                # Try parsing as JSON
                parsed = json.loads(data)

                if isinstance(parsed, dict):
                    # Convert dict to sections
                    for key, value in parsed.items():
                        sections.append({
                            "title": str(key).replace("_", " ").title(),
                            "content": self._format_value(value)
                        })
                elif isinstance(parsed, list):
                    # Handle list of items
                    for idx, item in enumerate(parsed):
                        sections.append({
                            "title": f"Item {idx + 1}",
                            "content": self._format_value(item)
                        })
                else:
                    sections.append({
                        "title": "Data",
                        "content": self._format_value(parsed)
                    })

                return sections
            except (json.JSONDecodeError, ValueError):
                pass

        # Fallback: Split by common section markers
        if "\n\n" in data:
            # Split by double newlines
            parts = data.split("\n\n")
            for idx, part in enumerate(parts):
                if part.strip():
                    # Try to identify title (first line if it's short)
                    lines = part.strip().split("\n", 1)
                    if len(lines) > 1 and len(lines[0]) < 100:
                        title = lines[0].strip("#* ")
                        content = lines[1]
                    else:
                        title = f"Section {idx + 1}"
                        content = part

                    sections.append({
                        "title": title,
                        "content": content
                    })
        else:
            # Single section
            sections.append({
                "title": "Output",
                "content": data
            })

        return sections

    def _format_value(self, value: Any) -> str:
        """Format a value for display."""
        if isinstance(value, (dict, list)):
            return json.dumps(value, indent=2)
        return str(value)

    def _escape_html(self, text: str) -> str:
        """Escape HTML special characters."""
        return (text
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#39;"))

    def _darken_color(self, hex_color: str, amount: float) -> str:
        """Darken a hex color by a percentage."""
        try:
            hex_color = hex_color.lstrip('#')
            r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            r = int(r * (1 - amount))
            g = int(g * (1 - amount))
            b = int(b * (1 - amount))
            return f"#{r:02x}{g:02x}{b:02x}"
        except:
            return hex_color

    def generate_html(self, sections: List[Dict[str, Any]]) -> str:
        """Generate the complete HTML page."""

        collapsed_class = "collapsed" if self.collapsed_by_default else ""

        # Generate sections HTML
        sections_html = ""
        for idx, section in enumerate(sections):
            section_id = f"section-{idx}"
            sections_html += f"""
            <div class="section-card {collapsed_class}">
                <div class="section-header" onclick="toggleSection('{section_id}')">
                    <div class="section-title">
                        <span class="toggle-icon">▼</span>
                        <h3>{section['title']}</h3>
                    </div>
                    <button class="copy-btn" onclick="copyText('{section_id}', event)" title="Copy to clipboard">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                        </svg>
                        Copy
                    </button>
                </div>
                <div class="section-content" id="{section_id}">
                    <pre class="content-text">{self._escape_html(section['content'])}</pre>
                </div>
            </div>
            """

        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            color: #1f2937;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        .header {{
            text-align: center;
            margin-bottom: 40px;
            animation: fadeInDown 0.6s ease-out;
        }}

        .header h1 {{
            color: white;
            font-size: 2.5rem;
            font-weight: 700;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 10px;
        }}

        .header p {{
            color: rgba(255,255,255,0.9);
            font-size: 1.1rem;
        }}

        .back-link {{
            display: inline-block;
            background: rgba(255,255,255,0.2);
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            text-decoration: none;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }}

        .back-link:hover {{
            background: rgba(255,255,255,0.3);
            transform: translateY(-2px);
        }}

        .sections-container {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}

        .section-card {{
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            overflow: hidden;
            transition: all 0.3s ease;
            animation: fadeInUp 0.6s ease-out;
            animation-fill-mode: both;
        }}

        .section-card:hover {{
            box-shadow: 0 10px 20px rgba(0,0,0,0.15);
            transform: translateY(-2px);
        }}

        .section-header {{
            background: {self.theme_color};
            color: white;
            padding: 20px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: background 0.3s ease;
        }}

        .section-header:hover {{
            background: {self._darken_color(self.theme_color, 0.1)};
        }}

        .section-title {{
            display: flex;
            align-items: center;
            gap: 15px;
            flex: 1;
        }}

        .section-title h3 {{
            font-size: 1.3rem;
            font-weight: 600;
        }}

        .toggle-icon {{
            font-size: 1.2rem;
            transition: transform 0.3s ease;
            display: inline-block;
        }}

        .section-card.collapsed .toggle-icon {{
            transform: rotate(-90deg);
        }}

        .copy-btn {{
            background: rgba(255,255,255,0.2);
            border: 1px solid rgba(255,255,255,0.3);
            color: white;
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.3s ease;
            font-weight: 500;
        }}

        .copy-btn:hover {{
            background: rgba(255,255,255,0.3);
            transform: scale(1.05);
        }}

        .copy-btn:active {{
            transform: scale(0.95);
        }}

        .copy-btn.copied {{
            background: #10b981;
            border-color: #10b981;
        }}

        .section-content {{
            max-height: 1000px;
            overflow: hidden;
            transition: max-height 0.4s ease, padding 0.4s ease;
        }}

        .section-card.collapsed .section-content {{
            max-height: 0;
            padding: 0;
        }}

        .content-text {{
            padding: 25px;
            background: #f9fafb;
            border-left: 4px solid {self.theme_color};
            margin: 0;
            white-space: pre-wrap;
            word-wrap: break-word;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            font-size: 0.95rem;
            line-height: 1.6;
            color: #374151;
            overflow-x: auto;
        }}

        .toast {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: #10b981;
            color: white;
            padding: 15px 25px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.3s ease;
            pointer-events: none;
            font-weight: 500;
            z-index: 1000;
        }}

        .toast.show {{
            opacity: 1;
            transform: translateY(0);
        }}

        @keyframes fadeInDown {{
            from {{
                opacity: 0;
                transform: translateY(-30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 2rem;
            }}

            .section-header {{
                padding: 15px;
            }}

            .section-title h3 {{
                font-size: 1.1rem;
            }}

            .content-text {{
                padding: 15px;
                font-size: 0.85rem;
            }}

            .copy-btn {{
                padding: 6px 12px;
                font-size: 0.8rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{self.title}</h1>
            <p>Click on sections to expand/collapse • Click copy to copy text</p>
            <br>
            <a href="/" class="back-link">← Enter New Data</a>
        </div>

        <div class="sections-container">
            {sections_html}
        </div>
    </div>

    <div class="toast" id="toast">Copied to clipboard!</div>

    <script>
        function toggleSection(sectionId) {{
            const section = document.getElementById(sectionId).closest('.section-card');
            section.classList.toggle('collapsed');
        }}

        function copyText(sectionId, event) {{
            event.stopPropagation();

            const contentElement = document.getElementById(sectionId).querySelector('.content-text');
            const text = contentElement.textContent;

            navigator.clipboard.writeText(text).then(() => {{
                showToast('Copied to clipboard!');

                const btn = event.currentTarget;
                const originalText = btn.innerHTML;
                btn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Copied!';
                btn.classList.add('copied');

                setTimeout(() => {{
                    btn.innerHTML = originalText;
                    btn.classList.remove('copied');
                }}, 2000);
            }}).catch(err => {{
                console.error('Failed to copy:', err);
                showToast('Failed to copy!');
            }});
        }}

        function showToast(message) {{
            const toast = document.getElementById('toast');
            toast.textContent = message;
            toast.classList.add('show');

            setTimeout(() => {{
                toast.classList.remove('show');
            }}, 3000);
        }}

        // Add staggered animation to sections
        document.querySelectorAll('.section-card').forEach((card, index) => {{
            card.style.animationDelay = `${{index * 0.1}}s`;
        }});
    </script>
</body>
</html>
        """

        return html

    def generate(self, data: str, title: str = None, theme_color: str = None,
                 auto_parse: bool = True, collapsed: bool = False) -> str:
        """Generate HTML from data with custom settings."""
        if title:
            self.title = title
        if theme_color:
            self.theme_color = theme_color
        self.auto_parse_json = auto_parse
        self.collapsed_by_default = collapsed

        sections = self.parse_data(data)
        return self.generate_html(sections)


# Flask routes
@app.route('/')
def index():
    """Display the input form"""
    return render_template('input.html')


@app.route('/display', methods=['POST'])
def display():
    """Process and display the data"""
    data = request.form.get('data', '')
    title = request.form.get('title', 'LLM Data Display')
    theme_color = request.form.get('theme_color', '#4F46E5')
    collapsed = request.form.get('collapsed', 'off') == 'on'

    if not data:
        return "No data provided", 400

    generator = DataDisplayGenerator()
    html = generator.generate(
        data=data,
        title=title,
        theme_color=theme_color,
        collapsed=collapsed
    )

    return html


@app.route('/api/generate', methods=['POST'])
def api_generate():
    """API endpoint for generating display HTML"""
    try:
        data = request.json
        generator = DataDisplayGenerator()
        html = generator.generate(
            data=data.get('data', ''),
            title=data.get('title', 'LLM Data Display'),
            theme_color=data.get('theme_color', '#4F46E5'),
            auto_parse=data.get('auto_parse', True),
            collapsed=data.get('collapsed', False)
        )
        return jsonify({'html': html, 'success': True})
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 400


if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Interactive Data Display - Local Web Server")
    print("=" * 60)
    print()
    print("Starting server...")
    print("Open your browser and visit: http://127.0.0.1:5000")
    print()
    print("Press CTRL+C to stop the server")
    print("=" * 60)
    print()

    app.run(debug=True, host='127.0.0.1', port=5000)
