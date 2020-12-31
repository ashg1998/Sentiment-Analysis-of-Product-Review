# -*- coding: utf-8 -*-
"""Sentiment Analysis of product Review using LSTM.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oJVE4J0YPQaQoNy_1ye0fswjDjOmvOt_
"""

from google.colab import drive
drive.mount("/content/drive")

"""Task#1: Understand The Problem Statement And Business Case"""

!pip install nltk

!pip install gensim

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
import plotly.express as px
#TensorF;ow
import tensorflow as tf
from tensorflow.keras.preprocessing.text import one_hot, Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Dense, Flatten, Embedding, Input, LSTM, Conv1D, MaxPool1D, Bidirectional, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical

stock_df = pd.read_csv("/content/drive/My Drive/Colab Notebooks/stock_sentiment.csv")

stock_df.isnull().sum()

stock_df.head()

stock_df.info()

stock_df['Sentiment'].value_counts()

sns.countplot(stock_df['Sentiment'])

stock_df['Sentiment'].nunique()

"""Task 3: Data Cleaning removing puntuation marks."""

import re
import string
def remove_pun(message):
  test_punch_removed = [char for char in message if char not in string.punctuation]
  test_punch_removed = ''.join(test_punch_removed)

  return test_punch_removed

stock_df['Text Without Punctuation'] = stock_df['Text'].apply(remove_pun)

stock_df.head()

def remove_pun(message):
  setence = re.sub('[^a-zA-z0-9]',' ',message)
  sentence = setence.split()
  sentence = ' '.join(sentence)
  return(sentence)

s1="Ashish, Is a good.! Boy"
print(remove_pun(s1))

stock_df['Text Without Punctuation1'] = stock_df['Text'].apply(remove_pun)

stock_df.head()

"""Task 4: Data Cleaning Removing Stopwords"""

nltk.download('stopwords')

stopwords.words('english')

ps = PorterStemmer()
def remove_stopwords(message):
    reviews = message.split()
    reviews = [ps.stem(word) for word in reviews if not word in set(stopwords.words('english'))]
    reviews = ' '.join(reviews)
    return(reviews)

stock_df['with out stop words1'] = stock_df['Text Without Punctuation1'].apply(remove_stopwords)

stock_df.head()

from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use','will','aap','co','day','user','stock','today','week','year','https'])

# Remove stopwords and remove short words (less than 2 characters)
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if len(token) >= 3 and token not in stop_words:
            result.append(token)
            
    return result

stock_df['Text Without Punc & Stopwords'] = stock_df['Text Without Punctuation'].apply(preprocess)

stock_df.head()

"""Task #5: Plot WORDCLOUD"""

stock_df['Text Without Punc & Stopwords joined'] = stock_df['Text Without Punc & Stopwords'].apply(lambda x: " ".join(x))

stock_df.head()

#Positive Sentiments
plt.figure(figsize=(20,20))
wc= WordCloud(max_words=1000, width=1600,height=800).generate(" ".join(stock_df[stock_df['Sentiment']==1]['Text Without Punc & Stopwords joined']))
plt.imshow(wc)

#Negative Sentiments
plt.figure(figsize=(20,20))
wc= WordCloud(max_words=1000, width=1600,height=800).generate(" ".join(stock_df[stock_df['Sentiment']==0]['Text Without Punc & Stopwords joined']))
plt.imshow(wc)

"""TAsk #6: Visualize Cleaned Datasets"""

nltk.download('punkt')

nltk.word_tokenize(stock_df['Text Without Punc & Stopwords joined'][0])

"""Counting number of words."""

maxlen = -1

for doc in stock_df['Text Without Punc & Stopwords joined']:
  tokens = nltk.word_tokenize(doc)
  if(maxlen< len(tokens)):
    maxlen=len(tokens)

print('Maximum number of words in any document', maxlen)

tweets_length = [len(nltk.word_tokenize(x)) for x in stock_df['Text Without Punc & Stopwords joined'] ]

fig = px.histogram(x= tweets_length, nbins = 50)
fig.show()

tweets_length_0 =  [len(nltk.word_tokenize(x)) for x in  stock_df[stock_df['Sentiment']==0]['Text Without Punc & Stopwords joined']]
sns.countplot(x=tweets_length_0)

"""Task 7: Preparing the Data By Tokenizing And Padding"""

list_of_words = []
for i in stock_df['Text Without Punc & Stopwords']:
  for j in i:
    list_of_words.append(j)

total_words = len(list(set(list_of_words)))

total_words

X= stock_df['Text Without Punc & Stopwords']
y = stock_df['Sentiment']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train ,y_test = train_test_split(X,y, test_size = 0.2)

X_train.shape

X_test.shape

tokenizer = Tokenizer(num_words=total_words)
tokenizer.fit_on_texts(X_train)

#Training Data
train_sequence = tokenizer.texts_to_sequences(X_train)
#Testing Data
test_sequences = tokenizer.texts_to_sequences(X_test)

train_sequence

print("The encoding for document\n",X_train[1:2], "is:", train_sequence[1])

#Add padding to training and testing
padding_train = pad_sequences(train_sequence, maxlen=29)
padding_test = pad_sequences(test_sequences, maxlen= 29)

for i, doc in enumerate(padding_train[:3]):
  print("The Padding Encoding for Document:",i+1,"is ",doc)

y_train_cat = to_categorical(y_train, 2)
y_test_cat = to_categorical(y_test,2)

padding_train = pad_sequences(train_sequence, maxlen=15)
padding_test = pad_sequences(test_sequences, maxlen= 15)

len(padding_train[0])

#Sequential Model
model = Sequential()
model.add(Embedding(total_words,output_dim=512))
#bidirectional RNN and LSTM
model.add(LSTM(256))
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(2,activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
model.summary()

#Sequential Model
model = Sequential()
model.add(Embedding(total_words,output_dim=256))
#bidirectional RNN and LSTM
model.add(LSTM(256))
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(2,activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
model.summary()

# train the model
model.fit(padding_train, y_train_cat, batch_size = 32, validation_split = 0.2, epochs = 2)

"""Evaluating Model:"""

#make prediction
pred = model.predict(padding_test)

#make prediction
prediction = []
for i in pred:
  prediction.append(np.argmax(i))

#original values
original = []
for i in y_test_cat:
  original.append(np.argmax(i))

#accuracy score on text data
#output Embedding 512
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(original, prediction)
accuracy

#accuracy score on text data
#output Embedding 1024
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(original, prediction)
accuracy

#accuracy score on text data
#output Embedding 256
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(original, prediction)
accuracy

# Plot the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(original, prediction)
sns.heatmap(cm, annot = True)
