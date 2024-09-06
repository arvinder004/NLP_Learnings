# GETTING STARTED WITH NLTK


import nltk
nltk.download('punkt_tab') #installer for nltk

#nltk.download() open a window to install

text = """Welcome you to programming knowledge. Lets start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""



#WORD TOKENIZATION
from nltk.tokenize import word_tokenize
word_tokens = word_tokenize(text)
print("WORD TOKENIZATION->",word_tokens)

#SENTENCE TOKENIZATION
from nltk.tokenize import sent_tokenize
sentence_tokens = sent_tokenize(text)
print("SENTENCE TOKENIZATION->",sentence_tokens)


#to find occurence of words/probablity
from nltk.probability import FreqDist
fd = FreqDist(word_tokens)
print(fd) #outputs the samples and outcomes
print(fd.most_common(3)) #outputs most common words

#install matplotlib
import matplotlib.pyplot as plt

#to output graph with frequencies of words
fd.plot(30, cumulative=False) #30 as a scale
plt.show()