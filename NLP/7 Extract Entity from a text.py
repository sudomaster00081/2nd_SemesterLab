# Extract Entity from a text

import spacy
import en_core_web_sm
#import en_core_web_trf
# >>>>pip install spacy
# >>>>python -m spacy download en_core_web_trf
# >>>>python -m spacy download en_core_web_sm

file = open ('Text as a bag of words.txt')
text = file.read()
#text = "Hello World"
NER = spacy.load("en_core_web_sm")
Entities = NER(text)

for word in Entities.ents:
    print(word.text,word.label_)