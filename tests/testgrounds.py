import re
with open("tests/example.lmc", "rt") as file:
    n= 1
    text = file.read()
    word = [word for word in re.split(r"([ \t]+|\n)", text) if word and not word.isspace() or word == "\n"]
    print(word)