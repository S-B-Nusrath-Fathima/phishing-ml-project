from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# Feature extraction
def extract_features(url):
    return [
        len(url),
        1 if "@" in url else 0,
        1 if url.startswith("https") else 0,
        1 if "-" in url else 0
    ]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    features = [extract_features(url)]

    prediction = model.predict(features)[0]

    if prediction == 1:
        result = "⚠️ Phishing Website Detected"
    else:
        result = "✅ Safe Website"

    return render_template('result.html', url=url, result=result)

if __name__ == "__main__":
    app.run(debug=True)