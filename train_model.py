import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
from extract_features import extract_features

# Load dataset (your file should have columns: 'url', 'label')
data = pd.read_csv('phishing_dataset.csv')
data['features'] = data['url'].apply(extract_features)

X = pd.DataFrame(data['features'].tolist())
y = data['label']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
    


