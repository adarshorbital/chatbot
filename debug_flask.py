#!/usr/bin/env python3
"""
Debug script to identify the 503 error cause
"""

import os
import sys
import traceback

def check_environment():
    """Check environment variables"""
    print("=== Environment Check ===")
    api_key = os.environ.get("GENAI_API_KEY")
    print(f"GENAI_API_KEY set: {'Yes' if api_key else 'No'}")
    if api_key:
        print(f"API key length: {len(api_key)}")
    
    print(f"CONFIG_FILE: {os.environ.get('CONFIG_FILE', 'Not set')}")
    print(f"SECRET_KEY: {'Set' if os.environ.get('SECRET_KEY') else 'Not set'}")
    print()

def check_files():
    """Check required files"""
    print("=== File Check ===")
    required_files = [
        'config.yaml',
        'templates/index.html',
        'static/lattice_ai_icon.png',
        'static/purdue-genai-studio-logo.png'
    ]
    
    for file_path in required_files:
        exists = os.path.exists(file_path)
        print(f"{file_path}: {'✓' if exists else '✗'}")
        if exists:
            try:
                size = os.path.getsize(file_path)
                print(f"  Size: {size} bytes")
            except:
                print(f"  Size: Cannot read")
    print()

def check_directories():
    """Check required directories"""
    print("=== Directory Check ===")
    required_dirs = ['templates', 'static', 'uploads', 'logs']
    
    for dir_path in required_dirs:
        exists = os.path.exists(dir_path)
        is_dir = os.path.isdir(dir_path) if exists else False
        print(f"{dir_path}: {'✓' if exists and is_dir else '✗'}")
        if exists and is_dir:
            try:
                contents = os.listdir(dir_path)
                print(f"  Contents: {contents}")
            except:
                print(f"  Contents: Cannot read")
    print()

def test_imports():
    """Test required imports"""
    print("=== Import Check ===")
    imports_to_test = [
        'flask',
        'flask_cors',
        'flask_limiter',
        'yaml',
        'requests'
    ]
    
    for module in imports_to_test:
        try:
            __import__(module)
            print(f"{module}: ✓")
        except ImportError as e:
            print(f"{module}: ✗ - {e}")
    
    # Test optional imports
    optional_imports = [
        ('PyPDF2', 'pypdf2'),
        ('pandas', 'pandas')
    ]
    
    for display_name, module_name in optional_imports:
        try:
            __import__(module_name)
            print(f"{display_name}: ✓ (optional)")
        except ImportError:
            print(f"{display_name}: ✗ (optional)")
    print()

def test_config_loading():
    """Test config loading"""
    print("=== Config Loading Test ===")
    try:
        import yaml
        config_path = os.environ.get('CONFIG_FILE', 'config.yaml')
        
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            print(f"Config loaded successfully from {config_path}")
            print(f"Course name: {config.get('course', {}).get('name', 'Not set')}")
            print(f"GenAI base URL: {config.get('genai', {}).get('base_url', 'Not set')}")
        else:
            print(f"Config file {config_path} not found - will use defaults")
    except Exception as e:
        print(f"Config loading error: {e}")
        traceback.print_exc()
    print()

def test_flask_basic():
    """Test basic Flask functionality"""
    print("=== Flask Basic Test ===")
    try:
        from flask import Flask
        app = Flask(__name__)
        
        @app.route('/test')
        def test():
            return "Flask is working"
        
        print("Flask app creation: ✓")
        
        # Test if we can create a test client
        with app.test_client() as client:
            response = client.get('/test')
            print(f"Test route response: {response.status_code}")
            
    except Exception as e:
        print(f"Flask basic test error: {e}")
        traceback.print_exc()
    print()

def test_template_rendering():
    """Test template rendering"""
    print("=== Template Rendering Test ===")
    try:
        from flask import Flask, render_template_string
        
        app = Flask(__name__)
        
        # Test basic template rendering
        with app.app_context():
            result = render_template_string("Hello {{ name }}", name="World")
            print(f"Basic template rendering: ✓ ('{result}')")
            
        # Test if templates directory is accessible
        if os.path.exists('templates/index.html'):
            with app.app_context():
                # Try to render the actual template with minimal config
                test_config = {
                    'COURSE_NAME': 'TEST',
                    'ASSISTANT_NAME': 'TEST',
                    'ASSISTANT_TITLE': 'TEST',
                    'WELCOME_MESSAGE': 'TEST',
                    'INPUT_PLACEHOLDER': 'TEST',
                    'LOGO_FILE': 'test.png',
                    'FOOTER_TEXT': 'TEST'
                }
                
                from flask import render_template
                result = render_template('index.html', health_status=True, config=test_config)
                print("Template rendering: ✓")
        else:
            print("Template rendering: ✗ - index.html not found")
            
    except Exception as e:
        print(f"Template rendering error: {e}")
        traceback.print_exc()
    print()

if __name__ == '__main__':
    print("Flask App Debug Tool")
    print("=" * 50)
    
    check_environment()
    check_files()
    check_directories()
    test_imports()
    test_config_loading()
    test_flask_basic()
    test_template_rendering()
    
    print("=" * 50)
    print("Debug complete. Check the results above for issues.")