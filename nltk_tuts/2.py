# REMOVING STOP WORDS USING NLTK 


import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize, sent_tokenize

# Stop words in NLTK are common words that carry little to no semantic meaning in a given text. They typically include words like articles (“the”, “a”), prepositions (“in”, “on”), conjunctions (“and”, “but”), and pronouns (“he”, “she”) that do not contribute significantly to the text’s meaning or context.

stop_words = set(stopwords.words('english'))
# putting this inside a text to remove duplicates
# print(stop_words)

text = """Welcome you to programming knowledge. Lets start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""

demoWords = ["playing", "happiness", "going", "doing", "yes", "no", "I", "having", "had", "haved"]

word_tokens = word_tokenize(text)
# print(word_tokens)

# sentence_tokens = sent_tokenize(text)
# print(sentence_tokens)


# remove stop words from tokenized words

tokenized_words_without_stop_words = []

for word in word_tokens:
    if word not in stop_words:
        tokenized_words_without_stop_words.append(word)

# print(tokenized_words_without_stop_words)

# or we can use set operations to find the difference of words instead of this for loop

# print(set(tokenized_words_without_stop_words) - set(stop_words))


# to see removed words
stop_words_which_got_removed = set(word_tokens) - set(tokenized_words_without_stop_words)
print("TOKENIZED WORDS WHICH INCLUDED ALL THE WORDS INCLUDING STOP WORDS --> ", word_tokens)
print("TOKENS WITHOUT STOP WORDS --> ", tokenized_words_without_stop_words)
print("STOP WORDS WHICH GOT REMOVED --> ", stop_words_which_got_removed)
