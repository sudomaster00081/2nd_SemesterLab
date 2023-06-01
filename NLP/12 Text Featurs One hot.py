#Convert Text Features using one hot Encoding

# >>>> pip install scikit-learn

from sklearn.preprocessing import OneHotEncoder
# Sample corpus
corpus = ['This is the first document.',
          'This is the second document.',
          'And this is the third one.',
          'Is this the first document?']

# Create an instance of the OneHotEncoder class
encoder = OneHotEncoder()

# Fit the encoder to the corpus and transform the corpus into a one-hot encoded matrix
one_hot_encoded = encoder.fit_transform([[text] for text in corpus])

# Print the one-hot encoded matrix
print(one_hot_encoded.toarray())

