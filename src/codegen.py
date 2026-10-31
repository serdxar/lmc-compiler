#pass 2
opcodes = {
    "ADD": 1, "SUB": 2, "STO": 3, "LDA": 5,
    "BRA": 6, "BRZ": 7, "BRP": 8
}
special_cases = {
    "INP": 901, "OUT": 902, "HLT": 0
}

def pass2(tokens, pass1):
    machine_code = []
    for token in tokens:
        if token.mnemonic == "DAT":
            if token.operand != "none":
                instruction = int(token.operand)
            else:
                instruction = 0
        elif token.mnemonic in special_cases:
            instruction = special_cases[token.mnemonic]
        else:
            if token.operand.isdecimal():
                address = int(token.operand)
            else:
                address = pass1[token.operand]
            instruction = opcodes[token.mnemonic]*100 + address
        machine_code.append(instruction)
    return machine_code