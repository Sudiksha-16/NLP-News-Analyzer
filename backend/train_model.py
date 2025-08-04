# train_model.py
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("news_headlines.csv")

df = df[['title', 'category']].dropna()

X = df['title']
y = df['category']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

joblib.dump(model, "news_classifier_model.pkl")
joblib.dump(vectorizer, "news_vectorizer.pkl")

print("Model and vectorizer saved successfully.")
