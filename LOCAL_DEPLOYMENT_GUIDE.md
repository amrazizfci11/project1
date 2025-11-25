# 🚀 Local Deployment Guide

This guide will help you deploy the Interactive Data Display as a local web application on your computer.

## 🎯 Quick Start (3 Steps)

### Step 1: Install Flask
```bash
pip install Flask
```

### Step 2: Run the Server
```bash
python app.py
```

### Step 3: Open in Browser
Open your browser and visit: **http://127.0.0.1:5000**

That's it! 🎉

---

## 📖 Detailed Instructions

### Prerequisites

- **Python 3.7+** installed on your computer
- **pip** (Python package installer)
- **Web browser** (Chrome, Firefox, Safari, or Edge)

### Installation

#### Option 1: Install Flask Only (Recommended for local deployment)
```bash
pip install Flask
```

#### Option 2: Install All Dependencies
```bash
pip install -r requirements.txt
```

Note: You don't need Langflow to run the local web server!

### Running the Application

1. **Navigate to the project directory:**
   ```bash
   cd /path/to/project1
   ```

2. **Start the Flask server:**
   ```bash
   python app.py
   ```

3. **You should see:**
   ```
   ============================================================
   🚀 Interactive Data Display - Local Web Server
   ============================================================

   Starting server...
   Open your browser and visit: http://127.0.0.1:5000

   Press CTRL+C to stop the server
   ============================================================
   ```

4. **Open your browser** and go to: `http://127.0.0.1:5000`

### Using the Web Interface

1. **Input Your Data**
   - Paste your LLM output, JSON, or text data into the large text area
   - The form accepts any text format

2. **Customize (Optional)**
   - **Title**: Change the page title
   - **Theme Color**: Choose a color or pick from presets
   - **Collapsed**: Check to start with sections collapsed

3. **Try Examples**
   - Click any example button to see how different data formats work
   - Examples include: JSON, Text Sections, LLM Response, Business Report

4. **Generate Display**
   - Click "✨ Generate Display" button
   - Your data will be displayed in a beautiful interactive format

5. **Interact with Results**
   - Click section headers to expand/collapse
   - Click "Copy" buttons to copy section content
   - Click "← Enter New Data" to go back and try different data

### Stopping the Server

Press `CTRL+C` in the terminal where the server is running.

---

## 🔧 Configuration

### Change Port

To run on a different port, edit `app.py`:

```python
app.run(debug=True, host='127.0.0.1', port=8080)  # Change 5000 to 8080
```

### Access from Other Devices on Your Network

To access from other devices (phone, tablet):

1. Edit `app.py`:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5000)
   ```

2. Find your computer's IP address:
   - **Windows**: `ipconfig` in CMD
   - **Mac/Linux**: `ifconfig` or `ip addr`

3. On other devices, visit: `http://YOUR_IP_ADDRESS:5000`

---

## 📊 API Endpoint

The application also provides a JSON API endpoint:

### POST `/api/generate`

**Request:**
```json
{
  "data": "Your data here",
  "title": "Custom Title",
  "theme_color": "#4F46E5",
  "auto_parse": true,
  "collapsed": false
}
```

**Response:**
```json
{
  "html": "<html>...</html>",
  "success": true
}
```

**Example using curl:**
```bash
curl -X POST http://127.0.0.1:5000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"data": "{\"key\": \"value\"}", "title": "My Display"}'
```

**Example using Python:**
```python
import requests

response = requests.post('http://127.0.0.1:5000/api/generate', json={
    'data': '{"summary": "Test data", "details": "More info"}',
    'title': 'API Generated Display',
    'theme_color': '#059669'
})

html = response.json()['html']
```

---

## 🎨 Supported Data Formats

### 1. JSON Objects
```json
{
  "section1": "Content here",
  "section2": {
    "nested": "data",
    "values": [1, 2, 3]
  }
}
```

### 2. Plain Text with Sections
```
Section Title 1
Content for section 1

Section Title 2
Content for section 2
```

### 3. Markdown-Style Headers
```
# Main Section
Content here

## Subsection
More content
```

### 4. LLM Responses
Any text output from ChatGPT, Claude, or other LLMs

---

## 💡 Usage Examples

### Example 1: Displaying ChatGPT Output

1. Ask ChatGPT a question
2. Copy the entire response
3. Paste into the web interface
4. Click "Generate Display"
5. Get a beautifully formatted result!

### Example 2: Formatting API Response

```python
import requests
import json

# Get data from an API
response = requests.get('https://api.example.com/data')
data = response.json()

# Convert to string
data_str = json.dumps(data, indent=2)

# Manually open browser to http://127.0.0.1:5000
# Paste data_str into the form
# Or use the API endpoint (see above)
```

### Example 3: Processing Multiple Files

```python
import os

# Read multiple text files
data_sections = {}
for filename in os.listdir('my_data_folder'):
    with open(f'my_data_folder/{filename}', 'r') as f:
        data_sections[filename] = f.read()

# Convert to JSON
import json
data_str = json.dumps(data_sections, indent=2)

# Paste into web interface or use API
```

---

## 🐛 Troubleshooting

### Port Already in Use

**Error:** `Address already in use`

**Solution:**
1. Change the port in `app.py` to a different number (e.g., 5001, 8080)
2. Or stop the process using port 5000:
   - **Windows**: `netstat -ano | findstr :5000` then `taskkill /PID [PID] /F`
   - **Mac/Linux**: `lsof -ti:5000 | xargs kill`

### Flask Not Found

**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
pip install Flask
```

### Page Not Loading

**Problem:** Browser shows "Can't connect" or "Site not reachable"

**Solutions:**
1. Make sure the server is running (check terminal)
2. Check the URL: `http://127.0.0.1:5000` (not https)
3. Try `http://localhost:5000` instead
4. Check if firewall is blocking the connection

### Data Not Displaying Correctly

**Problem:** Data shows as one big section

**Solutions:**
1. Try adding double newlines (`\n\n`) between sections for text
2. For JSON, ensure it's valid (use JSONLint.com)
3. Try one of the example buttons to verify the app works

---

## 🔒 Security Notes

### For Local Use Only

This application is designed for **local use only**. Do not expose it to the internet without proper security measures.

### For Production Deployment

If you need to deploy this to a production environment:

1. **Use a production WSGI server** (gunicorn, uWSGI)
2. **Add authentication** (login system)
3. **Use HTTPS** (SSL certificate)
4. **Add rate limiting**
5. **Validate and sanitize all inputs**
6. **Set `debug=False`** in app.py

---

## 📁 Project Structure

```
project1/
├── app.py                    # Flask web application (run this!)
├── templates/
│   └── input.html           # Input form interface
├── static/                  # (empty - could add CSS/JS files)
├── data_display_component.py # Langflow component (not needed for local)
├── test_component.py        # Test suite
├── example_output.html      # Example of generated output
└── requirements.txt         # Dependencies
```

---

## 🎓 Tips & Tricks

### 1. Keep the Server Running
Leave the server running in a terminal tab and use it throughout the day for different data.

### 2. Bookmark the Page
Add `http://127.0.0.1:5000` to your browser bookmarks for quick access.

### 3. Use Keyboard Shortcuts
- `Ctrl+A` to select all in textarea
- `Ctrl+V` to paste data quickly

### 4. Save Generated Pages
On the result page, use `Ctrl+S` or `Cmd+S` to save the HTML file.

### 5. Create Shortcuts
**Windows:** Create a `.bat` file:
```batch
@echo off
cd C:\path\to\project1
python app.py
pause
```

**Mac/Linux:** Create a `.sh` file:
```bash
#!/bin/bash
cd /path/to/project1
python app.py
```

### 6. Chrome/Edge App Mode
Run as a standalone app:
```bash
# After starting the server
chrome --app=http://127.0.0.1:5000
```

---

## 🔄 Updates & Maintenance

### Updating the Application

1. Pull latest changes from git
2. No need to restart if only templates changed
3. Restart server if `app.py` changed (Ctrl+C then `python app.py`)

### Backup Your Customizations

If you modify `app.py` or templates:
```bash
git add app.py templates/
git commit -m "Custom modifications"
```

---

## 📞 Need Help?

1. **Check this guide** - Most common issues are covered
2. **Try the examples** - Verify the app works with provided data
3. **Check the terminal** - Look for error messages
4. **Browser console** - Press F12 to see any JavaScript errors

---

## ✨ What's Next?

- Try different data formats
- Experiment with theme colors
- Use the API endpoint for automation
- Integrate with your existing workflows
- Share the generated HTML pages with your team

---

**Happy Data Displaying! 🎉**

For more information, see:
- `README.md` - Complete project documentation
- `COMPONENT_USAGE.md` - Langflow integration guide
- `test_component.py` - Testing examples
