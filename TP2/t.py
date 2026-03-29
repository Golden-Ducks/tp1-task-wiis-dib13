import numpy as np
from sklearn.cluster import KMeans


doc1 = "The gold medal price is high effort"
doc2 = "Winning a gold medal needs a high jump"
doc3 = "Market for a gold medal is a trade of sweat"
doc4 = "The athlete will trade all for a gold medal"


doc5 = "The gold bars price is high today"
doc6 = "Investing in gold bars needs a high rate"
doc7 = "Market for gold bars is a trade of money"
doc8 = "The bank will trade all for gold bars"


def preprocess_text(text):
   
    text = text.lower()

 
    punctuation = ".,!?;:()[]{}\"'-"
    for p in punctuation:
        text = text.replace(p, "")


    tokens = text.split()

    return tokens



def make_ngrams(tokens, n):
    ngrams = []

    for i in range(len(tokens) - n + 1):
        gram = " ".join(tokens[i:i+n])
        ngrams.append(gram)

    return ngrams



def vectorize(docs, n_gram_size=1):
    all_doc_ngrams = []

   
    for doc in docs:
        tokens = preprocess_text(doc)
        ngrams = make_ngrams(tokens, n_gram_size)
        all_doc_ngrams.append(ngrams)

 
    vocab_set = set()
    for ngrams in all_doc_ngrams:
        for gram in ngrams:
            vocab_set.add(gram)


    vocab = sorted(list(vocab_set))


    vectors = []
    for ngrams in all_doc_ngrams:
        vector = []
        for word in vocab:
            if word in ngrams:
                vector.append(1)
            else:
                vector.append(0)
        vectors.append(vector)

    return np.array(vectors), vocab


all_docs = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8]


true_labels = [0, 0, 0, 0, 1, 1, 1, 1]



X1, vocab1 = vectorize(all_docs, n_gram_size=1)
km1 = KMeans(n_clusters=2, random_state=42)
km1.fit(X1)
pred1 = km1.labels_



X2, vocab2 = vectorize(all_docs, n_gram_size=2)
km2 = KMeans(n_clusters=2, random_state=42)
km2.fit(X2)
pred2 = km2.labels_



def clustering_accuracy(true_labels, pred_labels):
    
    correct1 = 0
    for i in range(len(true_labels)):
        if true_labels[i] == pred_labels[i]:
            correct1 += 1

    flipped = [1 - x for x in pred_labels]
    correct2 = 0
    for i in range(len(true_labels)):
        if true_labels[i] == flipped[i]:
            correct2 += 1

    best_correct = max(correct1, correct2)
    return best_correct / len(true_labels)



print(" 1-gram ")
print("Vocabulary:")
print(vocab1)
print("Clusters:", pred1)
print("Accuracy:", clustering_accuracy(true_labels, list(pred1)))

print("\n 2-gram ")
print("Vocabulary:")
print(vocab2)
print("Clusters:", pred2)
print("Accuracy:", clustering_accuracy(true_labels, list(pred2)))