# SENTIMENT ANALYSIS, LEMMATIZATION AND STEMMING

import nltk
nltk.download('wordnet')

# Stemming in NLTK refers to the process of reducing words to their root or base form, known as the stem. This technique is used in Natural Language Processing (NLP) and Information Retrieval (IR) to group related words together, improve search queries, and enhance text analysis. NLTK provides several stemmers, each with its own algorithm and characteristics.

# The most well-known stemmers in NLTK are:

# Porter Stemmer (PorterStemmer): Developed by Martin Porter, this algorithm reduces words to their stem using a series of rules. It’s fast and simple but may not always produce the most accurate results.
# Snowball Stemmer (SnowballStemmer): Also developed by Martin Porter, this stemmer is an improvement over the Porter Stemmer. It’s faster and more logical, and it’s often used for English text.
# Lancaster Stemmer (LancasterStemmer): This stemmer uses a set of predefined rules to reduce words to their stem. It’s slower than the Porter Stemmer but can produce more accurate results.
# Regex Stemmer (RegexpStemmer): This stemmer uses regular expressions to identify and remove suffixes. It’s a rule-based approach that can be customized for specific languages or text types.



# Lemmatizers in NLTK are used to reduce words to their base or dictionary form, known as the lemma, by considering the context of the word and its part-of-speech (POS) tag. Unlike stemming, lemmatization takes into account the word’s meaning and grammatical category, resulting in more accurate reductions.



from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer

text = """Welcome you to programming knowledge. Lets start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""

demoWords = ["playing", "happiness", "going", "doing", "yes", "no", "I", "having", "had", "haved", "coding", "programming", "code", "program"] #having and haved are related to each other, similarly programming and program , doing and do


lematizer = WordNetLemmatizer()
stemmer = PorterStemmer()

for word in demoWords:
    #word , stem , lemmatize
    print(word, stemmer.stem(word), lematizer.lemmatize(word, "v"))
    #lemmatization is more accurate
    #both have thier advantages and disadvantages


#download vader_lexicon for sentiment analysis
nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

#to check negativity, positivity or neutrality of a statement
print(sia.polarity_scores("Programming is fun"))
print(sia.polarity_scores("Programming is not fun"))