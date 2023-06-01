#remove Stopwords from a string

import nltk
from nltk.corpus import stopwords
# >>>>pip install nltk
#nltk.download('punkt')
#nltk.download('stopwords')

file = open('Text as a bag of words.txt')

text = file.read()

print(f"\n Text = \n {text}\n")

tokenizedText = nltk.word_tokenize(text)
tokensWithout = []
stopwordsall = []
stopwordsall.append(stopwords)
for token in tokenizedText:
    if token not in  stopwords.words() and token not in tokensWithout:
        tokensWithout.append(token)
        

print("\nClean Words :\n")
for token in tokensWithout:
    print (token)
