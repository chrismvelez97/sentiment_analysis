from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "learn php from guru99 and make study easy"

words_in_text = word_tokenize(text)

print(words_in_text)

# output
# ['learn', 'php', 'from', 'guru99', 'and', 'make', 'study', 'easy']

tokens_tag = pos_tag(words_in_text)

for item in tokens_tag:
    print(item)

# Output with tags
# ('learn', 'JJ')
# ('php', 'NN')
# ('from', 'IN')
# ('guru99', 'NN')
# ('and', 'CC')
# ('make', 'VB')
# ('study', 'NN')
# ('easy', 'JJ')
