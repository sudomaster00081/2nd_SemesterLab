#Correct Spelling Mistake of Given Words

#>>>> pip install autocorrect

from autocorrect import Speller

# Create an instance of the spell checker
spell = Speller()
# List of words with spelling errors
words_with_errors = ["Wrold", "helo", "recieve", "acccomodate"]

# Correct the spelling errors in the words
for word in words_with_errors:
    corrected_word = spell(word)
    print(f"{word} -> {corrected_word}")
