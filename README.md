# Sentiment-Analysis-of-Product-Review
We live in a world where we are constantly bombarded with social media feeds, tweets and news article.
NLP or Natural Processing works by converting words into numbers. Then this numbers are used to train ML/AI Model to make predictions.
AI/ML - based sentiment analysis models, can be used to understand the sentiment from the public tweets, which can be used as a factor while making a buy/sell decision for securities.
In this project we use NLP and ML & AI to understand the text data and predict the sentiment using ML/AI model.
#Step 1: Exploring the data
We found data is of 5791 rows and 2 columns, with no null values.
Dataset contains two columns text and Sentiment(Positive and Negative)
We also found it is imbalanced dataset.


![alt text](https://github.com/ashg1998/Sentiment-Analysis-of-Product-Review/blob/main/images/sentiments.JPG)

#Step 2: Cleaning the Data
Removing all the punctuation marks.
Removing all the stop words from the text column.
stopwords list is also update with these words ['from', 'subject', 're', 'edu', 'use','will','aap','co','day','user','stock','today','week','year','https']. And then all
the stopwords is removed  while comparing with new stopwords list.
 
 #Step 3: In these step  text data is visualized.
 Positive Words:
![alt text](https://github.com/ashg1998/Sentiment-Analysis-of-Product-Review/blob/main/images/positive_wordcloud.jpg)

Negative Words:
![alt text](https://github.com/ashg1998/Sentiment-Analysis-of-Product-Review/blob/main/images/negative.jpg)

Negative WordCount:
![alt text](https://github.com/ashg1998/Sentiment-Analysis-of-Product-Review/blob/main/images/negative_wordcount.jpg)


Text Lenght in text column
![alt text](https://github.com/ashg1998/Sentiment-Analysis-of-Product-Review/blob/main/images/average_wordcount.jpg)

#Step 4: 
Words in Text columns is converted into words, i.e, Tokenized
After tokenizing the output is obtained in form of list, which is then padded into 29 length
LSTM Model is made:
![alt text](https://github.com/ashg1998/Sentiment-Analysis-of-Product-Review/blob/main/images/model_summary.jpg)

#Result:
We got the accuracy of 76%
Confusion Matrix
![alt text](https://github.com/ashg1998/Sentiment-Analysis-of-Product-Review/blob/main/images/confusion_matrix.jpg)



 
