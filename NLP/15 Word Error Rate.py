# Find The Word Error Rate (WER) of a Sentence

# >>>>>> pip install nltk

import nltk

def wer(reference, hypothesis):
    reference = nltk.word_tokenize(reference.lower())
    hypothesis = nltk.word_tokenize(hypothesis.lower())
    edit_distance = nltk.edit_distance(reference, hypothesis)
    wer_score = edit_distance / len(reference)
    return wer_score
# Example usage
reference = "the quick brown fox jumps over the lazy dog"
hypothesis = "the quik brown fox jump over the lazi dog"
wer_score = wer(reference, hypothesis)
print("WER:", wer_score)
