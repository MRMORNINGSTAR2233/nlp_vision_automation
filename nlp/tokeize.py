
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import nltk
import ssl

"""
Sample code to tokenize text
"""
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt_tab')
sample_text = "I love programming!"
tokens = word_tokenize(sample_text)
print("Tokens:", tokens)
"""
Sample code to generate n-grams
"""
text = "I love programming in Python. I also love using Python for data science."
token = word_tokenize(text)
trigrams = list(ngrams(tokens, 3))
print("Trigrams:", trigrams)
