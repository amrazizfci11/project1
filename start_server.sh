#!/bin/bash

# Interactive Data Display - Local Server Startup Script

echo "=========================================="
echo "🚀 Interactive Data Display Server"
echo "=========================================="
echo ""

# Check if Flask is installed
if ! python -c "import flask" 2>/dev/null; then
    echo "⚠️  Flask is not installed!"
    echo ""
    echo "Installing Flask..."
    pip install Flask
    echo ""
fi

# Start the server
echo "Starting server..."
echo ""
python app.py
