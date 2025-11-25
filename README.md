# Interactive Data Display Component for Langflow

[![Langflow](https://img.shields.io/badge/Langflow-Compatible-blue)](https://www.langflow.org/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A beautiful, interactive Langflow custom component that displays LLM output data in a professional web interface with collapsible sections, smooth animations, and copy-to-clipboard functionality.

![Example Output](example_output.html)

## 🚀 Features

- **🎨 Beautiful Modern UI** - Gradient backgrounds, smooth animations, and professional design
- **📦 Auto-Sectioned Display** - Intelligently groups data into organized, collapsible sections
- **📋 One-Click Copy** - Copy any section to clipboard with visual feedback
- **🔍 Smart JSON Parsing** - Automatically detects and formats JSON data
- **🎨 Customizable Theming** - Easy color customization to match your brand
- **📱 Fully Responsive** - Perfect display on desktop, tablet, and mobile devices
- **⚡ Interactive Panels** - Smooth expand/collapse animations
- **🔒 HTML Sanitization** - Safely handles user input with proper escaping

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Component Details](#component-details)
- [Usage Examples](#usage-examples)
- [Testing](#testing)
- [Customization](#customization)
- [Documentation](#documentation)

## 🔧 Installation

### Prerequisites

- Langflow installed (version 1.0.0+)
- Python 3.9 or higher

### Method 1: Using Custom Components Directory

1. **Create the directory structure:**
```bash
mkdir -p my_langflow_components/display
cd my_langflow_components/display
```

2. **Copy the component file:**
```bash
# Copy data_display_component.py to this directory
cp /path/to/data_display_component.py .
```

3. **Create `__init__.py`:**
```bash
touch __init__.py
```

4. **Set environment variable and start Langflow:**
```bash
export LANGFLOW_COMPONENTS_PATH=/path/to/my_langflow_components
langflow run
```

### Method 2: Direct Integration

1. Copy `data_display_component.py` directly into Langflow's components directory
2. Restart Langflow
3. The component will appear in the components panel

### Method 3: Import in Langflow UI

1. Open Langflow web interface
2. Navigate to Components → Import Component
3. Upload `data_display_component.py`
4. Component is immediately available

## 🚀 Quick Start

### Basic Usage in Langflow

1. **Create a new flow**
2. **Add components:**
   - Add an LLM component (e.g., OpenAI, Anthropic)
   - Add the "Interactive Data Display" component
3. **Connect them:**
   - Connect LLM output to Data Input
4. **Configure (optional):**
   - Set custom title, theme color
5. **Run the flow!**

### Example Flow

```
[User Input] → [OpenAI LLM] → [Interactive Data Display] → [Chat Output]
```

## 📦 Component Details

### Inputs

| Input | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| **Data Input** | MessageText | Yes | - | LLM output (text, JSON, or structured data) |
| **Page Title** | String | No | "LLM Data Display" | Main heading for the page |
| **Theme Color** | String | No | "#4F46E5" | Primary color (hex format) |
| **Auto Parse JSON** | Boolean | No | True | Automatically parse JSON into sections |
| **Collapsed by Default** | Boolean | No | False | Start with sections collapsed |

### Output

- **HTML Output**: A `Message` object containing complete HTML page
- Can be connected to Chat Output, Text Output, or saved to file

### Supported Data Formats

1. **JSON Objects** - Keys become section titles
2. **JSON Arrays** - Items become numbered sections
3. **Plain Text** - Splits by paragraphs/double newlines
4. **Markdown-style** - Detects headers as section titles
5. **Mixed Format** - Combines multiple parsing strategies

## 💡 Usage Examples

### Example 1: Simple LLM Output

**Input:**
```
The benefits of cloud computing include:

Cost Efficiency
Pay only for what you use, reducing capital expenditure.

Scalability
Easily scale resources up or down based on demand.

Accessibility
Access your data from anywhere with an internet connection.
```

**Result:** Three beautiful collapsible sections with copy buttons

### Example 2: JSON Data from API

**Input:**
```json
{
  "user_info": {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "role": "Data Scientist"
  },
  "analysis_results": {
    "accuracy": 0.94,
    "precision": 0.91,
    "recall": 0.89,
    "f1_score": 0.90
  },
  "recommendations": [
    "Increase training data size",
    "Try ensemble methods",
    "Perform feature engineering"
  ]
}
```

**Result:** Formatted sections with proper JSON indentation

### Example 3: Research Analysis

Create a flow that:
1. Takes user query about a topic
2. Uses LLM to research and analyze
3. Formats response with sections: Summary, Details, Sources
4. Displays in interactive format

## 🧪 Testing

### Local Testing (Without Langflow)

Run the included test script:

```bash
python test_component.py
```

This generates 5 test HTML files demonstrating different use cases:
- `test_output_json.html` - JSON data example
- `test_output_text.html` - Plain text example
- `test_output_llm.html` - LLM-style response
- `test_output_collapsed.html` - Collapsed sections
- `test_output_error.html` - Error handling

Open any file in your browser to see the result!

### View Example Output

Open `example_output.html` in your browser to see a complete example with business report data.

## 🎨 Customization

### Color Themes

Popular theme colors:

| Theme | Hex Code | Best For |
|-------|----------|----------|
| Indigo (Default) | `#4F46E5` | Professional, tech |
| Emerald | `#059669` | Success, finance |
| Red | `#DC2626` | Alerts, important |
| Purple | `#7C3AED` | Creative, design |
| Blue | `#2563EB` | Trust, corporate |
| Orange | `#EA580C` | Energy, enthusiasm |

### Advanced Customization

Edit the `generate_html()` method in `data_display_component.py` to:
- Modify CSS styles
- Change layout structure
- Add custom JavaScript features
- Integrate additional libraries

## 📚 Documentation

Detailed documentation available in:
- **[COMPONENT_USAGE.md](COMPONENT_USAGE.md)** - Comprehensive usage guide
- **[data_display_component.py](data_display_component.py)** - Fully commented source code
- **[test_component.py](test_component.py)** - Testing examples

## 🛠️ Technical Architecture

```
InteractiveDataDisplay (Component)
│
├── Input Processing
│   ├── Auto JSON detection
│   ├── Text parsing
│   └── Section extraction
│
├── HTML Generation
│   ├── Responsive CSS
│   ├── Interactive JavaScript
│   └── Secure HTML escaping
│
└── Output
    └── Message with complete HTML page
```

## 📁 Project Structure

```
.
├── data_display_component.py    # Main component file
├── test_component.py             # Test suite
├── example_output.html           # Example output demo
├── COMPONENT_USAGE.md            # Detailed usage guide
├── README.md                     # This file
└── requirements.txt              # Dependencies
```

## 🔍 Troubleshooting

### Component not appearing in Langflow

1. Verify `__init__.py` exists in component directory
2. Check `LANGFLOW_COMPONENTS_PATH` environment variable
3. Restart Langflow completely
4. Check Langflow logs for import errors

### HTML not rendering

- Ensure output is connected to a viewer component
- Some components show raw HTML - use browser-based output
- Check browser console for JavaScript errors

### Copy button not working

- Requires modern browser (Chrome, Firefox, Safari, Edge)
- HTTPS may be required for clipboard API
- Check browser permissions for clipboard access

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

MIT License - feel free to use in your projects!

## 🙏 Acknowledgments

- Built for [Langflow](https://www.langflow.org/)
- Inspired by modern data visualization tools
- Designed for the LLM application community

## 📞 Support

For issues or questions:
1. Check the [troubleshooting section](#troubleshooting)
2. Review [COMPONENT_USAGE.md](COMPONENT_USAGE.md)
3. Visit [Langflow Documentation](https://docs.langflow.org)
4. Open an issue on GitHub

## 🚀 What's Next?

Planned features:
- [ ] Export to PDF functionality
- [ ] Dark mode support
- [ ] Chart/graph integration
- [ ] Table formatting
- [ ] Syntax highlighting for code blocks
- [ ] Custom CSS injection option
- [ ] Multiple theme presets

---

**Made with ❤️ for the Langflow community**

*Star this repo if you find it useful!*
