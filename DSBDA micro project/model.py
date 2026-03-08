import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

fake["label"] = 0
true["label"] = 1

data = pd.concat([fake, true])

x = data["text"]
y = data["label"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

x_train = vectorizer.fit_transform(x_train)

model = PassiveAggressiveClassifier()
model.fit(x_train, y_train)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model saved")