# Read Text from an File and Print them as Tokens

# >>>>pip install nltk

import nltk
#nltk.download('punkt')

file = open("Text as a bag of words.txt", 'r')

# print (file)
text = file.read()

print(f"\n Text = \n {text}\n")

tokens = nltk.word_tokenize(text)


tokenWithCount = {}

for token in tokens:
    tokenWithCount[token] = 0
    
for token in tokens:
    tokenWithCount[token] = tokenWithCount[token] + 1 

for token in tokenWithCount:
    print(f"\nToken >> '{token}' count = {tokenWithCount[token]}")



