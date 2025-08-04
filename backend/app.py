from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("news_classifier_model.pkl")
vectorizer = joblib.load("news_vectorizer.pkl")

def classify_news(text):
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    return prediction

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text', '')
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity

    if sentiment > 0:
        result = "Positive"
    elif sentiment < 0:
        result = "Negative"
    else:
        result = "Neutral"

    return jsonify({'result': result})

@app.route('/classify_news', methods=['POST'])
def classify_news_route():
    data = request.json
    text = data.get('text', '')
    category = classify_news(text)
    return jsonify({'result': category})

if __name__ == '__main__':
    app.run(debug=True)
