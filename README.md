# 📰 NLP News Analyzer – Sentiment Analysis & News Category Classification Web App

A full-stack Natural Language Processing (NLP) based web application that offers two key functionalities:

- ✅ **Sentiment Analysis**: Determines whether the input text expresses **Positive**, **Negative**, or **Neutral** sentiment using **TextBlob**.
- 🗂 **News Category Classification**: Classifies news headlines into categories like **Sports**, **Politics**, **Technology**, etc., using **TF-IDF** + **Logistic Regression**.


## 🚀 Features

- 🔍 **Real-time Sentiment Analysis**
- 🧠 **News Headline Category Prediction**
- 🌙 **Light/Dark Mode Toggle**
- ⚡ Fast Backend with **Flask**
- 🖥️ Intuitive Frontend with **React.js**
- 📦 Pre-trained ML Model with **Scikit-learn**


## 🛠️ Technologies Used

### Frontend (React.js)
- React.js
- CSS3 (Responsive Design)
- Fetch API

### Backend (Flask)
- Flask + Flask-CORS
- Python
- TextBlob (Sentiment Analysis)
- Joblib (Model Saving/Loading)

### Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression


## 📚 Dataset Used

**Comprehensive News Articles Dataset**

- Includes labeled news across various domains like:
  - 📰 Politics
  - 🏈 Sports
  - 💻 Technology
- Fields: `title`, `description`, `content`, `source`, `category`
- Purpose: Used to train ML model to classify headlines.


## 🔄 NLP Workflow

### Step 1: Dataset Preparation
- Removed null values
- Converted text to lowercase

### Step 2: Feature Extraction
- Used `TF-IDF Vectorizer` to convert text to numeric format

### Step 3: Model Training
- Trained `Logistic Regression` model
- Used `train_test_split` for evaluation

### Step 4: Save Model
- `news_classifier_model.pkl` – Trained model
- `news_vectorizer.pkl` – Fitted TF-IDF vectorizer

### Step 5: Sentiment Analysis
- Implemented with `TextBlob`


## 🔁 Application Workflow

1. User enters text via the frontend.
2. Request is sent to Flask via REST API.
3. Flask:
   - Loads saved model/vectorizer
   - Performs prediction
4. Result is returned and displayed on screen.

## 🚀 Conclusion

This project showcases the potential of combining modern technologies like React.js, Node.js, Express, and MongoDB to build a powerful, full-stack application. By integrating sentiment analysis and text summarization using advanced NLP techniques, the app delivers meaningful insights from textual data. Feel free to explore, contribute, and enhance the project further!

Thank you for checking it out! 🌟

