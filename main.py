import nltk
# nltk.download('punkt')
# nltk.download("stopwords")
from nltk.corpus import stopwords # Text data
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
# nltk.download('omw-1.4')
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("scarves") # scarf
from nltk.tokenize import RegexpTokenizer


example_string = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult."""

print(word_tokenize(example_string))