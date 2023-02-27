# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 20:31:44 2023

@author: SPANDAN
"""
import string
from collections import Counter
import matplotlib.pyplot as plt
text = open('read.txt',encoding='utf-8').read()   #Reading the string

lower_case = text.lower()     #Converting text into lower case

clean_text = lower_case.translate(str.maketrans('','',string.punctuation))  #Cleaning the text by removing the punctuations

tokenize_word = clean_text.split()  #Tokenizing the words in a string

stop_word = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]  #list of words which provide no significant meaning to emotion analysis in a sentence.

final_word = []  #empty list to store all the words which are not stop words.
for word in tokenize_word:
    if word not in stop_word:
        final_word.append(word)
emotion_list = []
with open('emotion.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',', '').replace("'",'').strip()
        words, emotion = clear_line.split(':')
        if words in final_word:
            emotion_list.append(emotion)  
w = Counter(emotion_list)
print(w)       
'''print(lower_case)
print(clean_text)
print(tokenize_word)
print(final_word)'''
print(emotion_list)
fig, ax = plt.subplots()
ax.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()