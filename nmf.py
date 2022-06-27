from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer


out = '/home/julia/poetry/data/nlp_lektury_merge_pruned.txt'
vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=15000,
                             stop_words='\n')
X = vectorizer.fit_transform(out)
print(X)
# X = 
# model = NMF(n_components=100, init='random', random_state=0)
# W = model.fit_transform(X)
# H = model.components_