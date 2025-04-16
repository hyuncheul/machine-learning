import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


def remove_punc(x):
    new_string = []
    for i in x:
        if i not in string.punctuation:
            new_string.append(i)

    new_string = ''.join(new_string)
    return new_string

def stop_words(x):
    new_string = []
    for i in x:
        if i.lower() not in stopwords.words('english'):
            new_string.append(i.lower())
    new_string = ''.join(new_string)
    return new_string

file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/spam.csv'
data = pd.read_csv(file_url)

data['text'] = data['text'].apply(remove_punc)
data['text'] = data['text'].apply(stop_words)

data['target'] = data['target'].map({'spam': 1, 'ham': 0})

x = data['text']
y = data['target']

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
cv.fit(x)
x = cv.transform(x)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 100)

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(x_train, y_train)
pred = model.predict(x_test)

from sklearn.metrics import accuracy_score, confusion_matrix
print(accuracy_score(y_test, pred))
print(confusion_matrix(y_test,pred))


