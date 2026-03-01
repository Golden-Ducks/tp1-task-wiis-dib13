D1 = "I feel good."
D2 = "I do feel even better now, thank you!"
D3 = "What's happened to you? you all good?"

def clean(text):
    text = text.lower()
    ponctuation = "!?.,'"
    for c in ponctuation:
        text = text.replace(c, "")
    
    mots = text.split()
    resultat = []
    for m in mots:
        if m not in ["i", "do", "even", "now", "thank", "what", "to", "you", "all"]:
            resultat.append(m)
    return resultat


D1_c = clean(D1)  
D2_c = clean(D2)  
D3_c = clean(D3)  

print("D1 =", D1_c)
print("D2 =", D2_c)
print("D3 =", D3_c)
print()

vocab = []
for doc in [D1_c, D2_c, D3_c]:
    for mot in doc:
        if mot not in vocab:
            vocab.append(mot)

print("Vocabulaire =", vocab)  
print()

def vect(doc, vocab):
    v = []
    for mot in vocab:
        v.append(1 if mot in doc else 0)
    return v

print("D1 →", vect(D1_c, vocab))
print("D2 →", vect(D2_c, vocab))
print("D3 →", vect(D3_c, vocab))