#Remove Punctuations from text data

import string

file = open('NLP\Text as a bag of words.txt')

text = file.read()
# print(type(text))

print(f"\nText = \n{text}\n")

punctuations = string.punctuation
textwithout = ''
# print(type(textwithout))
for alph in text :
    if alph not in punctuations:
        textwithout = textwithout + alph

print(f"Punctuations removed Text = \n{textwithout}\n")
