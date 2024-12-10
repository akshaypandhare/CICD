# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the simple Flask API!",
        "description": "This is the home endpoint of our application."
    }), 200

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "message": "Application is up and running smoothly."
    }), 200

@app.route('/test')
def test_endpoint():
    return jsonify({
        "test": "Test endpoint is working",
        "result": "Success"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)