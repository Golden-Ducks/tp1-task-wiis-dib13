D1 = "I love cats"
D2 = "Cats are chill"
D3 = "I am late"


def preprocess_text(text):
    text = text.lower()
    tokens = text.split()
    return tokens



def add_padding(tokens):
    return ["<s>"] + tokens + ["</s>"]



def extract_windows(tokens, window_size=1):
    windows = []

    for i in range(window_size, len(tokens) - window_size):
        window = tokens[i - window_size : i + window_size + 1]
        windows.append(" ".join(window))

    return windows



def build_vocab(all_windows):
    vocab_set = set()

    for doc_windows in all_windows:
        for window in doc_windows:
            vocab_set.add(window)

    vocab = sorted(list(vocab_set))
    return vocab



def vectorize_doc(doc_windows, vocab):
    vector = []

    for word in vocab:
        if word in doc_windows:
            vector.append(1)
        else:
            vector.append(0)

    return vector



all_docs = [D1, D2, D3]
all_windows = []

for doc in all_docs:
    tokens = preprocess_text(doc)
    padded_tokens = add_padding(tokens)
    windows = extract_windows(padded_tokens, window_size=1)
    all_windows.append(windows)


vocab = build_vocab(all_windows)


v1 = vectorize_doc(all_windows[0], vocab)
v2 = vectorize_doc(all_windows[1], vocab)
v3 = vectorize_doc(all_windows[2], vocab)


print("Windows of D1:", all_windows[0])
print("Windows of D2:", all_windows[1])
print("Windows of D3:", all_windows[2])

print("\nVocabulary:")
for i in range(len(vocab)):
    print(i, ":", vocab[i])

print("\nVector D1:", v1)
print("Vector D2:", v2)
print("Vector D3:", v3)