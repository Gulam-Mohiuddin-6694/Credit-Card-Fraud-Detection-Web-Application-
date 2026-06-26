#!/bin/bash

echo "========================================"
echo "Credit Card Fraud Detection Web App"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
else
    echo "No virtual environment found."
    echo "Running with system Python..."
fi

echo ""
echo "Starting Flask application..."
echo ""
echo "The application will be available at:"
echo "http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo "========================================"
echo ""

python app.py
