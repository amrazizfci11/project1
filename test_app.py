"""
Quick test to verify the Flask app can start correctly
"""

import sys

# Test imports
print("Testing imports...")
try:
    from flask import Flask, render_template, request, jsonify
    print("✓ Flask imports successful")
except ImportError as e:
    print(f"✗ Flask import failed: {e}")
    sys.exit(1)

# Test app.py can be imported
print("\nTesting app.py...")
try:
    from app import app, DataDisplayGenerator
    print("✓ app.py imports successful")
except ImportError as e:
    print(f"✗ app.py import failed: {e}")
    sys.exit(1)

# Test DataDisplayGenerator
print("\nTesting DataDisplayGenerator...")
try:
    generator = DataDisplayGenerator()
    test_data = '{"test": "data", "section": "content"}'
    html = generator.generate(test_data, title="Test")
    assert "test" in html.lower()
    assert "data" in html.lower()
    print("✓ DataDisplayGenerator works correctly")
except Exception as e:
    print(f"✗ DataDisplayGenerator test failed: {e}")
    sys.exit(1)

# Test Flask routes
print("\nTesting Flask routes...")
try:
    with app.test_client() as client:
        # Test index route
        response = client.get('/')
        assert response.status_code == 200
        print("✓ Index route (/) works")

        # Test display route with POST
        response = client.post('/display', data={
            'data': '{"test": "data"}',
            'title': 'Test Title',
            'theme_color': '#4F46E5',
            'collapsed': 'off'
        })
        assert response.status_code == 200
        assert b'Test Title' in response.data or b'test' in response.data
        print("✓ Display route (/display) works")

        # Test API route
        response = client.post('/api/generate',
                              json={'data': '{"api": "test"}'},
                              content_type='application/json')
        assert response.status_code == 200
        json_response = response.get_json()
        assert json_response['success'] == True
        print("✓ API route (/api/generate) works")

except Exception as e:
    print(f"✗ Flask routes test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 60)
print("✅ All tests passed! The Flask app is ready to run.")
print("=" * 60)
print("\nTo start the server, run:")
print("  python app.py")
print("\nThen open your browser to:")
print("  http://127.0.0.1:5000")
print("=" * 60)
