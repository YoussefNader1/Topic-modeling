import PreProcessing
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


def load_data():
    data = pd.read_csv("articles1.csv")
    content = data['content']
    title = data['title']
    return content, title


contents, titles = load_data()

# vectorizing using word count
cv = CountVectorizer(stop_words="english")
X = cv.fit_transform(contents)
pd.DataFrame(X.toarray(), columns=cv.get_feature_names())

# vectorizing using tf-idf
cv_tfidf = TfidfVectorizer()
X_tfidf = cv_tfidf.fit_transform(contents)
pd.DataFrame(X_tfidf.toarray(), columns=cv_tfidf.get_feature_names())
