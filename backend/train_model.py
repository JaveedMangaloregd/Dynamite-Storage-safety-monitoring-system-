import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("dataset.csv")

X = df[["temperature", "gas", "smoke", "flame"]]
y = df["status"]

model = RandomForestClassifier()

model.fit(X, y)

pickle.dump(model, open("alarm_model.pkl", "wb"))

print("Model trained successfully")