import PreProcessing
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def load_data():
    data = pd.read_csv("articles1.csv")
    content = data['content'].drop_duplicates().dropna()[:36000]
    title = data['title']
    return content, title


contents, titles = load_data()

p1 = PreProcessing.EnhanceSentence(contents)
enhanced_content = p1.stopwords_removal()
print(enhanced_content[0])

# # vectorizing using word count
# cv = CountVectorizer(stop_words="english")
# X = cv.fit_transform(contents)
# pd.DataFrame(X.toarray(), columns=cv.get_feature_names())

# vectorizing using tf-idf
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(enhanced_content)
# pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
K = 20
model = KMeans(n_clusters=K, init='k-means++', max_iter=100, n_init=1, random_state=1)
model.fit(X)

order_centroids = model.cluster_centers_.argsort()[:, ::-1]
print(order_centroids)

terms = vectorizer.get_feature_names()
for i in range(K):
    print("cluster %d : " % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])
    print('--------------------------------------------')

Y = vectorizer.transform(['china and korea are enemies.'])
prediction = model.predict(Y)
print(prediction)

# from yellowbrick.cluster import KElbowVisualizer
#
# km = KMeans(random_state=1)
# visualizer = KElbowVisualizer(km, k=(2, 5))
#
# visualizer.fit(X)  # Fit the data to the visualizer
# visualizer.show()  # Finalize and render the figure