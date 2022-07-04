# This imports the functionality to tokenize words and sentences
from nltk.tokenize import sent_tokenize, word_tokenize

example_string = """
 Muad'Dib learned rapidly because his first training was in how to learn.
 And the first lesson of all was the basic trust that he could learn.
 It's shocking  to find how many people do not believe they can learn,
 and how many more believe learning to be difficult."""

for word in word_tokenize(example_string):
    print(word)

# output
# Muad'Dib
# learned
# rapidly
# because
# his
# first
# training
# was
# in
# how
# to
# learn
# .
# And
# the
# first
# lesson
# of
# all
# was
# the
# basic
# trust
# that
# he
# could
# learn
# .
# It
# 's
# shocking
# to
# find
# how
# many
# people
# do
# not
# believe
# they
# can
# learn
# ,
# and
# how
# many
# more
# believe
# learning
# to
# be
# difficult
# .


for sentence in sent_tokenize(example_string):
    print(sentence)

# output
#  Muad'Dib learned rapidly because his first training was in how to learn.
# And the first lesson of all was the basic trust that he could learn.
# It's shocking  to find how many people do not believe they can learn,
#  and how many more believe learning to be difficult.
