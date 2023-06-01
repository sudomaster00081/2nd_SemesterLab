# Convert Text Features using a count vectoriser

# >>>> pip install scikit-learn
# >>>> pip install pandas

from sklearn.feature_extraction.text import CountVectorizer

# Sample text data
text_data = ['This is the first document.', 'This is the second second document.', 'And the third one.', 'Is this the first document?']

# Creating instance of CountVectorizer
cv = CountVectorizer()
# Transforming text data to document-term matrix
doc_term_matrix = cv.fit_transform(text_data)

# Creating vocabulary of the text data
vocab = cv.get_feature_names_out()

# Creating a pandas dataframe of the document-term matrix
import pandas as pd
df = pd.DataFrame(doc_term_matrix.toarray(), columns=vocab)

# Viewing the dataframe
print(df)
