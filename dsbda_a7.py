# -*- coding: utf-8 -*-
"""Copy of A7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Egjbyst_ZnPOkGwtjacxTe_AW3fvDK_h

A7 Text Analytics
1. Extract Sample document and apply following document preprocessing methods:
Tokenization, POS Tagging, stop words removal, Stemming and Lemmatization.
2. Create representation of document by calculating Term Frequency and Inverse Document
Frequency.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import nltk

file=open('/content/ds.txt','r')
#keep file outside sample data for colab and in same folder for jn
#for jn
#file=open('ds.txt','r')

nltk.download('all')

file

content=file.read()
content

from nltk.tokenize import sent_tokenize

sentence = sent_tokenize(content)
sentence

from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer(f"\w+")
words=tokenizer.tokenize(content)
words

tokenizer=RegexpTokenizer(f"\s")
words1=tokenizer.tokenize(content)
words1

#POS tagging and stop word removing
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopWords=set(stopwords.words('english'))

print(stopWords)

for sen in sentence:
    Words=word_tokenize(sen)
    filteredWords=[word.lower() for word in Words if word.lower() not in stopWords]
    print(f"words without stopwords{filteredWords}")
    print(f"words with stopwords{Words}")

#POS tagging
for sen in sentence:
    Words=word_tokenize(sen)
    filteredWords=[word.lower() for word in Words if word.lower() not in stopWords]
    tagged = nltk.pos_tag(filteredWords)
    print(tagged)

#OR
tagged = nltk.pos_tag(words)
print(tagged)

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

for sen in sentence:
    Words=word_tokenize(sen)
    filteredWords=[word.lower() for word in Words if word.lower() not in stopWords]

    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filteredWords]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filteredWords]

    print("\nOriginal Tokens:", Words)
    print("Stemmed Tokens:", stemmed_tokens)
    print("Lemmatized Tokens:", lemmatized_tokens)

#OR
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in words]

lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in words]

print("\nOriginal Tokens:", Words)
print("Stemmed Tokens:", stemmed_tokens)
print("Lemmatized Tokens:", lemmatized_tokens)

#the difference between first and second is that in first approach we performed it on filtered words and in the second we performed it on simple array of words

# 6. TF-IDF Calculation
# TF-IDF Vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform([content])

# Show the TF-IDF scores for the terms in the document
terms = vectorizer.get_feature_names_out()
print("\nTF-IDF Scores:")
for term, score in zip(terms, tfidf_matrix.toarray()[0]):
    print(f"{term}: {score}")