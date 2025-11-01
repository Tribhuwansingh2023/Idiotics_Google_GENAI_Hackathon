from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re
import string
from database import EyeSpyDatabase
import hashlib

app = Flask(__name__)
CORS(app)

# Load the trained model and vectorizer
try:
    vectorizer = joblib.load('vectorizer.jb')
    model = joblib.load('model.jb')
except FileNotFoundError:
    vectorizer = None
    model = None

# Initialize database
db = EyeSpyDatabase()

def clean_text(text):
    """Cleans the input text in the same way as the training data."""
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

@app.route('/api/predict', methods=['POST'])
def predict():
    """Endpoint to predict if a news article is real or fake."""
    if not model or not vectorizer:
        return jsonify({"error": "Model or vectorizer not loaded. Please train the model first."}), 500

    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Please provide the news article text in the 'text' field."}), 400

    news_text = data['text']
    if not news_text.strip():
        return jsonify({"error": "Text cannot be empty."}), 400

    # Create a hash of the content to check for cached results
    content_hash = hashlib.sha256(news_text.encode('utf-8')).hexdigest()
    cached_result = db.get_analysis_by_hash(content_hash)

    if cached_result:
        # Convert ObjectId to string for JSON serialization
        cached_result["_id"] = str(cached_result["_id"])
        return jsonify({
            "success": True,
            "cached": True,
            "result": cached_result
        })

    try:
        # Clean the text and make a prediction
        cleaned_text = clean_text(news_text)
        vectorized_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(vectorized_text)[0]
        prediction_proba = model.predict_proba(vectorized_text)[0]

        is_fake = prediction == 0
        confidence = prediction_proba[0] if is_fake else prediction_proba[1]

        result = {
            "is_fake": bool(is_fake),
            "confidence": float(confidence),
            "fake_probability": float(prediction_proba[0]),
            "real_probability": float(prediction_proba[1]),
            "original_text": news_text
        }

        # Save to database
        db.save_analysis(content_hash, result)

        return jsonify({
            "success": True,
            "cached": False,
            "result": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    try:
        stats = db.get_analysis_stats()
        return jsonify({
            "status": "healthy",
            "message": "EyeSpy API is running",
            "database": "connected",
            "stats": stats
        })
    except Exception as e:
        return jsonify({
            "status": "healthy",
            "message": "EyeSpy API is running",
            "database": "disconnected",
            "error": str(e)
        })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get analysis statistics"""
    try:
        stats = db.get_analysis_stats()
        return jsonify({"success": True, "stats": stats})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)