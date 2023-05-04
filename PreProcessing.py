import nltk
# nltk.download('punkt')
# nltk.download("stopwords")
from nltk.corpus import stopwords  # Text data
from nltk.corpus import wordnet as wn
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
# nltk.download('omw-1.4')
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
import string
import csv

lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("scarves")  # scarf
# from nltk.tokenize import RegexpTokenizer

stop_words = set(stopwords.words("english"))
# not working
# stop_words.add('not')
# stop_words.add('to')
# stop_words.add('the')
# stop_words.add('a')
# stop_words.add('they')

tag_map = {
    'CC': None,
    'CD': wn.NOUN,
    'DT': None,
    'EX': wn.ADV,
    'FW': None,
    'IN': wn.ADV,
    'JJ': wn.ADJ,
    'JJR': wn.ADJ,
    'JJS': wn.ADJ,
    'LS': None,
    'MD': None,
    'NN': wn.NOUN,
    'NNS': wn.NOUN,
    'NNP': wn.NOUN,
    'NNPS': wn.NOUN,
    'PDT': wn.ADJ,
    'POS': None,
    'PRP': None,
    'PRP$': None,
    'RB': wn.ADV,
    'RBR': wn.ADV,
    'RBS': wn.ADV,
    'RP': wn.ADV,
    'SYM': None,
    'TO': None,
    'UH': None,
    'VB': wn.VERB,
    'VBD': wn.VERB,
    'VBG': wn.VERB,
    'VBN': wn.VERB,
    'VBP': wn.VERB,
    'VBZ': wn.VERB,

}


class EnhanceSentence:

    def __init__(self, data):
        self.data = data

    def stopwords_removal(self):
        content_list = []
        for lines in self.data:
            lines = lines.translate(str.maketrans('', '', string.punctuation))
            words = word_tokenize(lines)
            filtered_list = [word for word in words if word.casefold() not in stop_words]  # remove stopwords
            lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_list]  # lemma the words
            # tags = pos_tag(lemmatized_words)
            # w_net_lemma = []
            # for tag in tags:
            #     w_net_lemma.append(lemmatizer.lemmatize(tag[0], pos=tag_map[tag[1]]))
            #     print(len(filtered_list))
            lines = ' '.join(lemmatized_words)
            content_list.append(lines)
            headers = ["title", "content"]
            OutPut_list = []
            OutPut_list.append([self.data[0], content_list])
            # with open("NLP", "w") as nlp:
            #     student = csv.writer(nlp)
            #     student.writerow(headers)
            #     student.writerows(OutPut_list)
        return content_list
