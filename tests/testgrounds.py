import re
space = "    "
with open("tests/example.lmc", "r") as file:
    lines = file.readlines()
    with open("tests/example.lmc", "w") as file:
        counter = 00
        for line in lines:
            file.write(f"{counter} {line}")
            counter += 1

    