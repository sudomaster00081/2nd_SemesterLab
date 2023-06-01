#Convert Text Data Into Lowercase

file = open('Text as a bag of words.txt')
text = file.read()
lower = text.lower()
print(f"\nText = \n{text}\n")

print(f"Lowered Text = \n{lower}\n")