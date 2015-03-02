# import nltk
# from nltk.chunk import *
# from nltk.chunk.util import *
# from nltk.chunk.regexp import *
# from nltk import Tree
# sentence = raw_input("Feed me language!: ")
#
# tokens = nltk.word_tokenize(sentence)
#
# entities = nltk.pos_tag(tokens)
#
# parser = RegexpParser('''
# ADJ: {<JJ>} #Adj -> 'JJ'
# ADJP: {<ADJ>} #AdjP -> 'Adj'
# N: {<NN.*>} #N -> 'NN'
# V: {<V.*>} #V -> 'VBZ'
# D: {<DT>*<PRP>*} #Det -> 'DT'
# NP: {<ADJP>?<N>} #NP -> Adj N
# DP: {<D>*<NP>?} #DP -> Det NP | Det
# VP: {<V><DP>*<ADJP>*} #VP -> V DP
# ''')
#
# tree = parser.parse(entities)
#
# print("\n")
# print(tree.pprint_latex_qtree())
# print("\n")
# print(entities)
# tree.draw()

###################################################
# THAT AWKWARD MOMENT WHEN STANFORD ONE UPS YOUR PARSER #
###################################################

import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = './jars'
os.environ['STANFORD_MODELS'] = './jars'

#Create parser
parser = stanford.StanfordParser(model_path="./englishPCFG.ser.gz")

sentence = raw_input("Feed me language!: ")

#To do multiple sentences change to parser.raw_parse_sents(("sentence1", "sentence2"))
syntax = parser.raw_parse((sentence))

#Draw tree and then print qtree
for sentence in syntax:
    sentence.draw()
    print(sentence.pprint_latex_qtree())
