D1 = "Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza."
D2 = "Five pizza were ready, but 3 bourak burned!"
D3 = "We only had 8 chamiyya, no pizza, and one tea."
D4 = "Is 6 too much? I ate nine bourak lol."


num_map = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}


def normalize(text):

    text = text.lower()

    punctuation = "!()-[]{};:,<>./?@#$%^&*_~'\""
    for c in punctuation:
        text = text.replace(c, "")

    words = text.split()

    for i in range(len(words)):
        if words[i] in num_map:
            words[i] = num_map[words[i]]

    return " ".join(words)



print("D1:", normalize(D1))
print("D2:", normalize(D2))
print("D3:", normalize(D3))
print("D4:", normalize(D4))