import nltk
from nltk.chunk import *
from nltk.chunk.util import *
from nltk.chunk.regexp import *
from nltk import Tree

sentence = raw_input("Feed me language!: ")

tokens = nltk.word_tokenize(sentence)

entities = nltk.pos_tag(tokens)

parser = RegexpParser('''
ADJ: {<JJ>} #Adj -> 'JJ'
ADJP: {<ADJ>} #AdjP -> 'Adj'
N: {<NN.*>} #N -> 'NN'
V: {<V.*>} #V -> 'VBZ'
D: {<DT>*} #Det -> 'DT'
NP: {<ADJP>?<N>} #NP -> Adj N
DP: {<D>*<NP>?} #DP -> Det NP | Det
VP: {<V><DP>} #VP -> V DP
''')

tree = parser.parse(entities)

print(tree.pprint_latex_qtree())
print(entities)

tree.draw()
