# Create a Custom Function For text Standardization
import string
#import re 


def standardize(text):
    lower = text.lower()
    punctuations = string.punctuation

    textwithout = ''
    # print(type(textwithout))
    for alph in lower :
        if alph not in punctuations:
            textwithout = textwithout + alph
    numeric = '1','2','3','4','5','6','7','8','9','0'        


    textwithoutnum = ''            
    for num in textwithout :
        if num not in numeric:
            textwithoutnum = textwithoutnum + num
   
    return textwithoutnum

file = open('Text as a bag of words.txt')
text = file.read()

print(f"\nText = \n{text}\n")

print(f"\nNormalised Text = \n{standardize(text)}\n")








