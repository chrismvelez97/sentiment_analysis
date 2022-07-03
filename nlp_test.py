from nltk.corpus import twitter_samples
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
import re, string

positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
text = twitter_samples.strings('tweets.20150430-223406.json')

# Tokenizes text breaking it up into pieces
tweet_tokens = twitter_samples.tokenized('positive_tweets.json')

print(tweet_tokens[0])

def lemmatize_sentence(tokens):
    # imports lemmatizer class and assigns it to variable
    lemmatizer = WordNetLemmatizer()

    # New list that will return tokenized sentence lemmatized
    lemmatized_sentence = []

    # Parses tokenized sentence and tags word type
    for word, tag in pos_tag(tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        # Appends lemmatized words back to lemmatized_sentence list using tags
        lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
    return (lemmatized_sentence)

def remove_noise(tweet_tokens, stop_words()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):

        token = re.sub('http[s]?://')
