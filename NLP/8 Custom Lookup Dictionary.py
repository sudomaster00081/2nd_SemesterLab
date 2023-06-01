# Create a custom Lookup Dictionary and Create a Custom Function For text Standardization

# >>>>pip install nltk

import nltk
#nltk.download('punkt')

lookup_dict = {
    'btw': 'by the way',
    'lol': 'laugh out loud',
    'idk': 'I don\'t know',
    'omg': 'oh my god',
    'wtf': 'what the heck',
    # Add more entries as needed
}

def standardize_text(text, lookup_dict):
    words = text.lower().split()
    standardized_words = [lookup_dict.get(word, word) for word in words]
    standardized_text = ' '.join(standardized_words)
    return standardized_text

text = "btw idk what to do lol"
standardized_text = standardize_text(text, lookup_dict)
print(standardized_text)
