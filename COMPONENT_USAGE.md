# Interactive Data Display Component for Langflow

A beautiful, interactive Langflow component that displays LLM output data in a professional web page with collapsible sections and copy-to-clipboard functionality.

## Features

- 🎨 **Beautiful UI** - Modern gradient background with smooth animations
- 📦 **Sectioned Display** - Automatically groups data into collapsible sections
- 📋 **Copy to Clipboard** - One-click copy functionality for each section
- 🎯 **Auto JSON Parsing** - Intelligently parses JSON data into structured sections
- 🎨 **Customizable Theme** - Change colors to match your brand
- 📱 **Responsive Design** - Works perfectly on desktop and mobile
- ⚡ **Interactive Panels** - Expand/collapse sections with smooth animations

## Installation

### Option 1: Using LANGFLOW_COMPONENTS_PATH (Recommended)

1. Create a custom components directory structure:
```bash
mkdir -p my_components/display
```

2. Copy the component file:
```bash
cp data_display_component.py my_components/display/
```

3. Create an `__init__.py` file:
```bash
touch my_components/display/__init__.py
```

4. Set the environment variable before starting Langflow:
```bash
export LANGFLOW_COMPONENTS_PATH=/path/to/my_components
langflow run
```

### Option 2: Using Langflow's Default Components Directory

1. Find your Langflow installation directory
2. Navigate to the components folder (usually `langflow/components/`)
3. Create a new directory called `display`
4. Copy `data_display_component.py` into this directory
5. Restart Langflow

### Option 3: Direct Import in Langflow UI

1. Open Langflow web interface
2. Click on "Components" in the sidebar
3. Click "Import Component"
4. Upload the `data_display_component.py` file
5. The component will be available in your components list

## Component Inputs

| Input | Type | Description | Default |
|-------|------|-------------|---------|
| **Data Input** | MessageText | LLM output data (text, JSON, or formatted data) | Required |
| **Page Title** | String | Main title for the display page | "LLM Data Display" |
| **Theme Color** | String | Primary color in hex format | "#4F46E5" |
| **Auto Parse JSON** | Boolean | Automatically parse JSON into sections | True |
| **Collapsed by Default** | Boolean | Start with sections collapsed | False |

## Usage Examples

### Example 1: Display LLM Chat Response

```
Flow: OpenAI → Interactive Data Display
```

Connect the OpenAI (or any LLM) output directly to the Data Input.

**Input:**
```
Q: What are the benefits of AI?

A: 1. Automation - Reduces manual tasks
2. Efficiency - Processes data faster
3. Accuracy - Minimizes human error
```

**Result:** Beautifully formatted sections with copy buttons

### Example 2: Display JSON Data

**Input:**
```json
{
  "user_profile": {
    "name": "John Doe",
    "email": "john@example.com",
    "role": "Admin"
  },
  "statistics": {
    "total_users": 1234,
    "active_sessions": 56,
    "api_calls": 9876
  },
  "recent_activity": [
    "Logged in",
    "Updated profile",
    "Created new project"
  ]
}
```

**Result:** Each top-level key becomes a collapsible section with formatted content

### Example 3: Display Structured Analysis

**Input:**
```
# Executive Summary
This quarter showed strong growth with revenue up 23%.

# Key Metrics
- Revenue: $1.2M (+23%)
- Users: 15,000 (+15%)
- Retention: 89% (+5%)

# Recommendations
1. Increase marketing spend
2. Focus on user retention
3. Expand to new markets
```

**Result:** Automatically splits into sections based on headers

### Example 4: Custom Themed Display

**Inputs:**
- Data Input: Your LLM output
- Page Title: "Customer Analysis Report"
- Theme Color: "#DC2626" (Red)
- Collapsed by Default: True

**Result:** Red-themed interface with all sections collapsed initially

## Sample Flows

### Flow 1: Research Assistant
```
User Input → OpenAI (with system prompt) → Interactive Data Display
```

**System Prompt:**
```
You are a research assistant. Format your response as JSON with these sections:
- summary: Brief overview
- key_findings: Main discoveries
- recommendations: Suggested actions
- sources: References used
```

### Flow 2: Data Analysis Pipeline
```
CSV File → Data Processor → OpenAI Analysis → Interactive Data Display
```

### Flow 3: Multi-Step Analysis
```
User Question → Agent → Multiple Tools → Combine Text → Interactive Data Display
```

## Customization

### Changing Colors

Popular color schemes:

| Theme | Hex Code | Description |
|-------|----------|-------------|
| Indigo | #4F46E5 | Default, professional |
| Red | #DC2626 | Bold, attention-grabbing |
| Green | #059669 | Fresh, success-oriented |
| Purple | #7C3AED | Creative, modern |
| Blue | #2563EB | Trust, corporate |
| Orange | #EA580C | Energetic, warm |

### Advanced Customization

To modify the HTML/CSS, edit the `generate_html()` method in the component file:

```python
def generate_html(self, sections: List[Dict[str, Any]]) -> str:
    # Modify the HTML template here
    # Change styles, layout, add new features
    ...
```

## Data Format Support

The component intelligently handles:

1. **Plain Text** - Splits by double newlines into sections
2. **JSON Objects** - Each key becomes a section
3. **JSON Arrays** - Each item becomes a numbered section
4. **Markdown-like** - Detects headers (#, ##, ###) as section titles
5. **Mixed Format** - Combines multiple parsing strategies

## Tips & Best Practices

1. **For Best Results:**
   - Structure your LLM prompts to output organized data
   - Use JSON format for complex nested data
   - Add clear headers/titles to text sections

2. **Performance:**
   - Component handles large outputs (up to several MB)
   - Long sections remain scrollable within the panel
   - Collapsed mode improves initial load for many sections

3. **Integration:**
   - Works with any Langflow component that outputs text/messages
   - Can be chained with other components
   - Output is a Message object containing full HTML

4. **Mobile Friendly:**
   - Automatically adjusts layout for small screens
   - Touch-friendly buttons and panels
   - Readable font sizes on all devices

## Troubleshooting

### Component not appearing in Langflow

1. Check that `__init__.py` exists in the component directory
2. Verify LANGFLOW_COMPONENTS_PATH is set correctly
3. Restart Langflow after adding the component
4. Check Langflow logs for import errors

### HTML not rendering properly

- The component outputs HTML in a Message object
- Use a compatible output component (Chat Output, Text Output)
- Some viewers may show raw HTML - use a browser-based output

### JSON parsing fails

- Enable "Auto Parse JSON" to automatically detect JSON
- Manually format your data if auto-parsing doesn't work
- Check that JSON is valid using a JSON validator

### Copy button not working

- Modern browsers required (Chrome, Firefox, Edge, Safari)
- HTTPS may be required for clipboard API
- Check browser console for errors

## Advanced Features

### Programmatic Usage

If using in Python scripts:

```python
from data_display_component import InteractiveDataDisplay

# Create component instance
display = InteractiveDataDisplay()

# Set parameters
display.data_input = '{"key": "value"}'
display.title = "My Report"
display.theme_color = "#059669"

# Generate output
message = display.build_display()

# Get HTML
html_output = message.text

# Save to file
with open('output.html', 'w') as f:
    f.write(html_output)
```

### Extending the Component

Add custom input types:

```python
# In the inputs list
IntInput(
    name="max_sections",
    display_name="Max Sections",
    info="Maximum number of sections to display",
    value=10,
)
```

Add custom parsing logic:

```python
def parse_data(self, data: str) -> List[Dict[str, Any]]:
    # Add your custom parsing logic
    if "###CUSTOM###" in data:
        # Handle custom format
        pass
    # ... rest of method
```

## Component Architecture

```
InteractiveDataDisplay (Component)
│
├── Inputs
│   ├── data_input (MessageTextInput)
│   ├── title (StrInput)
│   ├── theme_color (StrInput)
│   ├── auto_parse_json (BoolInput)
│   └── collapsed_by_default (BoolInput)
│
├── Methods
│   ├── parse_data() - Parse input into sections
│   ├── generate_html() - Create HTML output
│   ├── _format_value() - Format data values
│   ├── _escape_html() - Sanitize HTML
│   └── build_display() - Main build method
│
└── Output
    └── Message(text=html)
```

## License

This component is provided as-is for use with Langflow. Feel free to modify and extend it for your needs.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review Langflow documentation: https://docs.langflow.org
3. Check Langflow GitHub: https://github.com/langflow-ai/langflow

## Version History

- **v1.0.0** - Initial release with core features
  - Interactive collapsible sections
  - Copy to clipboard functionality
  - Auto JSON parsing
  - Responsive design
  - Customizable theming
