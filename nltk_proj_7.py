import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(filleid)), category)
             for category in movie_reviews.categories()
             for filleid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []

for word in movie_reviews.words():
    all_words.append(word.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]


def find_features(document):
    words = set(document)
    features = {}
    for word in word_features:
        features[word] = (word in words)

    return features


# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(find_features(rev), category) for (rev, category) in documents]

training_set = featuresets[:1900]
testing_set = featuresets[1900:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print(f"Naive Bayes Algoritm accuracy: {nltk.classify.accuracy(classifier, testing_set) * 100}")
classifier.show_most_informative_features(15)