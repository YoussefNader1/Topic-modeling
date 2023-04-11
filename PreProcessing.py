import nltk
# nltk.download('punkt')
# nltk.download("stopwords")
from nltk.corpus import stopwords  # Text data
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
# nltk.download('omw-1.4')
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("scarves")  # scarf
# from nltk.tokenize import RegexpTokenizer

stop_words = set(stopwords.words("english"))
stop_words.add('not')


class PreProcessing:

    def __init__(self, data):
        self.data = data

    def stopwords_removal(self):
        content_list = []
        for lines in self.data:
            words = word_tokenize(lines)
            filtered_list = [word for word in words if word.casefold() not in stop_words]  # remove stopwords
            lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_list]  # lemma the words
            #     print(len(filtered_list))
            lines = ' '.join(lemmatized_words)
            content_list.append(lines)
        return content_list
