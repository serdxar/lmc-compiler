#lexer.py

#Step 0: add the line numbers
def addLineNumbers():
    import re
    with open("tests/example.lmc", "r") as file:
        lines = file.readlines()
        with open("tests/example.lmc", "w") as file:
            counter = 0
            for line in lines:
                file.write(f"{counter} {line}")
                counter += 1


instructions = ["ADD", "SUB", "STO", "LDA", "BRA", "BRP", "BRZ", "INP", "OUT", "HLT", "DAT"]

class Tokens():
    def __init__(self, line, label, mnemonic, operand):
        self.line = line
        self.label = label
        self.mnemonic = mnemonic
        self.operand = operand

    def __repr__(self):
        return f"Tokens({self.line}, {self.label}, {self.mnemonic}, {self.operand})"
    


def tokenRecogniser(text):
    tokens= []
    text = text.split("//")[0]
    words = text.split()
    if not words:
        return None
    #print(words)

    for i, ins in enumerate(words):
        if ins in instructions:
            if words[i-1].isdecimal() == False:
                # means there is a label
                if i+1 < len(words):
                    token = Tokens(words[i-2], words[i-1], ins, words[i+1])
                else:
                    token = Tokens(words[i-2], words[i-1], ins, "none")
            else: #there is no label
                if i+1 < len(words):
                    token = Tokens(words[i-1], "none", ins, words[i+1])
                else:
                    token = Tokens(words[i-1], "none", ins, "none")
            tokens.append(token)
    return(tokens)