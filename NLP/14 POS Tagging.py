# Tag The Parts Of Speech (POS Tagging) in a Sentence

# >>>> pipp install nltk

import nltk

# Downloading required packages for nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

# Sample sentence
sentence = "The quick brown fox jumps over the lazy dog."

# Tokenizing the sentence into words
words = nltk.word_tokenize(sentence)

# Tagging the parts of speech in the words
pos_tags = nltk.pos_tag(words)
# Printing the tagged words
print(pos_tags)
