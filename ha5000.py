import nltk
from nltk.chunk import *
from nltk.chunk.util import *
from nltk.chunk.regexp import *
from nltk import Tree
from nltk.tag.stanford import POSTagger

#This NEEDS to be 'st' otherwise everything breaks
st = POSTagger('/home/ethan/Documents/git/homework-automator-5000/stanford-postagger/models/english-bidirectional-distsim.tagger', '/home/ethan/Documents/git/homework-automator-5000/stanford-postagger/stanford-postagger.jar')

userin = raw_input("Feed me language!: ")

sentence = st.tag(userin.split())

parser = RegexpParser('''
ADJ: {<JJ>} #Adj -> 'JJ'
ADJP: {<ADJ>} #AdjP -> 'Adj'
N: {<NN.*>} #N -> 'NN'
V: {<V.*>} #V -> 'VBZ'
D: {<DT>*<PRP>*} #Det -> 'DT'
NP: {<ADJP>?<N>} #NP -> Adj N
D\': {<D>} #D' -> 'D'
DP: {<D\'>*<NP>?} #DP -> Det NP | Det
VP: {<V><DP>*<ADJP>*} #VP -> V DP
''')

tree = parser.parse(sentence)

print("\n")
print(tree.pprint_latex_qtree())
print("\n")
print(sentence)
tree.draw()
