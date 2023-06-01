#Generate N-Grams For a Given Sentence

# >>>> pip install nltk

#import nltk
from nltk import ngrams

def Ngram(sentence, n):
    trigrams = ngrams(sentence.split(), n)
    # Print the trigrams
    for gram in trigrams:
        print(gram)

# Sample sentence
sentence = "The quick brown fox jumps over the lazy dog"

# Generate trigrams for the sentence
for i in range(1, 5):
    print(f"\n{i} - Gram:")
    Ngram(sentence, i)
