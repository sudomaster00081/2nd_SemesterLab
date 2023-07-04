import spacy


#python -m spacy download en_core_web_sm
# Load the English language model in spaCy
nlp = spacy.load('en_core_web_sm')

# Function to print the token and its children recursively
def print_token_tree(token, level=0):
    print('  ' * level + token.text + ' - ' + token.dep_)
    for child in token.children:
        print_token_tree(child, level + 1)

# Function to process the text and print the token tree
def process_text(text):
    doc = nlp(text)
    for token in doc:
        if token.dep_ == 'ROOT':
            print_token_tree(token)

# Receive input text from the user
# text = input("Enter a sentence: ")
file = open("Text as a bag of words.txt", 'r')

# print(file)
text = file.read()

# Process the text and print the token tree
process_text(text)
