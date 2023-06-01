# Perform steaming and levetization on Text

# >>>>> pip install textblob
# >>>>> pip install nltk
# >>>>> python -m textblob.download_corpora

from textblob import TextBlob

file = open('Text as a bag of words.txt')

text = file.read()

# Create a TextBlob object
blob = TextBlob(text)

# Perform stemming and lemmatization on each word in the text
stemmed_words = []
lemmatized_words = []
for word in blob.words:
    # Perform stemming on the word
    stemmed_word = word.stem()
    stemmed_words.append(stemmed_word)
    
    # Perform lemmatization on the word
    lemmatized_word = word.lemmatize()
    lemmatized_words.append(lemmatized_word)

# Print the results
print("Original text: ", text, "\n")
print("Stemmed text: ", " ".join(stemmed_words), "\n")
print("Lemmatized text: ", " ".join(lemmatized_words), "\n")
