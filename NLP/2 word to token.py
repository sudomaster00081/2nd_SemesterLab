# Read Text from an File and Print them as Tokens

# >>>>pip install nltk

import nltk
#nltk.download('punkt')


file = open("NLP\Text as a bag of words.txt", 'r')

# print(file)
text = file.read()

print(f"\n Text = \n {text}\n")

tokens = nltk.word_tokenize(text)

print (tokens)