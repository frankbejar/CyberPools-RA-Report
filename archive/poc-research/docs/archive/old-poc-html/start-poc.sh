#!/bin/bash
# Quick start script for CyberPools PDF POC

echo "🚀 Starting CyberPools PDF Generator POC..."
echo ""
echo "📂 Current directory: $(pwd)"
echo ""
echo "🌐 Starting local web server on port 8000..."
echo ""
echo "✅ Once the server starts, open your browser to:"
echo ""
echo "   👉  http://localhost:8000/local-poc.html"
echo ""
echo "💡 Press Ctrl+C to stop the server when done"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Start Python HTTP server
python3 -m http.server 8000
