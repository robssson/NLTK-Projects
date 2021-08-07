from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# nltk.download()  --> I would like to recommend you to install and download 'all'

example_text = "Hello mate, how are you? Today will be a good day! The weather is great. Best regards my friend."

print(sent_tokenize(example_text))
print(f"Length of sent tokenize: {len(sent_tokenize(example_text))}")
print(word_tokenize(example_text))
print(f"Length of word tokenize: {len(word_tokenize(example_text))}")

stop_words = set(stopwords.words("english"))

words = word_tokenize(example_text)

filtered_text = []

filtered_text = [word for word in words if word not in stop_words]
print(filtered_text)
print(f"Length of word tokenize after filtering (stop_words): {len(filtered_text)}")

