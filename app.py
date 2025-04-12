from flask import Flask, render_template, request
import pickle
from extract_features import extract_features

app = Flask(__name__)

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        features = extract_features(url)
        prediction = model.predict([features])[0]
        result = "Phishing Website" if prediction == 1 else "Legitimate Website"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
