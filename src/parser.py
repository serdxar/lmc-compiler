#pass 1
def parse(tokens):
    labels = {}
    for i, token in enumerate(tokens):
        if token.label != "none":
            labels[token.label] = i
    return labels