import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Sample dataset
data = {
    'length': [20, 75, 60, 15, 90, 25],
    'has_at': [0, 1, 0, 0, 1, 0],
    'has_https': [1, 0, 1, 1, 0, 1],
    'has_dash': [0, 1, 1, 0, 1, 0],
    'label': [0, 1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

X = df[['length', 'has_at', 'has_https', 'has_dash']]
y = df['label']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model as model.pkl
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ model.pkl created successfully!")