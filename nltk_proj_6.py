from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

example_text = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(example_text)
print(tok[1:10])
