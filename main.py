# main.py
from src.lexer import tokenRecogniser
from src.lexer import addLineNumbers
from src.parser import parse
from src.codegen import pass2



with open("tests/example.lmc", "r") as file:
    words = file.read().split()
    print(words)
    if words[0] != "0":
        addLineNumbers()
        print("line numbers added")
    else:
        print("number lines do exist")

tokens = []
with open("tests/example.lmc", "r") as file:
    for line in file:
        result = tokenRecogniser(line)
        if result:
            tokens.extend(result)

for token in tokens:
    print(token)
pass1 = parse(tokens)
print(pass1)
print(pass2(tokens, pass1))