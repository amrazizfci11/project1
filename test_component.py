"""
Test script for the Interactive Data Display Component
Run this to test the component locally without Langflow
"""

import json
from data_display_component import InteractiveDataDisplay
from langflow.schema import Message


def test_with_json():
    """Test with JSON data"""
    print("Testing with JSON data...")

    component = InteractiveDataDisplay()
    component.data_input = json.dumps({
        "summary": "This is a summary of the analysis",
        "key_findings": "- Finding 1\n- Finding 2\n- Finding 3",
        "recommendations": "1. Do this\n2. Do that\n3. Do something else",
        "metrics": {
            "accuracy": 0.95,
            "precision": 0.92,
            "recall": 0.88
        }
    })
    component.title = "Test Report - JSON Data"
    component.theme_color = "#059669"
    component.auto_parse_json = True
    component.collapsed_by_default = False

    result = component.build_display()
    with open('test_output_json.html', 'w', encoding='utf-8') as f:
        f.write(result.text)

    print("✓ JSON test completed. Check test_output_json.html")


def test_with_text():
    """Test with plain text data"""
    print("Testing with plain text data...")

    component = InteractiveDataDisplay()
    component.data_input = """
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

# Risk Analysis
Competition is increasing in the market.
We need to stay ahead with innovation.
"""
    component.title = "Quarterly Business Review"
    component.theme_color = "#4F46E5"
    component.auto_parse_json = True
    component.collapsed_by_default = False

    result = component.build_display()
    with open('test_output_text.html', 'w', encoding='utf-8') as f:
        f.write(result.text)

    print("✓ Text test completed. Check test_output_text.html")


def test_with_llm_style_response():
    """Test with LLM-style conversational response"""
    print("Testing with LLM-style response...")

    component = InteractiveDataDisplay()
    component.data_input = """
Based on your question about implementing a user authentication system, here's my analysis:

**Architecture Overview**
For a modern web application, I recommend implementing JWT-based authentication with refresh tokens. This provides a good balance between security and user experience.

**Key Components Required**
1. Authentication Service: Handle login, logout, and token generation
2. User Database: Store user credentials (hashed passwords using bcrypt)
3. Middleware: Validate tokens on protected routes
4. Frontend State Management: Store and manage auth state

**Security Considerations**
- Always use HTTPS in production
- Implement rate limiting on login endpoints
- Use secure password hashing (bcrypt, argon2)
- Set appropriate token expiration times
- Implement CSRF protection
- Consider 2FA for sensitive operations

**Implementation Steps**
Step 1: Set up user model and database schema
Step 2: Create authentication endpoints (login, register, refresh)
Step 3: Implement JWT token generation and validation
Step 4: Add authentication middleware
Step 5: Protect routes that require authentication
Step 6: Implement frontend auth flow

**Code Example**
Here's a basic structure for the authentication service:
- POST /api/auth/register - Create new user
- POST /api/auth/login - Authenticate user
- POST /api/auth/refresh - Refresh access token
- POST /api/auth/logout - Invalidate tokens

**Testing Strategy**
- Unit tests for authentication logic
- Integration tests for auth endpoints
- Security testing (penetration testing)
- Load testing for authentication endpoints

**Estimated Timeline**
- Basic implementation: 2-3 days
- Security hardening: 1-2 days
- Testing: 1-2 days
- Total: 4-7 days for a production-ready system
"""
    component.title = "LLM Response: Authentication System"
    component.theme_color = "#7C3AED"
    component.auto_parse_json = True
    component.collapsed_by_default = False

    result = component.build_display()
    with open('test_output_llm.html', 'w', encoding='utf-8') as f:
        f.write(result.text)

    print("✓ LLM test completed. Check test_output_llm.html")


def test_collapsed_mode():
    """Test with collapsed sections by default"""
    print("Testing collapsed mode...")

    component = InteractiveDataDisplay()
    component.data_input = json.dumps({
        "section_1": "Content for section 1",
        "section_2": "Content for section 2",
        "section_3": "Content for section 3",
        "section_4": "Content for section 4",
        "section_5": "Content for section 5"
    })
    component.title = "Collapsed Sections Demo"
    component.theme_color = "#DC2626"
    component.auto_parse_json = True
    component.collapsed_by_default = True

    result = component.build_display()
    with open('test_output_collapsed.html', 'w', encoding='utf-8') as f:
        f.write(result.text)

    print("✓ Collapsed mode test completed. Check test_output_collapsed.html")


def test_error_handling():
    """Test error handling"""
    print("Testing error handling...")

    component = InteractiveDataDisplay()
    # This should work fine, but let's test with unusual input
    component.data_input = "Simple single-line text without any structure"
    component.title = "Error Handling Test"
    component.theme_color = "#EA580C"
    component.auto_parse_json = True
    component.collapsed_by_default = False

    result = component.build_display()
    with open('test_output_error.html', 'w', encoding='utf-8') as f:
        f.write(result.text)

    print("✓ Error handling test completed. Check test_output_error.html")


if __name__ == "__main__":
    print("=" * 60)
    print("Interactive Data Display Component - Test Suite")
    print("=" * 60)
    print()

    try:
        test_with_json()
        print()
        test_with_text()
        print()
        test_with_llm_style_response()
        print()
        test_collapsed_mode()
        print()
        test_error_handling()
        print()
        print("=" * 60)
        print("All tests completed successfully!")
        print("Open the generated HTML files in your browser to see results.")
        print("=" * 60)
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
