import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the dataset
df = pd.read_csv("facebook_ads.csv", encoding="ISO-8859-1")

# 2. Features & target
X = df[["Time Spent on Site", "Salary"]]
y = df["Clicked"]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

# 4. Model training
clf = LogisticRegression()
clf.fit(X_train, y_train)

# 5. Save the model
pickle.dump(clf, open("my_model.pkl", "wb"))

print("Model saved successfully!")