from nltk.tokenize import sent_tokenize, word_tokenize

# nltk.download()  --> I would like to recommend you to install and download 'all'

example_text = "Hello mate, how are you? Today will be a good day! The weather is great. Best regards my friend."

print(sent_tokenize(example_text))
print(f"Length of sent tokenize: {len(sent_tokenize(example_text))}")
print(word_tokenize(example_text))
print(f"Length of word tokenize: {len(word_tokenize(example_text))}")

for word in word_tokenize(example_text):
    print(word)
