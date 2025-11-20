#!/bin/bash
# CyberPools Report Generator - Mac/Linux Quick Start
# File: 7.3 - run.sh
# Updated: October 2025 - Style Guide v1.0 Compliant

echo ""
echo "==============================================================="
echo "  CyberPools Risk Assessment Report Generator"
echo "  Style Guide v1.0 Compliant"
echo "==============================================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python 3 is not installed"
    echo "Install Python 3.8+ from https://www.python.org/downloads/"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Check if we're in the correct directory
if [ ! -f "scripts/transform_and_generate.py" ] && [ ! -f "transform_and_generate.py" ]; then
    echo ""
    echo "⚠️  WARNING: Cannot find transform_and_generate.py"
    echo "Make sure you're running this from the cyberpools-report folder"
    echo ""
    exit 1
fi

# Check if dependencies are installed
python3 -c "import jinja2" 2>/dev/null
if [ $? -ne 0 ]; then
    echo ""
    echo "📦 Installing dependencies..."
    
    # Try to find requirements.txt
    if [ -f "docs/requirements.txt" ]; then
        python3 -m pip install -r docs/requirements.txt
    elif [ -f "requirements.txt" ]; then
        python3 -m pip install -r requirements.txt
    else
        echo "❌ ERROR: Cannot find requirements.txt"
        echo "Expected location: docs/requirements.txt or ./requirements.txt"
        exit 1
    fi
    
    if [ $? -ne 0 ]; then
        echo "❌ ERROR: Failed to install dependencies"
        exit 1
    fi
    
    echo "✓ Dependencies installed"
fi

echo "✓ All dependencies ready"
echo ""

# Run the script from the correct location
if [ -f "scripts/transform_and_generate.py" ]; then
    python3 scripts/transform_and_generate.py "$@"
elif [ -f "transform_and_generate.py" ]; then
    python3 transform_and_generate.py "$@"
else
    echo "❌ ERROR: Cannot find transform_and_generate.py"
    exit 1
fi

echo ""
echo "Press any key to exit..."
read -n 1
