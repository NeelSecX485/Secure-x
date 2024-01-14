import nltk
import re
import sklearn
import pandas as pd

# Load dataset into Pandas DataFrame
data = pd.read_csv("D:\Project\phishing_site_urls.csv")

# Preprocess data
X = data['links']
y = data['labels']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.3)

# Train machine learning model
model = sklearn.svm.SVC()
model.fit(X_train, y_train)

# Test model and evaluate performance
predictions = model.predict(X_test)
accuracy = sklearn.metrics.accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Implement Chatbot
def classify_link(link):
    link = link.lower() # convert link to lowercase
    link = re.sub(r'https?://', '', link) # remove http/https prefix
    prediction = model.predict([link])[0]
    if prediction == 'phishing':
        return "Warning: This link may be a phishing attempt. Do not click it."
    else:
        return "This link appears to be safe."

def chatbot():
    user_input = input("Enter a link: ")
    if 'http' in user_input or 'https' in user_input:
        classification = classify_link(user_input)
        print(classification)
    else:
        print("Not a valid link.")
        chatbot()

chatbot()
