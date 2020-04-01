import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(ex)
print(sent)

#find pattern
pattern = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print(cs)

#show hierarchy
from nltk.chunk import conlltags2tree, tree2conlltags, ne_chunk
from pprint import pprint
iob_tagged = tree2conlltags(cs)
pprint(iob_tagged)

#recognize name entity
ne_tree = ne_chunk(pos_tag(word_tokenize(ex)))
print(ne_tree)