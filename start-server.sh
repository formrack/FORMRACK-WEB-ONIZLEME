#!/bin/bash
# Formrack 3D Model Server Launcher
# Linux/macOS Shell Script

echo ""
echo "=========================================="
echo "  Formrack 3D Model Server"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3 first"
    exit 1
fi

echo "Starting server..."
echo ""
echo "Open your browser and go to:"
echo "http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 server.py
